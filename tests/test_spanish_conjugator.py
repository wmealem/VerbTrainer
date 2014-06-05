# Unit tests for Spanish verb conjugation
import unittest
import languages.spanish as Spanish
from functools import partial


class TestSpanishConjugator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_verbs = ['hablar', 'vender', 'vivir']

    def test_present(self):
        expected = [['hablo', 'hablas', 'hablás', 'habla',
                     'hablamos', 'habláis', 'hablan'],
                    ['vendo', 'vendes', 'vendés', 'vende',
                     'vendemos', 'vendéis', 'venden'],
                    ['vivo', 'vives', 'vivís', 'vive',
                     'vivimos', 'vivís', 'viven']]

        self.run_sub_tests(expected, 'presente')

    def test_imperfect(self):
        expected = [['hablaba', 'hablabas', 'hablabas', 'hablaba',
                     'hablábamos', 'hablabais', 'hablaban'],
                    ['vendía', 'vendías', 'vendías', 'vendía',
                     'vendíamos', 'vendíais', 'vendían'],
                    ['vivía', 'vivías', 'vivías', 'vivía',
                     'vivíamos', 'vivíais', 'vivían']]

        self.run_sub_tests(expected, 'pretérito imperfecto')

    def test_future(self):
        expected = [['hablaré', 'hablarás', 'hablarás', 'hablará',
                     'hablaremos', 'hablaréis', 'hablarán'],
                    ['venderé', 'venderás', 'venderás', 'venderá',
                     'venderemos', 'venderéis', 'venderán'],
                    ['viviré', 'vivirás', 'vivirás', 'vivirá',
                     'viviremos', 'viviréis', 'vivirán']]

        self.run_sub_tests(expected, 'futuro simple')

    def test_preterit(self):
        expected = [['hablé', 'hablaste(s)', 'hablaste(s)', 'habló',
                     'hablamos', 'hablasteis', 'hablaron'],
                    ['vendí', 'vendiste(s)', 'vendiste(s)', 'vendió',
                     'vendimos', 'vendisteis', 'vendieron'],
                    ['viví', 'viviste(s)', 'viviste(s)', 'vivió',
                     'vivimos', 'vivisteis', 'vivieron']
                    ]

        self.run_sub_tests(expected, 'pretérito indefinido')

    def run_sub_tests(self, expected, tense):
        conj = partial(Spanish.construct_stem_and_ending, tense=tense)
        for i, verb in enumerate(TestSpanishConjugator.test_verbs):
            with self.subTest(verb=verb, tense=tense):
                [self.assertEqual(expect, actual) for expect, actual in
                 zip(expected[i], conj(verb))]
