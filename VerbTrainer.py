#!/usr/bin/python3
import languages.french as French
import languages.spanish as Spanish
from collections import OrderedDict


def main():

    print("Welcome to Verb Trainer!")
    language = get_language_choice()

    while True:
        task_choice = get_task_choice()
        if task_choice == '1':
            conjugate_verb(language)
        else:
            break

    goodbye(language)

def conjugate_verb(language):
    tenses, conjugator, view, cloze, export = get_language_tools(language)

    tense_choice = construct_tense_menu(tenses, len(tenses))

    menu = '\n'.join(['{}) {}'.format(*item) for item in tense_choice.items()])

    while (True):
            infinitive = get_infinitive()
            tense = tense_choice[input('Tense?\n' + menu + '\n> ')]

            conj = conjugator(infinitive, tense)

            output = output_menu()

            if output == '1':
                view(infinitive, tense, conj)
            elif output == '2':
                with open('cloze.txt', 'w') as f:
                    output = cloze(infinitive, tense, conj)
                    f.write('\n'.join(output))

                print("File 'cloze.txt' written to current directory.")

            elif output == '3':      # TODO: add support for user-supplied translation and sound files
                with open('cloze_extra.txt', 'w') as f:
                    output = export(infinitive, tense, [], [], conj)
                    f.write('\n'.join(output))
                print("File 'cloze_extra.txt' written to current directory")

            quit = input('Continue? (y/n) > ')
            if quit.lower() == 'n':
                break


def get_language_tools(language):
    if language == 'French':
        tenses = French._TENSES
        conjugator = French.construct_inflection
        view = French.output_normal_view
        cloze = French.output_cloze
        export = French.output_cloze_import
    elif language == 'Spanish':
        tenses = Spanish._TENSES
        conjugator = Spanish.construct_inflection
        view = Spanish.output_normal_view
        cloze = Spanish.output_cloze
        export = Spanish.output_cloze_import
    else:
        raise NotImplementedError

    return tenses, conjugator, view, cloze, export


def goodbye(language):
    msg = {'Spanish': 'Adiós',
           'French': 'Au revoir!'}
    print('Thanks for using Verb Trainer!')
    print(msg[language])


def write_import():
    print('Writing import file...\n')


def write_to_file(f, conj):
    out = conj + '\n'
    f.write(out)


def output_menu():
    return input('1) Print to screen\n'
                 '2) Print basic cloze deletion Anki format to file\n'
                 '3) print cloze deletion format with translation and sound to file\n'
                 '> ')


def get_task_choice():
    return input('What would you like to do?\n'
                 '1) conjugate a verb\n'
                 '2) Quit\n'
                 "Type '1' or '2' then press 'Enter' > ")


def get_language_choice():
    language_choice = {'1': 'Spanish',
                       '2': 'French'
                       }

    return language_choice[input('Choose a language: 1) castellano 2) français\n'
                                     "Type '1' or '2', then press 'Enter' > ")]


def get_infinitive():
    return input('Infinitive? > ')


def construct_tense_menu(tenses, how_many=None):
    if not how_many:
        how_many = len(tenses)
    num = [str(i) for i in range(1, how_many+1)]
    return OrderedDict(zip(num, tenses))

if __name__ == "__main__":
    main()
