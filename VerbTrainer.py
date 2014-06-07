import languages.french as French
import languages.spanish as Spanish


def main():

    print("Welcome to Verb Trainer!")

    language_choice = {'1': 'Spanish',
                       '2': 'French'
                       }

    task_choice = {'1': conjugate_verb,
                   '2': goodbye}

    language = language_choice[input('Choose a language: 1) castellano 2) français\n'
                                     "Type '1' or '2', then press 'Enter' > ")]

    while True:

        task = task_choice[input('What would you like to do?\n'
                                 '1) conjugate a verb\n'
                                 '2) Quit\n'
                                 "Type '1' or '2' then press 'Enter' > ")]

        task(language)


def do_spanish():
    tense_choice =\
        {'1': 'presente',
         '2': 'pretérito imperfecto',
         '3': 'futuro simple',
         '4': 'pretérito indefinido'}

    while (True):
        infinitive = input('Infinitive? > ')
        tense =\
            tense_choice[input('1) presente\n'
                               '2) pretérito imperfecto\n'
                               '3) futuro simple\n'
                               '4) pretérito indefinado\n'
                               '5) Conditionnel\n'
                               '> ')]

        conj = Spanish.construct_inflection(infinitive, tense)

        output =\
            input('1) Print to screen\n'
                  '2) Print basic cloze deletion Anki format to file\n'
                  '3) print cloze deletion format with translation and sound to file\n'
                  '> ')
        if output == '1':
            print('\n'.join(Spanish.output_normal_view(infinitive, tense, conj)))
        elif output == '2':
            with open('cloze.txt', 'w') as f:
                output = Spanish.output_cloze(infinitive, tense, conj)
                f.write('\n'.join(output))

            print("File 'cloze.txt' written to current directory.")

        elif output == '3':      # TODO: add support for user-supplied translation and sound files
            with open('cloze_extra.txt', 'w') as f:
                output = Spanish.output_cloze_import(infinitive, tense,
                                                    [], [], conj)
                f.write('\n'.join(output))
            print("File 'cloze_extra.txt' written to current directory")

        quit = input('Continue? (y/n) > ')
        if quit.lower() == 'n':
            break

def do_french():
    tense_choice =\
        {'1': 'Présent',
         '2': 'Imparfait',
         '3': 'Passé simple',
         '4': 'Futur',
         '5': 'Conditionnel'}

    while (True):
            infinitive = input('Infinitive? > ')
            tense =\
                tense_choice[input('1) Présent 2) Imparfait 3) Passé simple\n'
                                   '4) Futur 5) Conditionnel\n'
                                   '> ')]

            conj = French.construct_inflection(infinitive, tense)

            output =\
                input('1) Print to screen\n'
                      '2) Print basic cloze deletion Anki format to file\n'
                      '3) print cloze deletion format with translation and sound to file\n'
                      '> ')

            if output == '1':
                print('\n'.join(French.output_normal_view(infinitive, tense, conj)))
            elif output == '2':
                with open('cloze.txt', 'w') as f:
                    output = French.output_cloze(infinitive, tense, conj)
                    f.write('\n'.join(output))

                print("File 'cloze.txt' written to current directory.")

            elif output == '3':      # TODO: add support for user-supplied translation and sound files
                with open('cloze_extra.txt', 'w') as f:
                    output = French.output_cloze_import(infinitive, tense,
                                                        [], [], conj)
                    f.write('\n'.join(output))
                print("File 'cloze_extra.txt' written to current directory")

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
