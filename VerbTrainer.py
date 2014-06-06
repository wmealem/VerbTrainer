import languages.french as French
import languages.spanish as Spanish


def main():

    print("Welcome to Verb Trainer!")

    language_choice = {'1': 'Spanish',
                       '2': 'French'
                       }

    task_choice = {'1': conjugate_verb,
                   '2': write_import,
                   '3': goodbye}

    language = language_choice[input('Choose a language: 1) castellano 2) français\n'
                                     "Type '1' or '2', then press 'Enter' > ")]

    while True:

        task = task_choice[input('What would you like to do?\n'
                                 '1) conjugate a verb and display it to the screen\n'
                                 '2) conjugate a verb and export to a file for Anki import\n'
                                 '3) Quit\n'
                                 "Type '1', '2', or '3' then press 'Enter' > ")]

        task(language)






    #print("Choose a task: 1) Export to Anki-compatible import file\n > ")
    choice = {'1': 'Présent',
              '2': 'Imparfait',
              '3': 'Passé simple',
              '4': 'Futur',
              '5': 'Conditionnel'}

    with open('import.txt', 'w') as f:

        while (True):
            infinitive = input('Infinitive? > ')
            tense = choice[input('1) Présent 2) Imparfait 3) Passé simple\n'
                                 '4) Futur 5) Conditionnel > ')]

            conj = French.construct_inflection(infinitive, tense)
            rules = French._cloze_import_rules

            to_write = [func(c, infinitive, tense)
                        for func, c in zip(rules, conj)]
            [write_to_file(f, item) for item in to_write]

            print('{} of {} was written to file.'.format(tense, infinitive))

            quit = input('Continue? (y/n) > ')
            if quit.lower() == 'n':
                break

    print("File 'import.txt' written to current directory.")

def do_spanish():
    print('Doing Spanish')

def do_french():
    from category import Category
    choice = {'1': 'Présent',
              '2': 'Imparfait',
              '3': 'Passé simple',
              '4': 'Futur',
              '5': 'Conditionnel'}
    while (True):
            infinitive = input('Infinitive? > ')
            tense = choice[input('1) Présent 2) Imparfait 3) Passé simple\n'
                                 '4) Futur 5) Conditionnel > ')]

            conj = French.construct_inflection(infinitive, tense)

            print('\n'.join(French.output_normal_view(infinitive, tense, conj)))

            quit = input('Continue? (y/n) > ')
            if quit.lower() == 'n':
                break

def do_german():
    raise NotImplementedError

def do_japanese():
    raise NotImplementedError

def conjugate_verb(language):
    do_something = {'Spanish': do_spanish,
                    'French': do_french}

    do_something[language]()

def goodbye(language):
    msg = {'Spanish': 'Adiós',
           'French': 'Au revoir!'}
    print('Thanks for using Verb Trainer!')
    print(msg[language])
    exit()

def write_import():
    print('Writing import file...\n')

def write_to_file(f, conj):
    out = conj + '\n'
    f.write(out)


if __name__ == "__main__":
    main()
