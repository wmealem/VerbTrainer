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

_FPS_FORMAT = '{0}{{{{c1::{1}::{2}, {3}}}}}'

_STD_FORMAT = '{0} {{{{c1::{1}::{2}, {3}}}}}'

_VOWELS = ('a', 'e', 'i', 'o', 'u')


def imparfait(infinitive):
    '''
    Creates the appropriate stem from the présent case
    '''
    stem = construct_stem_and_ending(infinitive, 'Présent').fpp
    return stem.rsplit('ons')[0]


def présent_subjonctif(infinitive):
    '''
    Creates the appropriate stem from the présent case
    '''
    stem = construct_stem_and_ending(infinitive, 'Présent').tpp
    return stem.rsplit('ent')[0]

# Logic for handling the different stem changes of regular verbs
_STEM_RULES =\
{'Présent': (lambda x: x[:-2]),
 'Futur': (lambda x: x[:-1] if x[-2:] == 're' else x),
 'Imparfait': imparfait,
 'Passé simple': (lambda x: x[:-2]),
 'Conditionnel': (lambda x: x[:-1] if x[-2:] == 're' else x),
 'Présent subjonctif': présent_subjonctif,
 'Imparfait subjonctif': (lambda x: x[:-2])}

# Simple Tense endings
# TODO: add the compound tenses and handle stem- and spelling-change
# verbs
_ENDINGS =\
    {'er':
     {'Présent': Category('e', 'es', 'e', 'ons', 'ez', 'ent'),
      'Imparfait': Category('ais', 'ais', 'ait', 'ions', 'iez', 'aient'),
      'Passé simple': Category('ai', 'as', 'a', 'âmes', 'âtes', 'èrent'),
      'Futur': Category('ai', 'as', 'a', 'ons', 'ez', 'ont'),
      'Conditionnel': Category('ais', 'ais', 'ait', 'ions', 'iez', 'aient'),
      'Présent subjonctif': Category('e', 'es', 'e', 'ions', 'iez', 'ent'),
      'Imparfait subjonctif': Category('asse', 'asses', 'ât',
                                       'assions', 'assiez', 'assent')},
     'ir':
     {'Présent': Category('is', 'is', 'it', 'issons', 'issez', 'issent'),
      'Imparfait': Category('ais', 'ais', 'ait', 'ions', 'iez', 'aient'),
      'Passé simple': Category('is', 'is', 'it', 'îmes', 'îtes', 'irent'),
      'Futur': Category('ai', 'as', 'a', 'ons', 'ez', 'ont'),
      'Conditionnel': Category('ais', 'ais', 'ait', 'ions', 'iez', 'aient'),
      'Présent subjonctif': Category('e', 'es', 'e', 'ions', 'iez', 'ent'),
      'Imparfait subjonctif': Category('isse', 'isses', 'ît',
                                       'issions', 'issiez', 'issent')
  },
     're':
     {'Présent': Category('s', 's', '', 'ons', 'ez', 'ent'),
      'Imparfait': Category('ais', 'ais', 'ait', 'ions', 'iez', 'aient'),
      'Passé simple': Category('is', 'is', 'it', 'îmes', 'îtes', 'irent'),
      'Futur': Category('ai', 'as', 'a', 'ons', 'ez', 'ont'),
      'Conditionnel': Category('ais', 'ais', 'ait', 'ions', 'iez', 'aient'),
      'Présent subjonctif': Category('e', 'es', 'e', 'ions', 'iez', 'ent'),
      'Imparfait subjonctif': Category('isse', 'isses', 'ît',
                                       'issions', 'issiez', 'issent')
  }
}


def imparfait_subjonctif(infinitive):
    '''
    Creates the appropriate stem from the passé simple case
    '''

    stem = construct_inflection(infinitive, 'Passé simple').tps
    return stem[:-1]


def construct_stem_and_ending(infinitive, tense):
    '''
    Given an infinitive and a tense, looks up the appropriate
    transformation rules and concatenates the resultant stem and
    ending
    '''
    stem = _STEM_RULES[tense](infinitive)
    endings = _ENDINGS[infinitive[-2:]][tense]
    return Category._make([stem + end for end in endings])


def construct_inflection(infinitive, tense):
    '''
    Given an infinitive and tense, constructs the combined
    stem and ending, and then prepends the appropriate pronoun
    '''
    stem_and_ending = construct_stem_and_ending(infinitive, tense)
    return Category._make([(f(c), c) for f, c in zip(_PRONOUNS,
                                                     stem_and_ending)])


def print_normal_view(infinitive, tense, result):
    '''
    Pretty-printing for the traditional two-column output
    of a verb conjugation
    '''
    print('\n{}, {}:'.format(infinitive, tense))
    print('⎯'*45)
    print('{:<25}‖ {}'.format(result.fps, result.fpp))
    print('{:<25}‖ {}'.format(result.sps, result.spp))
    print('{:<25}‖ {}'.format(result.tps, result.tpp))
    print()


def output_cloze(infinitive, tense):
    '''
    Combines the different parts of a verb conjugation with
    Anki's required formatting to produce a form suitable
    for a cloze-deletion card
    '''
    conj = construct_inflection(infinitive, tense)
    result = []
    # TODO - make this pythonic, it's an ugly hack as it is
    for i, item in enumerate(conj):
        if i == 0 and infinitive[0] in _VOWELS:
            result.append(_FPS_FORMAT.format(item[0], item[1],
                                             infinitive, tense))
        else:
            result.append(_STD_FORMAT.format(item[0], item[1],
                                             infinitive, tense))
    return Category._make(result)


def output_cloze_import(infinitive, tense, translation, sound):
    '''
    Combines the output of the output_cloze function with optional
    translation and sound fields and combines them to produce the
    format required for Anki's import function
    '''
    cloze = output_cloze(infinitive, tense)
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
