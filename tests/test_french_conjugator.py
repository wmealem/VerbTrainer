# Unit Tests for French conjugation
# Author: Michael Ealem

import unittest
import languages.french as French
from functools import partial
from category import Category


class TestFrenchConjugator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_verbs = ['parler', 'finir', 'vendre']

    def test_present_endings(self):
        expected = [['parle', 'parles', 'parle',
                     'parlons', 'parlez', 'parlent'],
                    ['finis', 'finis', 'finit',
                     'finissons', 'finissez', 'finissent'],
                    ['vends', 'vends', 'vend',
                     'vendons', 'vendez', 'vendent']]

        self.run_sub_tests(expected,
                           'présent',
                           French.construct_stem_and_ending)

    def test_imperfect_endings(self):
        expected = [['parlais', 'parlais', 'parlait',
                     'parlions', 'parliez', 'parlaient'],
                    ['finissais', 'finissais', 'finissait',
                     'finissions', 'finissiez', 'finissaient'],
                    ['vendais', 'vendais', 'vendait',
                     'vendions', 'vendiez', 'vendaient']]

        self.run_sub_tests(expected,
                           'imparfait',
                           French.construct_stem_and_ending)

    def test_passé_simple_endings(self):
        expected = [['parlai', 'parlas', 'parla',
                     'parlâmes', 'parlâtes', 'parlèrent'],
                    ['finis', 'finis', 'finit',
                     'finîmes', 'finîtes', 'finirent'],
                    ['vendis', 'vendis', 'vendit',
                     'vendîmes', 'vendîtes', 'vendirent']]

        self.run_sub_tests(expected,
                           'passé simple',
                           French.construct_stem_and_ending)

    def test_future_endings(self):
        expected = [['parlerai', 'parleras', 'parlera',
                     'parlerons', 'parlerez', 'parleront'],
                    ['finirai', 'finiras', 'finira',
                     'finirons', 'finirez', 'finiront'],
                    ['vendrai', 'vendras', 'vendra',
                     'vendrons', 'vendrez', 'vendront']]

        self.run_sub_tests(expected,
                           'futur',
                           French.construct_stem_and_ending)

    def test_conditional_endings(self):
        expected = [['parlerais', 'parlerais', 'parlerait',
                     'parlerions', 'parleriez', 'parleraient'],
                    ['finirais', 'finirais', 'finirait',
                     'finirions', 'finiriez', 'finiraient'],
                    ['vendrais', 'vendrais', 'vendrait',
                     'vendrions', 'vendriez', 'vendraient']]

        self.run_sub_tests(expected,
                           'conditionnel',
                           French.construct_stem_and_ending)

    def test_present_subjunctive_endings(self):
        expected = [['parle', 'parles', 'parle',
                     'parlions', 'parliez', 'parlent'],
                    ['finisse', 'finisses', 'finisse',
                     'finissions', 'finissiez', 'finissent'],
                    ['vende', 'vendes', 'vende',
                     'vendions', 'vendiez', 'vendent']]

        self.run_sub_tests(expected,
                           'subjonctif présent',
                           French.construct_stem_and_ending)

    def test_imperfect_subjunctive_endings(self):
        expected = [['parlasse', 'parlasses', 'parlât',
                     'parlassions', 'parlassiez', 'parlassent'],
                    ['finisse', 'finisses', 'finît',
                     'finissions', 'finissiez', 'finissent'],
                    ['vendisse', 'vendisses', 'vendît',
                     'vendissions', 'vendissiez', 'vendissent']]

        self.run_sub_tests(expected,
                           'subjonctif imparfait',
                           French.construct_stem_and_ending)

    def test_present_subjonctif_with_conjunction(self):
        expected = [[('que', 'je', 'parle'),
                     ('que', 'tu', 'parles'),
                     ("qu'", 'il/elle/on', 'parle'),
                     ('que', 'nous', 'parlions'),
                     ('que', 'vous', 'parliez'),
                     ("qu'", 'ils/elles', 'parlent')],
                    [('que', 'je', 'finisse'),
                     ('que', 'tu', 'finisses'),
                     ("qu'", 'il/elle/on', 'finisse'),
                     ('que', 'nous', 'finissions'),
                     ('que', 'vous', 'finissiez'),
                     ("qu'", 'ils/elles', 'finissent')],
                    [('que', 'je', 'vende'),
                     ('que', 'tu', 'vendes'),
                     ("qu'", 'il/elle/on', 'vende'),
                     ('que', 'nous', 'vendions'),
                     ('que', 'vous', 'vendiez'),
                     ("qu'", 'ils/elles', 'vendent')]]

        self.run_sub_tests(expected,
                           'subjonctif présent',
                           French.construct_inflection)

    def test_imperfect_subjunctive_with_conjunction(self):
        expected = [[('que', 'je', 'parlasse'),
                     ('que', 'tu', 'parlasses'),
                     ("qu'", 'il/elle/on', 'parlât'),
                     ('que', 'nous', 'parlassions'),
                     ('que', 'vous', 'parlassiez'),
                     ("qu'", 'ils/elles', 'parlassent')],
                    [('que', 'je', 'finisse'),
                     ('que', 'tu', 'finisses'),
                     ("qu'", 'il/elle/on', 'finît'),
                     ('que', 'nous', 'finissions'),
                     ('que', 'vous', 'finissiez'),
                     ("qu'", 'ils/elles', 'finissent')],
                    [('que', 'je', 'vendisse'),
                     ('que', 'tu', 'vendisses'),
                     ("qu'", 'il/elle/on', 'vendît'),
                     ('que', 'nous', 'vendissions'),
                     ('que', 'vous', 'vendissiez'),
                     ("qu'", 'ils/elles', 'vendissent')]]

        self.run_sub_tests(expected,
                           'subjonctif imparfait',
                           French.construct_inflection)

    def test_passé_composé(self):
        expected = [[("j'", 'ai', 'parlé'),
                     ('tu', 'as', 'parlé'),
                     ('il/elle/on', 'a', 'parlé'),
                     ('nous', 'avons', 'parlé'),
                     ('vous', 'avez', 'parlé'),
                     ('ils/elles', 'ont', 'parlé')],
                    [("j'", 'ai', 'fini'),
                     ('tu', 'as', 'fini'),
                     ('il/elle/on', 'a', 'fini'),
                     ('nous', 'avons', 'fini'),
                     ('vous', 'avez', 'fini'),
                     ('ils/elles', 'ont', 'fini')],
                    [("j'", 'ai', 'vendu'),
                     ('tu', 'as', 'vendu'),
                     ('il/elle/on', 'a', 'vendu'),
                     ('nous', 'avons', 'vendu'),
                     ('vous', 'avez', 'vendu'),
                     ('ils/elles', 'ont', 'vendu')]
]
        self.run_sub_tests(expected,
                           'passé composé',
                           French.construct_inflection)


    def test_pluperfect(self):
        expected = [[("j'", 'avais', 'parlé'),
                     ('tu', 'avais', 'parlé'),
                     ('il/elle/on', 'avait', 'parlé'),
                     ('nous', 'avions', 'parlé'),
                     ('vous', 'aviez', 'parlé'),
                     ('ils/elles', 'avaient', 'parlé')],
                    [("j'", 'avais', 'fini'),
                     ('tu', 'avais', 'fini'),
                     ('il/elle/on', 'avait', 'fini'),
                     ('nous', 'avions', 'fini'),
                     ('vous', 'aviez', 'fini'),
                     ('ils/elles', 'avaient', 'fini')],
                    [("j'", 'avais', 'vendu'),
                     ('tu', 'avais', 'vendu'),
                     ('il/elle/on', 'avait', 'vendu'),
                     ('nous', 'avions', 'vendu'),
                     ('vous', 'aviez', 'vendu'),
                     ('ils/elles', 'avaient', 'vendu')]
]
        self.run_sub_tests(expected,
                           'plus-que-parfait',
                           French.construct_inflection)

    def test_past_anterior(self):
        expected = [[("j'", 'eus', 'parlé'),
                     ('tu', 'eus', 'parlé'),
                     ('il/elle/on', 'eut', 'parlé'),
                     ('nous', 'eûmes', 'parlé' ),
                     ('vous', 'eûtes', 'parlé'),
                     ('ils/elles', 'eurent', 'parlé')],
                    [("j'", 'eus', 'fini'),
                     ('tu', 'eus', 'fini'),
                     ('il/elle/on', 'eut', 'fini'),
                     ('nous', 'eûmes', 'fini' ),
                     ('vous', 'eûtes', 'fini'),
                     ('ils/elles', 'eurent', 'fini')],
                    [("j'", 'eus', 'vendu'),
                     ('tu', 'eus', 'vendu'),
                     ('il/elle/on', 'eut', 'vendu'),
                     ('nous', 'eûmes', 'vendu' ),
                     ('vous', 'eûtes', 'vendu'),
                     ('ils/elles', 'eurent', 'vendu')]]

        self.run_sub_tests(expected,
                           'passé antérieur',
                           French.construct_inflection)

    def test_futur_anterior(self):
        expected = [[("j'", 'aurai', 'parlé'),
                     ('tu', 'auras', 'parlé'),
                     ('il/elle/on', 'aura', 'parlé'),
                     ('nous', 'aurons', 'parlé' ),
                     ('vous', 'aurez', 'parlé'),
                     ('ils/elles', 'auront', 'parlé')],
                    [("j'", 'aurai', 'fini'),
                     ('tu', 'auras', 'fini'),
                     ('il/elle/on', 'aura', 'fini'),
                     ('nous', 'aurons', 'fini' ),
                     ('vous', 'aurez', 'fini'),
                     ('ils/elles', 'auront', 'fini')],
                    [("j'", 'aurai', 'vendu'),
                     ('tu', 'auras', 'vendu'),
                     ('il/elle/on', 'aura', 'vendu'),
                     ('nous', 'aurons', 'vendu' ),
                     ('vous', 'aurez', 'vendu'),
                     ('ils/elles', 'auront', 'vendu')]]

        self.run_sub_tests(expected,
                           'futur antérieur',
                           French.construct_inflection)

    def test_past_conditional(self):
        expected = [[("j'", 'aurais', 'parlé'),
                     ('tu', 'aurais', 'parlé'),
                     ('il/elle/on', 'aurait', 'parlé'),
                     ('nous', 'aurions', 'parlé' ),
                     ('vous', 'auriez', 'parlé'),
                     ('ils/elles', 'auraient', 'parlé')],
                    [("j'", 'aurais', 'fini'),
                     ('tu', 'aurais', 'fini'),
                     ('il/elle/on', 'aurait', 'fini'),
                     ('nous', 'aurions', 'fini' ),
                     ('vous', 'auriez', 'fini'),
                     ('ils/elles', 'auraient', 'fini')],
                    [("j'", 'aurais', 'vendu'),
                     ('tu', 'aurais', 'vendu'),
                     ('il/elle/on', 'aurait', 'vendu'),
                     ('nous', 'aurions', 'vendu' ),
                     ('vous', 'auriez', 'vendu'),
                     ('ils/elles', 'auraient', 'vendu')]]

        self.run_sub_tests(expected,
                          'passé du conditionnel',
                          French.construct_inflection)

    def test_past_subjonctif_with_conjunction(self):
        expected = [[('que', "j'", 'aie', 'parlé'),
                     ('que', 'tu', 'aies', 'parlé'),
                     ("qu'", 'il/elle/on', 'ait', 'parlé'),
                     ('que', 'nous', 'ayons', 'parlé'),
                     ('que', 'vous', 'ayez', 'parlé'),
                     ("qu'", 'ils/elles', 'aient', 'parlé')],
                    [('que', "j'", 'aie', 'fini'),
                     ('que', 'tu', 'aies', 'fini'),
                     ("qu'", 'il/elle/on', 'ait', 'fini'),
                     ('que', 'nous', 'ayons', 'fini'),
                     ('que', 'vous', 'ayez', 'fini'),
                     ("qu'", 'ils/elles', 'aient', 'fini')],
                    [('que', "j'", 'aie', 'vendu'),
                     ('que', 'tu', 'aies', 'vendu'),
                     ("qu'", 'il/elle/on', 'ait', 'vendu'),
                     ('que', 'nous', 'ayons', 'vendu'),
                     ('que', 'vous', 'ayez', 'vendu'),
                     ("qu'", 'ils/elles', 'aient', 'vendu')]]

        self.run_sub_tests(expected,
                           'subjonctif passé',
                           French.construct_inflection)

    def test_pluperfect_subjonctif_with_conjunction(self):
        expected = [[('que', "j'", 'eusse', 'parlé'),
                     ('que', 'tu', 'eusses', 'parlé'),
                     ("qu'", 'il/elle/on', 'eût', 'parlé'),
                     ('que', 'nous', 'eussions', 'parlé'),
                     ('que', 'vous', 'eussiez', 'parlé'),
                     ("qu'", 'ils/elles', 'eussent', 'parlé')],
                    [('que', "j'", 'eusse', 'fini'),
                     ('que', 'tu', 'eusses', 'fini'),
                     ("qu'", 'il/elle/on', 'eût', 'fini'),
                     ('que', 'nous', 'eussions', 'fini'),
                     ('que', 'vous', 'eussiez', 'fini'),
                     ("qu'", 'ils/elles', 'eussent', 'fini')],
                    [('que', "j'", 'eusse', 'vendu'),
                     ('que', 'tu', 'eusses', 'vendu'),
                     ("qu'", 'il/elle/on', 'eût', 'vendu'),
                     ('que', 'nous', 'eussions', 'vendu'),
                     ('que', 'vous', 'eussiez', 'vendu'),
                     ("qu'", 'ils/elles', 'eussent', 'vendu')]]

        self.run_sub_tests(expected,
                           'subjonctif plus-que-parfait',
                           French.construct_inflection)

    def run_sub_tests(self, expected, tense, func_to_test):
        conj = partial(func_to_test, tense=tense)
        for i, verb in enumerate(TestFrenchConjugator.test_verbs):
            with self.subTest(verb=verb):
                [self.assertEqual(expect, actual) for expect, actual in
                 zip(expected[i], conj(verb))]

    def test_past_participle(self):
        expected = ['parlé', 'fini', 'vendu']
        actual = [French._construct_past_participle('parler'),
                  French._construct_past_participle('finir'),
                  French._construct_past_participle('vendre')]
        self.assertEqual(expected, actual)

    def test_verb_starts_with_a(self):
        inf = French.construct_inflection('abandonner', 'présent').fps
        pronoun, verb = inf
        self.assertEqual("j'abandonne", '{}{}'.format(pronoun, verb))




