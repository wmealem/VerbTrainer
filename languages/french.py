# Name:    french.py
# Author:  Michael Ealem
# Purpose: conjugate french verb tenses

from category import Category
from collections import namedtuple
import sqlite3

# French pronouns - easy way to handle the j'/je problem
# when the first letter of the verb is a vowel
# TODO: handle the case of the unaspirated h

_PRONOUNS = Category((lambda verb: "j'" if verb[0]
                      in _VOWELS else 'je'),
                     (lambda verb: 'tu'),
                     (lambda verb: 'il/elle/on'),
                     (lambda verb: 'nous'),
                     (lambda verb: 'vous'),
                     (lambda verb: 'ils/elles'))

_FPS_FORMAT = '{}{}'
_STD_FORMAT = '{} {}'
_FPS_CLOZE_FORMAT = '{0}{{{{c1::{1}::{2}, {3}}}}}'
_STD_CLOZE_FORMAT = '{0} {{{{c1::{1}::{2}, {3}}}}}'
_VOWELS = ('a', 'e', 'i', 'o', 'u')

SimpleTenseParts = namedtuple("SimpleTenseParts", 'pronoun verb')
CompoundTenseParts = namedtuple('CompoundTenseParts', 'pronoun aux past_participle')

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


_SIMPLE_TENSES = ['présent',
                  'passé simple',
                  'imparfait',
                  'futur',
                  'conditionnel']

# Logic for handling the different stem changes of regular verbs
_STEM_RULES =\
{'présent': (lambda x: x[:-2]),
 'futur': (lambda x: x[:-1] if x[-2:] == 're' else x),
 'imparfait': imparfait,
 'passé simple': (lambda x: x[:-2]),
 'conditionnel': (lambda x: x[:-1] if x[-2:] == 're' else x),
 'subjonctif présent': présent_subjonctif,
 'subjonctif imparfait': (lambda x: x[:-2])}


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
    with sqlite3.connect('verb_trainer.db') as con:
        cur = con.cursor()
        cur.execute("SELECT fps, sps, tps, fpp, spp, tpp FROM tense_endings"
                    "WHERE verb_type = ? AND tense_id = "
                    "(SELECT tense_id FROM tenses WHERE tense_name = ?)",
                    (verb_type, tense))

        endings = cur.fetchone()
    return Category._make([stem + end for end in endings])


def construct_simple_tense(infinitive, tense):
    stem_and_ending = construct_stem_and_ending(infinitive, tense)
    inflection = [(f(c), c) for f, c in zip(_PRONOUNS, stem_and_ending)]
    return Category._make([SimpleTenseParts._make(inf) for inf in inflection])


def construct_simple_tense_output(inflection):
    output = []
    if inflection.fps.verb[0] in _VOWELS:
        output.append(_FPS_FORMAT.format(inflection.fps.pronoun,
                                         inflection.fps.verb))
    else:
        output.append(_STD_FORMAT.format(inflection.fps.pronoun,
                                         inflection.fps.verb))
    output.append(_STD_FORMAT.format(inflection.sps.pronoun,
                                     inflection.sps.verb))
    output.append(_STD_FORMAT.format(inflection.tps.pronoun,
                                     inflection.tps.verb))
    output.append(_STD_FORMAT.format(inflection.fpp.pronoun,
                                     inflection.fpp.verb))
    output.append(_STD_FORMAT.format(inflection.spp.pronoun,
                                     inflection.spp.verb))
    output.append(_STD_FORMAT.format(inflection.tpp.pronoun,
                                     inflection.tpp.verb))

    return Category._make(output)



def construct_simple_tense_subjunctive(infinitive, tense):
    stem_and_ending = construct_stem_and_ending(infinitive, tense)
    return Category._make([("qu'" if f(c)[0] in _VOWELS else 'que', f(c), c)
                           for f, c in zip(_PRONOUNS, stem_and_ending)])


def construct_compound_tense(infinitive, tense):
    past_participle = _construct_past_participle(infinitive)
    inflection = [(f(aux), aux, past_participle)
                  for f, aux in zip(_PRONOUNS,
                                    _COMPOUND_TENSE[tense])]
    return Category._make(inflection)


