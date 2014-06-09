# Name:    french.py
# Author:  Michael Ealem
# Purpose: conjugate french verb tenses

from category import Category

# French pronouns - easy way to handle the j'/je problem
# when the first letter of the verb is a vowel
# TODO: handle the case of the unaspirated h

_PRONOUNS = Category((lambda stem: "j'" if stem[0]
                      in _VOWELS else 'je'),
                     (lambda stem: 'tu'),
                     (lambda stem: 'il/elle/on'),
                     (lambda stem: 'nous'),
                     (lambda stem: 'vous'),
                     (lambda stem: 'ils/elles'))

_FPS_FORMAT = '{}{}'
_STD_FORMAT = '{} {}'
_FPS_CLOZE_FORMAT = '{0}{{{{c1::{1}::{2}, {3}}}}}'
_STD_CLOZE_FORMAT = '{0} {{{{c1::{1}::{2}, {3}}}}}'


_VOWELS = ('a', 'e', 'i', 'o', 'u')


def imparfait(infinitive):
    '''
    Creates the appropriate stem from the présent case
    '''
    stem = construct_stem_and_ending(infinitive, 'présent').fpp
    return stem.rsplit('ons')[0]


def présent_subjonctif(infinitive):
    '''
    Creates the appropriate stem from the présent case
    '''
    stem = construct_stem_and_ending(infinitive, 'présent').tpp
    return stem.rsplit('ent')[0]


_TENSES =\
          [# simple tenses
              'présent',
              'passé simple',
              'imparfait',
              'futur',
              'conditionnel'
              'subjonctif présent',
              'subjonctif imparfait',
           # compound tenses
              'passé composé',
              'plus-que-parfait',
              'futur antérieur',
              'passé antérieur',
              'subjonctif passé',
              'subjonctif plus-que-parfait',
              'passé du conditionnel'
          ]


# Logic for handling the different stem changes of regular verbs
_STEM_RULES =\
{'présent': (lambda x: x[:-2]),
 'futur': (lambda x: x[:-1] if x[-2:] == 're' else x),
 'imparfait': imparfait,
 'passé simple': (lambda x: x[:-2]),
 'conditionnel': (lambda x: x[:-1] if x[-2:] == 're' else x),
 'présent subjonctif': présent_subjonctif,
 'imparfait subjonctif': (lambda x: x[:-2])}

# Simple Tense endings
# TODO: add the compound tenses and handle stem- and spelling-change
# verbs
_ENDINGS =\
    {'er':
     {'présent': Category('e', 'es', 'e', 'ons', 'ez', 'ent'),
      'imparfait': Category('ais', 'ais', 'ait', 'ions', 'iez', 'aient'),
      'passé simple': Category('ai', 'as', 'a', 'âmes', 'âtes', 'èrent'),
      'futur': Category('ai', 'as', 'a', 'ons', 'ez', 'ont'),
      'conditionnel': Category('ais', 'ais', 'ait', 'ions', 'iez', 'aient'),
      'présent subjonctif': Category('e', 'es', 'e', 'ions', 'iez', 'ent'),
      'imparfait subjonctif': Category('asse', 'asses', 'ât',
                                       'assions', 'assiez', 'assent')},
     'ir':
     {'présent': Category('is', 'is', 'it', 'issons', 'issez', 'issent'),
      'imparfait': Category('ais', 'ais', 'ait', 'ions', 'iez', 'aient'),
      'passé simple': Category('is', 'is', 'it', 'îmes', 'îtes', 'irent'),
      'futur': Category('ai', 'as', 'a', 'ons', 'ez', 'ont'),
      'conditionnel': Category('ais', 'ais', 'ait', 'ions', 'iez', 'aient'),
      'présent subjonctif': Category('e', 'es', 'e', 'ions', 'iez', 'ent'),
      'imparfait subjonctif': Category('isse', 'isses', 'ît',
                                       'issions', 'issiez', 'issent')
  },
     're':
     {'présent': Category('s', 's', '', 'ons', 'ez', 'ent'),
      'imparfait': Category('ais', 'ais', 'ait', 'ions', 'iez', 'aient'),
      'passé simple': Category('is', 'is', 'it', 'îmes', 'îtes', 'irent'),
      'futur': Category('ai', 'as', 'a', 'ons', 'ez', 'ont'),
      'conditionnel': Category('ais', 'ais', 'ait', 'ions', 'iez', 'aient'),
      'présent subjonctif': Category('e', 'es', 'e', 'ions', 'iez', 'ent'),
      'imparfait subjonctif': Category('isse', 'isses', 'ît',
                                       'issions', 'issiez', 'issent')
  }
}


def imparfait_subjonctif(infinitive):
    '''
    Creates the appropriate stem from the passé simple case
    '''

    stem = construct_inflection(infinitive, 'passé simple').tps
    return stem[:-1]


def construct_stem_and_ending(infinitive, tense):
    '''
    Given an infinitive and a tense, looks up the appropriate
    transformation rules and concatenates the resultant stem and
    ending
    '''
    stem = _STEM_RULES[tense](infinitive)
    verb_type = infinitive[-2:]
    endings = _ENDINGS[verb_type][tense]
    return Category._make([stem + end for end in endings])


def construct_inflection(infinitive, tense):
    '''
    Given an infinitive and tense, constructs the combined
    stem and ending, and then prepends the appropriate pronoun
    '''
    stem_and_ending = construct_stem_and_ending(infinitive, tense)
    return Category._make([(f(c), c) for f, c in zip(_PRONOUNS,
                                                     stem_and_ending)])


def output_normal_view(infinitive, tense, conj):
    '''
    Pretty-printing for the traditional two-column output
    of a verb conjugation
    '''
    return ['{}, {}:'.format(infinitive, tense),
    ('⎯'*45), '{:<25}‖ {}'.format(_FPS_FORMAT.format(*conj.fps) if
                                  infinitive[0] in _VOWELS else
                                  _STD_FORMAT.format(*conj.fps),
                                  _STD_FORMAT.format(*conj.fpp)),
    '{:<25}‖ {}'.format(_STD_FORMAT.format(*conj.sps),
                        _STD_FORMAT.format(*conj.spp)),
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
        if i == 0 and infinitive[0] in _VOWELS:
            result.append(_FPS_CLOZE_FORMAT.format(item[0], item[1],
                                             infinitive, tense))
        else:
            result.append(_STD_CLOZE_FORMAT.format(item[0], item[1],
                                             infinitive, tense))
    return Category._make(result)


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

    return Category._make(add_tag)
