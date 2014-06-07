# Spanish verb conjugations
from collections import namedtuple

# Spanish has two forms of the sps familiar - 'tú' and 'vos'
SpanishCategory = namedtuple('SpanishCategory', 'fps sps spsv tps fpp spp tpp')

_PRONOUNS = SpanishCategory('yo', 'tú', 'vos', 'él/ella/usted',
                           'nosotros/nosotras', 'vosotros/vosotras',
                           'ellos/ellas/ustedes')

_STD_FORMAT = '{} {}'
_STD_CLOZE_FORMAT = '{0} {{{{c1::{1}::{2}, {3}}}}}'

# Endings for the simple tenses
_ENDINGS =\
    {'ar':
     {'presente': SpanishCategory('o', 'as', 'ás',  'a',
                                  'amos', 'áis', 'an'),
      'pretérito imperfecto': SpanishCategory('aba', 'abas', 'abas', 'aba',
                                              'ábamos', 'abais', 'aban'),
      'futuro simple': SpanishCategory('é', 'ás', 'ás', 'á',
                                       'emos', 'éis', 'án'),
      'pretérito indefinido': SpanishCategory('é', 'aste(s)', 'aste(s)', 'ó',
                                              'amos', 'asteis', 'aron')
  },
     'er':
     {'presente': SpanishCategory('o', 'es', 'és', 'e',
                                  'emos', 'éis', 'en'),
      'pretérito imperfecto': SpanishCategory('ía', 'ías', 'ías', 'ía',
                                              'íamos', 'íais', 'ían'),
      'futuro simple': SpanishCategory('é', 'ás', 'ás', 'á',
                                       'emos', 'éis', 'án'),
      'pretérito indefinido': SpanishCategory('í', 'iste(s)', 'iste(s)','ió',
                                              'imos', 'isteis', 'ieron')
  },
     'ir':
     {'presente': SpanishCategory('o', 'es', 'ís', 'e',
                                  'imos', 'ís', 'en'),
      'pretérito imperfecto': SpanishCategory('ía', 'ías', 'ías', 'ía',
                                              'íamos', 'íais', 'ían'),
      'futuro simple': SpanishCategory('é', 'ás', 'ás', 'á',
                                       'emos', 'éis', 'án'),
      'pretérito indefinido': SpanishCategory('í', 'iste(s)', 'iste(s)', 'ió',
                                              'imos', 'isteis', 'ieron')
  }
}

# logic for adjusting the stem of the verb for the case
_STEM_RULES =\
    {'presente': (lambda x: x[:-2]),
     'pretérito imperfecto': (lambda x: x[:-2]),
     'futuro simple': (lambda x: x),
     'pretérito indefinido': (lambda x: x[:-2])
}


def construct_stem_and_ending(infinitive, tense):
    stem = _STEM_RULES[tense](infinitive)
    verb_type = infinitive[-2:]
    endings = _ENDINGS[verb_type][tense]
    return SpanishCategory._make([stem + end for end in endings])


def construct_inflection(infinitive, tense):
    '''
    Given an infinitive and tense, constructs the combined
    stem and ending, and then prepends the appropriate pronoun
    '''
    stem_and_ending = construct_stem_and_ending(infinitive, tense)
    return SpanishCategory._make([item for item in zip(_PRONOUNS,
                                                       stem_and_ending)])
def output_normal_view(infinitive, tense, conj):
    '''
    Pretty-printing for the traditional two-column output
    of a verb conjugation
    '''
    return ['{}, {}:'.format(infinitive, tense),
    ('⎯'*45), '{:<25}‖ {}'.format(_STD_FORMAT.format(*conj.fps),
                                  _STD_FORMAT.format(*conj.fpp)),
    '{:<25}‖ {}'.format(_STD_FORMAT.format(*conj.sps),
                        _STD_FORMAT.format(*conj.spp)),
    '{:<25}‖'.format(_STD_FORMAT.format(*conj.spsv)),
    '{:<25}‖ {}'.format(_STD_FORMAT.format(*conj.tps),
                        _STD_FORMAT. format(*conj.tpp))]

def output_cloze(infinitive, tense, conj):
    '''
    Combines the different parts of a verb conjugation with
    Anki's required formatting to produce a form suitable
    for a cloze-deletion card
    '''
    result = []
    # TODO - make this pythonic, it's an ugly hack as it is
    for i, item in enumerate(conj):
       result.append(_STD_CLOZE_FORMAT.format(item[0], item[1],
                                             infinitive, tense))
    return SpanishCategory._make(result)


def output_cloze_import(infinitive, tense, translation, sound, conj):
    '''
    Combines the output of the output_cloze function with optional
    translation and sound fields and combines them to produce the
    format required for Anki's import function
    '''
    cloze = output_cloze(infinitive, tense, conj)
    if translation:
        add_trn = [cz + ('|{}'.format(trn)) for cz, trn in
                   zip(cloze, translation)]
    else:
        add_trn = [cz + '|' for cz in cloze]

    if sound:
        add_snd = [trn + ('|[sound:{}]'.format(snd)) for
                   trn, snd in zip(add_trn, sound)]
    else:
        add_snd = [trn + '|' for trn in add_trn]

    add_tag = [snd + ('|{}'.format(infinitive)) for snd in add_snd]

    return SpanishCategory._make(add_tag)