def construct_compound_tense_subjunctive(infinitive, tense):
    past_participle = _construct_past_participle(infinitive)
    inflection = [("qu'" if f(aux)[0] in _VOWELS else 'que',
                   f(aux), aux, past_participle)
                  for f, aux in zip(_PRONOUNS,
                                    _COMPOUND_TENSE[tense])]
    return Category._make(inflection)


def construct_inflection(infinitive, tense):
    '''
    Given an infinitive and tense, constructs the combined
    stem and ending, and then prepends the appropriate pronoun
    '''
    if tense in ['subjonctif présent',
                 'subjonctif imparfait']:
        return construct_simple_tense_subjunctive(infinitive, tense)

    elif tense in ['subjonctif passé', 'subjonctif plus-que-parfait']:
        return construct_compound_tense_subjunctive(infinitive, tense)

    elif tense in ['passé composé',
                   'plus-que-parfait',
                   'futur antérieur',
                   'passé antérieur',
                   'passé du conditionnel']:
        return construct_compound_tense(infinitive, tense)
    else:
        return construct_simple_tense(infinitive, tense)


def elision(word1, word2):
    if word1 not in ['je', 'que']:
        raise ValueError("First parameter must be 'je' or 'que'")
    if word2[0] in _VOWELS:
        return word1[:-1] + word2
    return word1 + ' ' + word2


def output_normal_view(infinitive, tense, inflection):
    print(infinitive + ', ' + tense)
    print('─' * 50)
    if tense in _SIMPLE_TENSES:
        out = construct_simple_tense_output(inflection)
        print('{:<25}║  {}'.format(out.fps, out.fpp))
        print('{:<25}║  {}'.format(out.sps, out.spp))
        print('{:<25}║  {}'.format(out.tps, out.tpp))


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

AUX_VERB = {'avoir': {'présent': ['ai', 'as', 'a',
                                  'avons', 'avez', 'ont'],
                      'imparfait': ['avais', 'avais', 'avait',
                                    'avions', 'aviez', 'avaient'],
                      'passé simple': ['eus', 'eus', 'eut',
                                       'eûmes', 'eûtes', 'eurent'],
                      'futur': ['aurai', 'auras', 'aura',
                                'aurons', 'aurez', 'auront'],
                      'conditionnel': ['aurais', 'aurais', 'aurait',
                                       'aurions', 'auriez', 'auraient'],
                      'subjonctif présent': ['aie', 'aies', 'ait',
                                             'ayons', 'ayez', 'aient'],
                      'subjonctif imparfait': ['eusse', 'eusses', 'eût',
                                               'eussions', 'eussiez', 'eussent']},
            'être': {'présent': ['suis', 'es', 'est',
                                 'sommes', 'êtes', 'sont'],
                     'imparfait': ['étais', 'étais', 'était',
                                   'étions', 'étiez', 'étaient'],
                     'passé simple': ['fus', 'fus', 'fut',
                                      'fûmes', 'fûtes', 'furent'],
                     'futur': ['serai', 'seras', 'sera',
                               'serons', 'serez', 'seront'],
                     'conditionnel': ['serais', 'serais', 'serait',
                                      'serions', 'seriez', 'seraient'],
                     'subjonctif présent': ['sois', 'sois', 'soit',
                                            'soyons', 'soyez', 'soient'],
                     'subjonctif imparfait': ['fusse', 'fusses', 'fût',
                                              'fussions', 'fussiez', 'fussent']}}

_COMPOUND_TENSE = {'passé composé': AUX_VERB['avoir']['présent'],
                   'plus-que-parfait': AUX_VERB['avoir']['imparfait'],
                   'passé antérieur': AUX_VERB['avoir']['passé simple'],
                   'futur antérieur': AUX_VERB['avoir']['futur'],
                   'passé du conditionnel': AUX_VERB['avoir']['conditionnel'],
                   'subjonctif passé': AUX_VERB['avoir']['subjonctif présent'],
                   'subjonctif plus-que-parfait': AUX_VERB['avoir']['subjonctif imparfait']}

def _construct_past_participle(infinitive):
    '''
    Given an infinitive, returns the past participle for
    the given verb
    '''
    ending = infinitive[-2:]
    stem = infinitive[:-2]
    if ending == 'er':
        return stem + 'é'
    elif ending == 'ir':
        return stem + 'i'
    elif ending == 're':
        return stem + 'u'
    else:
        raise ValueError('parameter not a verb infinitive')