class TestClozeDeletionOutputRules(unittest.TestCase):
    @unittest.skip('move to output')
    def test_cloze_normal(self):
        expected = Category._make(['je {{c1::parle::parler, présent}}',
                    'tu {{c1::parles::parler, présent}}',
                    'il/elle/on {{c1::parle::parler, présent}}',
                    'nous {{c1::parlons::parler, présent}}',
                    'vous {{c1::parlez::parler, présent}}',
                    'ils/elles {{c1::parlent::parler, présent}}'])

        conj = French.construct_inflection('parler', 'présent')
        actual = French.output_cloze('parler', 'présent', conj)
        with self.subTest():
            self.assertEqual(expected.fps, actual.fps)
            self.assertEqual(expected.sps, actual.sps)
            self.assertEqual(expected.tps, actual.tps)
            self.assertEqual(expected.fpp, actual.fpp)
            self.assertEqual(expected.spp, actual.spp)
            self.assertEqual(expected.tpp, actual.tpp)

    @unittest.skip('move to output')
    def test_cloze_verb_begins_with_vowel(self):
        expected =\
            Category._make(["j'{{c1::abandonne::abandonner, présent}}",
                            'tu {{c1::abandonnes::abandonner, présent}}',
                            'il/elle/on {{c1::abandonne::abandonner, présent}}',
                            'nous {{c1::abandonnons::abandonner, présent}}',
                            'vous {{c1::abandonnez::abandonner, présent}}',
                            'ils/elles {{c1::abandonnent::abandonner, présent}}'])
        conj = French.construct_inflection('abandonner', 'présent')
        actual = French.output_cloze('abandonner', 'présent', conj)
        with self.subTest():
            self.assertEqual(expected.fps, actual.fps)
            self.assertEqual(expected.sps, actual.sps)
            self.assertEqual(expected.tps, actual.tps)
            self.assertEqual(expected.fpp, actual.fpp)
            self.assertEqual(expected.spp, actual.spp)
            self.assertEqual(expected.tpp, actual.tpp)

    @unittest.skip('move to output')
    def test_cloze_import(self):
        expected = Category._make(['je {{c1::parle::parler, présent}}|I speak|[sound:je parle.mp3]|parler',
                    'tu {{c1::parles::parler, présent}}|you speak|[sound:tu parles.mp3]|parler',
                    'il/elle/on {{c1::parle::parler, présent}}|he/she/it speaks|[sound:il parle.mp3]|parler',
                    'nous {{c1::parlons::parler, présent}}|we speak|[sound:nous parlons.mp3]|parler',
                    'vous {{c1::parlez::parler, présent}}|you speak|[sound:vous parlez.mp3]|parler',
                    'ils/elles {{c1::parlent::parler, présent}}|they speak|[sound:ils parlent.mp3]|parler'])

        translation = ['I speak', 'you speak', 'he/she/it speaks',
                       'we speak', 'you speak', 'they speak']

        sound = ['je parle.mp3', 'tu parles.mp3', 'il parle.mp3',
                 'nous parlons.mp3', 'vous parlez.mp3', 'ils parlent.mp3']

        conj = French.construct_inflection('parler', 'présent')
        actual = French.output_cloze_import('parler', 'présent',
                                            translation,
                                            sound,
                                            conj)

        with self.subTest():
            self.assertEqual(expected.fps, actual.fps)
            self.assertEqual(expected.sps, actual.sps)
            self.assertEqual(expected.tps, actual.tps)
            self.assertEqual(expected.fpp, actual.fpp)
            self.assertEqual(expected.spp, actual.spp)
            self.assertEqual(expected.tpp, actual.tpp)



if __name__ == '__main__':
    unittest.main()
