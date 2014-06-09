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

    def test_present(self):
        expected = [['parle', 'parles', 'parle',
                     'parlons', 'parlez', 'parlent'],
                    ['finis', 'finis', 'finit',
                     'finissons', 'finissez', 'finissent'],
                    ['vends', 'vends', 'vend',
                     'vendons', 'vendez', 'vendent']]

        self.run_sub_tests(expected, 'présent')

    def test_imperfect(self):
        expected = [['parlais', 'parlais', 'parlait',
                     'parlions', 'parliez', 'parlaient'],
                    ['finissais', 'finissais', 'finissait',
                     'finissions', 'finissiez', 'finissaient'],
                    ['vendais', 'vendais', 'vendait',
                     'vendions', 'vendiez', 'vendaient']]

        self.run_sub_tests(expected, 'imparfait')

    def test_passé_simple(self):
        expected = [['parlai', 'parlas', 'parla',
                     'parlâmes', 'parlâtes', 'parlèrent'],
                    ['finis', 'finis', 'finit',
                     'finîmes', 'finîtes', 'finirent'],
                    ['vendis', 'vendis', 'vendit',
                     'vendîmes', 'vendîtes', 'vendirent']]

        self.run_sub_tests(expected, 'passé simple')

    def test_future(self):
        expected = [['parlerai', 'parleras', 'parlera',
                     'parlerons', 'parlerez', 'parleront'],
                    ['finirai', 'finiras', 'finira',
                     'finirons', 'finirez', 'finiront'],
                    ['vendrai', 'vendras', 'vendra',
                     'vendrons', 'vendrez', 'vendront']]

        self.run_sub_tests(expected, 'futur')

    def test_conditional(self):
        expected = [['parlerais', 'parlerais', 'parlerait',
                     'parlerions', 'parleriez', 'parleraient'],
                    ['finirais', 'finirais', 'finirait',
                     'finirions', 'finiriez', 'finiraient'],
                    ['vendrais', 'vendrais', 'vendrait',
                     'vendrions', 'vendriez', 'vendraient']]

        self.run_sub_tests(expected, 'conditionnel')

    def test_present_subjunctive(self):
        expected = [['parle', 'parles', 'parle',
                     'parlions', 'parliez', 'parlent'],
                    ['finisse', 'finisses', 'finisse',
                     'finissions', 'finissiez', 'finissent'],
                    ['vende', 'vendes', 'vende',
                     'vendions', 'vendiez', 'vendent']]

        self.run_sub_tests(expected, 'présent subjonctif')

    def test_imperfect_subjunctive(self):
        expected = [['parlasse', 'parlasses', 'parlât',
                     'parlassions', 'parlassiez', 'parlassent'],
                    ['finisse', 'finisses', 'finît',
                     'finissions', 'finissiez', 'finissent'],
                    ['vendisse', 'vendisses', 'vendît',
                     'vendissions', 'vendissiez', 'vendissent']]

        self.run_sub_tests(expected, 'imparfait subjonctif')

    def run_sub_tests(self, expected, tense):
        conj = partial(French.construct_stem_and_ending, tense=tense)
        for i, verb in enumerate(TestFrenchConjugator.test_verbs):
            with self.subTest(verb=verb):
                [self.assertEqual(expect, actual) for expect, actual in
                 zip(expected[i], conj(verb))]


class TestConjugatorVerbsThatStartWithVowel(unittest.TestCase):
    def test_verb_starts_with_a(self):
        conj = French.construct_inflection('abandonner', 'présent').fps
        pronoun, verb = conj
        self.assertEqual("j'abandonne", '{0}{1}'.format(pronoun, verb))

class TestClozeDeletionOutputRules(unittest.TestCase):

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

class TestOutputViews(unittest.TestCase):
    def test_normal_view(self):
        expected =\
['parler, présent:',
'⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯',
'je parle                 ‖ nous parlons',
'tu parles                ‖ vous parlez',
'il/elle/on parle         ‖ ils/elles parlent'
]

        conj = French.construct_inflection('parler', 'présent')
        actual = French.output_normal_view('parler', 'présent', conj)
        self.assertEqual(expected, actual)

    def test_normal_view(self):
        expected =\
['abandonner, présent:',
'⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯',
"j'abandonne              ‖ nous abandonnons",
'tu abandonnes            ‖ vous abandonnez',
'il/elle/on abandonne     ‖ ils/elles abandonnent'
]

        conj = French.construct_inflection('abandonner', 'présent')
        actual = French.output_normal_view('abandonner', 'présent', conj)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
