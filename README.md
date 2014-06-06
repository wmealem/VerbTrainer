Verb Trainer is a tool for practice conjugating French and Spanish, and eventually German and Japanese verb tenses. Its original purpose was to streamline the creation of notes for the Anki (http://ankisrs.net/) spaced-repetition software, but as I started creating it I realized it would also be useful for creating drills and exercises not specifically tied to Anki. This initial version handles the simple tenses for regular verbs for Spanish and French. Compound tenses, irregular verbs, and stem- and spelling-changing verbs are not yet handled. Current development is focusing on exporting the conjugations to an Anki-compatible import format.

A discussion of the original approach is located at http://wp.me/p41P0x-26

Invocation:
        python3 VerbTrainer.py

Future plans include:
- add support for compound tenses
- add support for bulk import of verb lists for conversion to Anki import format
- add support for irregular verbs, etc.
- develop Python ncurses front-end
- add integration with libraries of public domain sound files (Project Shtooka, etc.)
- convert to an add-in for Anki and eliminate the need for an import file
- add Japanese support
- put all prompts into resource files so that different languages may be supported
