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

    def test_present_with_pronouns(self):
        expected = [['yo hablo',
                     'tú hablas', 'vos hablás',
                     'él/ella/usted habla',
                     'nosotros/nosotras hablamos',
                     'vosotros/vosotras habláis',
                     'ellos/ellas/ustedes hablan'],

                    ['yo vendo',
                     'tú vendes', 'vos vendés',
                     'él/ella/usted vende',
                     'nosotros/nosotras vendemos',
                     'vosotros/vosotras vendéis',
                     'ellos/ellas/ustedes venden'],

                    ['yo vivo',
                     'tú vives', 'vos vivís',
                     'él/ella/usted vive',
                     'nosotros/nosotras vivimos',
                     'vosotros/vosotras vivís',
                     'ellos/ellas/ustedes viven']]

        with self.subTest():
            for i, verb in enumerate(TestSpanishConjugator.test_verbs):
                conj = Spanish.construct_inflection(verb, 'presente')
                actual = [Spanish._STD_FORMAT.format(*item) for item in conj]
                self.assertEqual(expected[i], actual)

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

    def test_present_perfect(self):
        expected = [['he hablado', 'has hablado', 'has hablado', 'ha hablado',
                     'hemos hablado', 'habéis hablado', 'han hablado'],
                    ['he vendido', 'has vendido', 'has vendido', 'ha vendido',
                     'hemos vendido', 'habéis vendido', 'han vendido'],
                    ['he vivido', 'has vivido', 'has vivido', 'ha vivido',
                     'hemos vivido', 'habéis vivido', 'han vivido']]

        self.run_sub_tests(expected, 'pretérito perfecto')


class TestcompoundTenses(unittest.TestCase):
        def test_past_participle(self):
            expected = ['hablado', 'vendido', 'vivido']
            actual = [Spanish._construct_past_participle('hablar'),
                      Spanish._construct_past_participle('vender'),
                      Spanish._construct_past_participle('vivir')]
            self.assertEqual(expected, actual
)
