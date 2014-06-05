# Spanish verb conjugations
from collections import namedtuple

# Spanish has two forms of the sps familiar - 'tú' and 'vos'
SpanishCategory = namedtuple('SpanishCategory', 'fps sps spsv tps fpp spp tpp')

_PRONOUNS = SpanishCategory('yo', 'tú', 'vos', 'él/ella/usted',
                           'nosotros/nosotras', 'vosotros/vosotras',
                           'ellos/ellas/ustedes')

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


def construct_inflection(infinitive, tense):
    stem = _STEM_RULES[tense](infinitive)
    verb_type = infinitive[-2:]
    end = _ENDINGS[verb_type][tense]

    return SpanishCategory._make([stem + e for e in end])
