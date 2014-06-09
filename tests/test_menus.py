import unittest
import VerbTrainer
import languages.spanish as es
import languages.french as fr


class TestMenus(unittest.TestCase):
    def test_tense_menu_one(self):
        expected = 'presente'
        actual = VerbTrainer.construct_tense_menu(es._TENSES,1)
        self.assertEqual(expected, actual['1'])

    def test_spanish_tense_menu_five(self):
        expected = ['presente',
                    'pretérito imperfecto',
                    'pretérito indefinido',
                    'futuro simple',
                    'pretérito perfecto']
        actual = VerbTrainer.construct_tense_menu(es._TENSES, 5)
        self.assertEqual(expected, list(actual.values()))

    def test_spanish_tense_menu_all(self):
        expected = es._TENSES
        actual = VerbTrainer.construct_tense_menu(es._TENSES)
        self.assertEqual(expected, list(actual.values()))
