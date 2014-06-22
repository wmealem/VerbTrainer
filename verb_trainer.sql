PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS languages;
CREATE TABLE languages(language_id INTEGER PRIMARY KEY,
                       language_name TEXT NOT NULL);

INSERT INTO languages VALUES(NULL, 'française');
INSERT INTO languages VALUES(NULL, 'español');
INSERT INTO languages VALUES(NULL, 'deutsch');
INSERT INTO languages VALUES(NULL, '日本語');
DROP TABLE IF EXISTS verbs;
CREATE TABLE verbs(verb_id INTEGER PRIMARY KEY,
                   language_id INTEGER,
                   verb TEXT NOT NULL,
                   aux TEXT NOT NULL,
                   past_participle TEXT NOT NULL,
                   present_participle TEXT NOT NULL,
                   is_reflexive TINYINT DEFAULT 0,
                   is_aux TINYINT DEFAULT 0,
                   is_irregular TINYINT DEFAULT 0,
                   FOREIGN KEY(language_id) REFERENCES languages(language_id));
DROP TABLE IF EXISTS tenses;
CREATE TABLE tenses(tense_id INTEGER PRIMARY KEY,
                    language_id INTEGER,
                    tense_name TEXT NOT NULL,
                    is_simple TINYINT DEFAULT 0,
                    is_compound TINYINT DEFAULT 0,
                    is_subjunctive TINYINT DEFAULT 0,
                    FOREIGN KEY(language_id) REFERENCES languages(language_id));
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'présent', 1, 0, 0);
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'passé simple', 1, 0, 0);
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'imparfait', 1, 0, 0);
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'futur', 1, 0, 0);
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'conditionnel', 1, 0, 0);
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'subjonctif présent', 1, 0, 1);
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'subjonctif imparfait', 1, 0, 1);
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'passé composé', 0, 1, 0);
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'plus-que-parfait', 0, 1, 0);
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'futur antérieur', 0, 1, 0);
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'passé antérieur', 0, 1, 0);
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'subjonctif passé', 0, 1, 1);
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'subjonctif plus-que-parfait', 0, 1, 1);
INSERT INTO tenses VALUES(NULL, (SELECT language_id FROM languages WHERE language_name = 'française'), 'passé du conditionnel', 0, 1, 0);

DROP TABLE IF EXISTS tense_endings;
CREATE TABLE tense_endings(ending_id INTEGER PRIMARY KEY,
                           tense_id INTEGER,
                           verb_type TEXT NOT NULL,
                           fps TEXT NOT NULL,
                           sps TEXT NOT NULL,
                           tps TEXT NOT NULL,
                           fpp TEXT NOT NULL,
                           spp TEXT NOT NULL,
                           tpp TEXT NOT NULL,
                           FOREIGN KEY(tense_id) REFERENCES tenses(tense_id));

INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'présent'), 'er', 'e', 'es', 'e', 'ons', 'ez', 'ent' );
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'imparfait'), 'er', 'ais', 'ais', 'ait', 'ions', 'iez', 'aient');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'passé simple'), 'er', 'ai', 'as', 'a', 'âmes', 'âtes', 'èrent');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'futur'), 'er', 'ai', 'as', 'a', 'ons', 'ez', 'ont');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'conditionnel'), 'er', 'ais', 'ais', 'ait', 'ions', 'iez', 'aient');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'subjonctif présent'), 'er', 'e', 'es', 'e', 'ions', 'iez', 'ent');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'subjonctif imparfait'), 'er', 'asse', 'asses', 'ât', 'assions', 'assiez', 'assent');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'présent'), 'ir', 'is', 'is', 'it', 'issons', 'issez', 'issent');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'imparfait'), 'ir', 'ais', 'ais', 'ait', 'ions', 'iez', 'aient');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'passé simple'), 'ir', 'is', 'is', 'it', 'îmes', 'îtes', 'irent');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'futur'), 'ir', 'ai', 'as', 'a', 'ons', 'ez', 'ont');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'conditionnel'), 'ir', 'ais', 'ais', 'ait', 'ions', 'iez', 'aient');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'subjonctif présent'), 'ir', 'e', 'es', 'e', 'ions', 'iez', 'ent');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'subjonctif imparfait'), 'ir', 'isse', 'isses', 'ît', 'issions', 'issiez', 'issent');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'présent'), 're', 's', 's', '', 'ons', 'ez', 'ent');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'imparfait'), 're', 'ais', 'ais', 'ait', 'ions', 'iez', 'aient');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'passé simple'), 're', 'is', 'is', 'it', 'îmes', 'îtes', 'irent');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'futur'), 're', 'ai', 'as', 'a', 'ons', 'ez', 'ont');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'conditionnel'), 're', 'ais', 'ais', 'ait', 'ions', 'iez', 'aient');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'subjonctif présent'), 're', 'e', 'es', 'e', 'ions', 'iez', 'ent');
INSERT INTO tense_endings VALUES(NULL, (SELECT tense_id FROM tenses WHERE tense_name = 'subjonctif imparfait'), 're', 'isse', 'isses', 'ît', 'issions', 'issiez', 'issent');
