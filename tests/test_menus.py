import unittest
import languages.spanish as es
import languages.french as fr


class TestMenus(unittest.TestCase):
    def test_spanish_tense_menu_one(self):
        expected = 'presente'
        actual = es.construct_tense_menu(1)
        self.assertEqual(expected, actual['1'])

    def test_spanish_tense_menu_five(self):
        expected = ['presente',
                    'pretérito imperfecto',
                    'pretérito indefinido',
                    'futuro simple',
                    'pretérito perfecto']
        actual = es.construct_tense_menu(5)
        self.assertEqual(expected, list(actual.values()))

    def test_spanish_tense_menu_all(self):
        expected = es._TENSES
        actual = es.construct_tense_menu()
        self.assertEqual(expected, list(actual.values()))
