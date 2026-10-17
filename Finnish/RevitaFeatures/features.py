topics = ['Topic: Present tense conjugation. Verb type 1. FIN', 'Topic: Present tense conjugation. Verb type 2. FIN', 'Topic: Present tense conjugation. Verb type 3. FIN', 'Topic: Present tense conjugation. Verb type 4. FIN', 'Topic: Present tense conjugation. Verb type 5. FIN', 'Topic: Negative present tense. Verb type 1-5. FIN', 'Topic: KPT in uku/yky words. FIN', 'Topic: KPT in lki/rki words. FIN', 'Topic: Existential/possession constructions. FIN', 'Topic: Verb government. SM 1. Present. FIN', 'Topic: Verb government. SM 2. FIN', 'Topic: Verb government. SM 3. FIN', 'Topic: Verb government. SM 4. FIN', 'Topic: Verb + location cases. FIN', 'Topic: Imperative: second person singular. FIN', 'Topic: Nouns ending -e, -nen, -i, -si. Singular. FIN', 'Topic: Demonstrative pronouns: tämä, tuo, se. FIN', 'Topic: Genitive/Partitive + postposition. FIN', 'Topic: Singular total object. FIN', 'Topic: Singular partitive object. FIN', 'Topic: Plural total object. FIN', 'Topic: Noun type: us/os/es (all cases). Singular. FIN', 'Topic: Plural nominative. Words ending with us/os/es. FIN', 'Topic: Time expressions. FIN', 'Topic: Imperfect tense. FIN', 'Topic: Noun type -As, -in. Singular. FIN', 'Topic: Plural nominative. Words ending with -As, -in. FIN', 'Topic: Genetiivi + täytyy: Nesessiivirakenne. FIN', 'Topic: Objekti: nesessiivirakenne. FIN', 'Topic: 3. infinitive in illative, inessive and elative: -maan, -massa, -masta. FIN', 'Topic: Verbityyppi 6. FIN', 'Topic: -minen verbaalisubstantiivi. FIN', 'Topic: Negatiivinen imperfekti: all verb types. FIN', 'Topic: Perfect tense. FIN', 'Topic: Verbi + mAAn. FIN', 'Topic: Sanatyypit ut/yt. FIN', 'Topic: Sanatyypit nut/nyt. FIN', 'Topic: Plural nominative. Words ending with ut/yt nut/nyt. FIN', 'Topic: Possessive suffixes. FIN', 'Topic: Pluperfect tense. FIN', 'Topic: Verbs of AISTI-group. FIN', 'Topic: Sanatyyppi Vus/Vys. FIN', 'Topic: Plural nominative. Words ending with Vus/Vys. FIN', 'Topic: Paikallissijat. Plural. FIN', 'Topic: Relative pronoun joka in singular. FIN', 'Topic: Pronoun Indefinite joku, jokin. FIN', 'Topic: Pronoun: Indefinite ei mikään. FIN', 'Topic: Pronoun: Indefinite ei kukaan. FIN', 'Topic: Relative pronoun joka in plural. FIN', 'Topic: Demonstrative pronouns in plural: nämä nuo ne. FIN', 'Topic: Interrogative pronouns: mikä, kuka. FIN', 'Topic: Partitive plural: talo, koira, kala, maa, mansikka. FIN', 'Topic: Partitive plural. Words ending with -e, -nen, -i. FIN', 'Topic: Partitive plural. Words ending with us/ys os/es. FIN', 'Topic: Partitive plural. Words ending with -As, -in. FIN', 'Topic: Partitive plural. Words ending with ut/yt nut/nyt. FIN', 'Topic: Partitive plural. Words ending with Vus/Vys. FIN', 'Topic: Partikkelit -kAAn, -kO. FIN', 'Topic: Konditionaali: nykyinen aika. FIN', 'Topic: Konditionaali: mennyt aika. FIN', 'Topic: Konditionaali: negatiivinen. FIN', 'Topic: Nouns ending in -ton/-tön. FIN', 'Topic: Basic cardinal numeral. FIN', 'Topic: Basic ordinal numeral. FIN', 'Topic: Compound cardinal numeral. FIN', 'Topic: Passive present. FIN', 'Topic: Tunnekausatiivi object. FIN', 'Topic: Passive imperfect. FIN', 'Topic: Passive perfect. FIN', 'Topic: Passive pluperfect. FIN', 'Topic: Imperative: second person plural. FIN', 'Topic: Imperative negative. FIN', 'Topic: Conditional Passive Present. FIN', 'Topic: Conditional Passive Perfect. FIN', 'Topic: Essive case. FIN', 'Topic: Translative case. FIN', 'Topic: 3. infinitive in adessive. FIN', 'Topic: 3. infinitive in abessive. FIN', 'Topic: Clitic -kin & -kaan/-kään. FIN', 'Topic: Clitic -han/-hän. FIN', 'Topic: Adjectives: comparative. All cases. FIN', 'Topic: Adjectives: superlative. All cases. FIN', 'Topic: Ordinal Numeral. FIN', 'Topic: Pronouns kumpi, kumpikin and ei kumpikaan in cases. FIN', 'Topic: Interrogative pronoun mones/monesko. FIN', 'Topic: VA-participle. FIN', 'Topic: TAVA-participle. FIN', 'Topic: NUT- and TU-participles. FIN', 'Topic: MA-participle. FIN', 'Topic: All possessive forms. FIN', 'Topic: Abessive case. FIN', 'Topic: Comitative case. FIN', 'Topic: Instructive case. FIN', 'Topic: Instructive 3 infinitive. FIN', 'Topic: Että-lauseenvastike-present. FIN', 'Topic: Että-lauseenvastike-perfect. FIN', 'Topic: KUN-lauseenvastike-present. FIN', 'Topic: KUN-lauseenvastike-perfect. FIN', 'Topic: KSE-infinitive-possessive. FIN', 'Topic: EN-infinitive. FIN', 'Topic: All instructive infinitives. FIN']
# 这个文件是专门用来去除不需要的特征的

feature_name_map = {'average_num_pos': 'Number of POS', 'average_tree_depth': 'Syntactic tree depth',
                    'average_sentence_length': 'Sentence length', 'OOV_coverage': 'Rare words',
                    'vocab_bag_1_coverage': 'Vocabulary bag 1', 'vocab_bag_2_coverage': 'Vocabulary bag 2',
                    'vocab_bag_3_coverage': 'Vocabulary bag 3', 'vocab_bag_4_coverage': 'Vocabulary bag 4',
                    'vocab_bag_5_coverage': 'Vocabulary bag 6', 'vocab_bag_6_coverage': 'Vocabulary bag 6',
                    'vocab_bag_7_coverage': 'Vocabulary bag 7', 'vocab_bag_8_coverage': 'Vocabulary bag 8',
                    'vocab_bag_9_coverage': 'Vocabulary bag 9', 'vocab_bag_10_coverage': 'Vocabulary bag 10',
                    'Noun-Paradigm-vowel': 'Nouns with vowel stem', 'Noun-Paradigm-talo': 'Paradigm "talo"',
                    'Noun-Paradigm-koira': 'Paradigm "koira/koiria"', 'Noun-Paradigm-kala': 'Paradigm "kala/kaloja"',
                    'Noun-Paradigm-bussi': 'Paradigm "bussi/n"', 'Noun-Paradigm-ovi': 'Paradigm "ovi/oven"',
                    'Noun-Paradigm-maa': 'Paradigm "maa/suo/valtio"', 'Noun-Paradigm-uusi': 'Paradigm "uusi"',
                    'Noun-Paradigm-mansikka': 'Paradigm "mansikka/mansikoita"',
                    'Noun-Paradigm-consonant': 'Nouns with consonant stem',
                    'Noun-Paradigm-kysymys': 'Paradigm "vastaus/kerros/vihannes"',
                    'Noun-Paradigm-aihe': 'Paradigm "aihe"', 'Noun-Paradigm-valas': 'Paradigm "asiakas/asiakkaan"',
                    'Noun-Paradigm-puhelin': 'Paradigm "puhelin"', 'Noun-Paradigm-olut': 'Paradigm "olut"',
                    'Noun-Paradigm-UNDEFINED': 'Paradigm "kevät"', 'Noun-Paradigm-nainen': 'Paradigm "nainen"',
                    'Noun-Paradigm-kannel': 'Paradigm "kannel"', 'Noun-Paradigm-manner': 'Paradigm "tytär/ien/joutsen"',
                    'Noun-Paradigm-koditon': 'Paradigm "koditon"', 'Noun-Paradigm-uutuus': 'Paradigm "uutuus"',
                    'Noun-Paradigm-other': 'Noun paradigm', 'Noun-pluralia-tantum': 'Pluralia Tantum',
                    'Noun-Compound-Inflection': 'Inflection inside compound',
                    'Noun-Possessive suffixes': 'Possessive suffixes', 'Noun-Time': 'Time expressions',
                    'Noun-Time-All': 'Time expressions', 'Noun-Time-Hour-adessive': 'Noun type: Hour, in adessive',
                    'Noun-Time-TOD-adessive+essive': 'Noun type: Time of a day, in adessive or essive',
                    'Noun-Time-Day-essive': 'Noun type: Day, in essive',
                    'Noun-Time-Week-adessive': 'Noun type: Week, in adessive',
                    'Noun-Time-Month-inessive': 'Noun type: Month, in inessive',
                    'Noun-Time-Season-adessive+essive': 'Noun type: Season, in adessive or essive',
                    'Noun-Time-Year-essive': 'Noun type: Year, in essive', 'Number-ROOT': 'Number',
                    'Number-Singular': 'Singular number', 'Number-Plural': 'Plural number', 'Case-ROOT': 'Case',
                    'Case-Nominative': 'Nominative case', 'Case-Accusative': 'Accusative case',
                    'Case-Genitive': 'Genitive case', 'Case-Genitive-Plural': 'Genitive plural',
                    'Case-Partitive': 'Partitive case', 'Case-Partitive-Plural': 'Lesson: Partitive plural',
                    'Case-Inner-Locative': 'Inner locative cases', 'Case-Inessive': 'Inessive case',
                    'Case-Elative': 'Elative case', 'Case-Illative': 'Illative case',
                    'Case-Outer-Locative': 'Outer locative cases', 'Case-Adessive': 'Adessive case',
                    'Case-Ablative': 'Ablative case', 'Case-Allative': 'Allative case',
                    'Case-Essive': 'Essive case', 'Case-Translative': 'Translative case',
                    'Case-Instructive': 'Instructive case', 'Case-Abessive': 'Abessive case',
                    'Case-Comitative': 'Comitative case', 'Adjective-ROOT': 'Adjective',
                    'Adjective-positive': 'Positive adjectives', 'Adjective-comparative': 'Comparative adjectives',
                    'Adjective-superlative': 'Superlative adjectives', 'Morpho-phonemics-ROOT': 'Morpho-Phonemics',
                    'Morpho-phonemics-Vowel-harmony': 'Vowel harmony',
                    'Morpho-phonemics-Consonant-gradation-double': 'Consonant gradation kk/pp/tt',
                    'Morpho-phonemics-Consonant-gradation-single': 'Consonant gradation k/p/t',
                    'Morpho-phonemics-Consonant-gradation-k-j': 'Consonant gradation k/j',
                    'Morpho-phonemics-Derivation': 'Derivation',
                    'Morpho-phonemics-Consonant-gradation-A-type-Nouns': 'Consonant gradation. A-type. Nouns',
                    'Morpho-phonemics-Consonant-gradation-A-type-Nouns-Active': 'Consonant gradation. A-type. Nouns',
                    'Morpho-phonemics-Consonant-gradation-A-type-Nouns-Inactive': 'Consonant gradation. A-type. Nouns',
                    'Morpho-phonemics-Consonant-gradation-A-type-Verbs': 'Consonant gradation. A-type. Verbs',
                    'Morpho-phonemics-Consonant-gradation-A-type-Verbs-Active': 'Consonant gradation. A-type. Verbs.',
                    'Morpho-phonemics-Consonant-gradation-A-type-Verbs-Inactive': 'Consonant gradation. A-type. Verbs.',
                    'Morpho-phonemics-Consonant-gradation-B-type-Nouns': 'Consonant gradation. B-type. Nouns',
                    'Morpho-phonemics-Consonant-gradation-B-type-Nouns-Active': 'Consonant gradation. B-type. Nouns.',
                    'Morpho-phonemics-Consonant-gradation-B-type-Nouns-Inactive': 'Consonant gradation. B-type. Nouns.',
                    'Morpho-phonemics-Consonant-gradation-B-type-Verbs': 'Consonant gradation. B-type. Verbs',
                    'Morpho-phonemics-Consonant-gradation-B-type-Verbs-Active': 'Consonant gradation. B-type. Verbs.',
                    'Morpho-phonemics-Consonant-gradation-B-type-Verbs-Inactive': 'Consonant gradation. B-type. Verbs.',
                    'Morpho-phonemics-Consonant-gradation-A-type-uku': 'Consonant gradation. A-type. uku-yky',
                    'Morpho-phonemics-Consonant-gradation-A-type-uku-Active': 'Consonant gradation. A-type. uku-yky.',
                    'Morpho-phonemics-Consonant-gradation-A-type-uku-Inactive': 'Consonant gradation. A-type. uku-yky.',
                    'Morpho-phonemics-Consonant-gradation-A-type-lki': 'Consonant gradation. A-type. lki-rki',
                    'Morpho-phonemics-Consonant-gradation-A-type-lki-Active': 'Consonant gradation. A-type. lki-rki.',
                    'Morpho-phonemics-Consonant-gradation-A-type-lki-Inactive': 'Consonant gradation. A-type. lki-rki.',
                    'Verb-ROOT': 'Verb inflection', 'Verb-Paradigm': 'Verb Paradigm',
                    'Verb-Paradigm-sanoa': 'Paradigm "sanoa/muistaa/tuntea"',
                    'Verb-Paradigm-saada': 'Paradigm "voida/saada/juoda"', 'Verb-Paradigm-tehdä': 'Paradigm "tehdä"',
                    'Verb-Paradigm-tulla': 'Paradigm "tulla/purra/kävellä"', 'Verb-Paradigm-juosta': 'Paradigm "juosta"',
                    'Verb-Paradigm-nousta': 'Paradigm "nousta"', 'Verb-Paradigm-haluta': 'Paradigm "haluta/salata/katketa"',
                    'Verb-Paradigm-tarvita': 'Paradigm "tarvita"', 'Verb-Paradigm-vanheta': 'Paradigm "vanheta"',
                    'Verb-Paradigm-other': 'Verb Paradigm', 'Clitics-ROOT': 'Clitics',
                    'Clitics-Question': 'Clitic question (-kO)', 'Clitics-Emphasis': 'Clitic of emphasis (-kin)',
                    'Clitics-Negation': 'Clitic of negation (-kAAn)', 'Clitics-han': 'Clitic (-hAn)', 'Clitics-pa': 'Clitic (-pA)',
                    'Possessiveness-ROOT': 'Possessiveness', 'Possessiveness-All pos': 'Possessive forms',
                    'Verb-Mood': 'Mood', 'Mood-Indicative': 'Indicative', 'Mood-Imperative': 'Imperative mood',
                    'Mood-Conditional': 'Conditional mood', 'Mood-Potential': 'Potential mood',
                    'Mood-Imperative-Negative': 'Imperative negative', 'Mood-Conditional-Negative': 'Conditional negative',
                    'Mood-Potential-Negative': 'Potential negative', 'Mood-Imperative-Passive': 'Imperative passive',
                    'Mood-Conditional-Passive': 'Conditional passive', 'Mood-Potential-Passive': 'Potential passive',
                    'Verb-Voice': 'Voice', 'Voice-Active': 'Active Voice', 'Voice-Passive': 'Passive (Impersonal)',
                    'Voice-Passive-Present': 'Passive present', 'Voice-Passive-Imperfect': 'Passive imperfect',
                    'Voice-Passive-Perfect': 'Passive perfect', 'Voice-Passive-Pluperfect': 'Passive pluperfect',
                    'Verb-Tense': 'Tense', 'Tense-Present': 'Present Tense', 'Tense-Imperfect': 'Imperfect Tense',
                    'Tense-Perfect': 'Perfect Tense', 'Tense-Pluperfect': 'Pluperfect Tense',
                    'Tense-Imperfect-Indicative': 'Indicative Imperfect tense', 'Tense-Perfect-Indicative': 'Indicative Perfect tense',
                    'Tense-Pluperfect-Indicative': 'Indicative Pluperfect tense',
                    'Tense-Imperfect-Indicative-Negative': 'Indicative negative imperfect',
                    'Verb-Polarity': 'Negation', 'Polarity-Positive': 'Positive', 'Polarity-Negative': 'Negative',
                    'Verb-Person': 'Person', 'Person-1': '1st Person', 'Person-2': '2nd Person',
                    'Person-3': '3rd Person', 'Verb-Participle': 'Participle', 'Participle-Active': 'Active participle',
                    'Participle-Passive': 'Passive participle', 'Participle-Present-Active-Easy': 'Participle: Present Active -va',
                    'Participle-Present-Active': 'Participle: Present Active -va',
                    'Participle-Present-Passive-Easy': 'Participle: Present Passive -ttava',
                    'Participle-Present-Passive': 'Participle: Present Passive -ttava',
                    'Participle-Perfect-Active-Easy': 'Participle: Perfect Active -nut',
                    'Participle-Perfect-Active': 'Participle: Perfect Active -nut',
                    'Participle-Perfect-Passive-Easy': 'Participle: Perfect Passive -ttu',
                    'Participle-Perfect-Passive': 'Participle: Perfect Passive -ttu',
                    'Participle-Agentive-Easy': 'Agentive participle', 'Participle-Agentive': 'Agentive participle',
                    'Participle-Negative-Easy': 'Participle: Negative -maton',
                    'Participle-Negative': 'Participle: Negative -maton',
                    'Participle-Possessive suffixes': 'Participle: Possessive forms', 
                    'Infinitive-1': 'Infinitive I (-A)', 'Infinitive-2': 'Infinitive II (-e)', 'Infinitive-3': 'Infinitive III (-mA)',
                    'Infinitive-4': 'Infinitive IV (-minen)', 'Infinitive-5': 'Infinitive V (-mAisillA)', 'Infinitive-TUA': 'TUA-Infinitive',
                    'Infinitive-TUA-maybe': 'TUA Infinitive', 
                    'Infinitive-1-Lative': 'Infinitive I (-A) in lative', 'Infinitive-2-Instructive-Active': 'Infinitive II (-e) in instructive',
                    'Infinitive-ESSA-Active': 'ESSA-Infinitive. Active', 'Infinitive-ESSA-Passive': 'ESSA-Infinitive. Passive',
                    'Infinitive-3-Inessive-Active': 'Infinitive III (-mA). Inessive',
                    'Infinitive-3-Elative-Active': 'Infinitive III (-mA). Elative',
                    'Infinitive-3-Illative-Active': 'Infinitive III (-mA). Illative',
                    'Infinitive-3-Adessive-Active': 'Infinitive III (-mA). Adessive',
                    'Infinitive-3-Abessive-Active': 'Infinitive III (-mA). Abessive',
                    'Infinitive-3-Instructive-Active': 'Infinitive III (-mA). Instructive. Active',
                    'Infinitive-3-Instructive-Passive': 'Infinitive III (-mA). Instructive. Passive',
                    'Verb-Transitive_pair': 'Transitive & intransitive verbs', 'Verb-Verb_nests': 'Verb nest pairs',
                    'Verb-Infinitive_bases': 'Infinitive bases', 'Adverb-ROOT': 'Adverbs',
                    'Adverb-Comparative': 'Adverb: Comparative', 'Adverb-Superlative': 'Adverb: Superlative',
                    'Pronoun-ROOT': 'Pronouns', 'Pronoun-Personal': 'Pronoun: Personal minä',
                    'Pronoun-Relative': 'Pronoun: Relative "joka"', 'Pronoun-Demonstrative': 'Pronoun: Demonstrative "tuo"',
                    'Pronoun-Indefinite': 'Pronoun: Indefinite "joku"', 'Pronoun-Indefinite-joku': 'Pronoun Indefinite "joku", "jokin"',
                    'Pronoun-Interrogative': 'Pronoun: Interrogative', 'Pronoun-Interrogative-kumpi': 'Pronoun: Interrogative ("kumpi")',
                    'Pronoun-Interrogative-mones': 'Pronoun: Interrogative (mones)', 'Pronoun-Reflexive': 'Pronoun: Reflexive "itse"',
                    'Pronoun-Reciprocal': 'Pronoun: Reciprocal "toisensa"',
                    'Pronoun-Indefinite-mikään': 'Pronoun: Indefinite "ei mikään"',
                    'Pronoun-Indefinite-kukaan': 'Pronoun: Indefinite "ei kukaan"',
                    'Numeral-ROOT': 'Numerals', 'Numeral-Cardinal': 'Cardinal numeral',
                    'Numeral-Cardinal-short': 'Basic cardinal numeral',
                    'Numeral-Cardinal-long': 'Compound cardinal numeral',
                    'Numeral-Ordinal': 'Ordinal numeral', 'Numeral-Ordinal-short': 'Basic ordinal numeral',
                    'Numeral-Ordinal-long': 'Compound ordinal numeral', 'Numeral-Quantifier': 'Quantifier',
                    'Lexicon-ROOT': 'Lexicon', 'Lexicon-Definitions': 'Lexicon: Definitions',
                    'Verb-Confusable_words': 'Confusable verbs', 'Noun-Confusable_words': 'Confusable nouns',
                    'Verb-SM-level-1': 'Suomen mestari Verb 1', 'Verb-SM-level-2': 'Suomen mestari Verb 2',
                    'Verb-SM-level-3': 'Suomen mestari Verb 3', 'Verb-SM-level-4': 'Suomen mestari Verb 4',
                    'Syntax-ROOT': 'Syntax',
                    'Syntax-Genitive-modifier': 'Genitive modifier', 'Syntax-Conjunctions': 'Syntax: conjunctions',
                    'Syntax-Sentence types': 'Sentence types', 'Syntax-Nollapersoona': 'Nollapersoona',
                    'Syntax-Verb-subject': 'Subject of verb', 'Syntax-construction-subject': 'Subject of construction',
                    'Syntax-construction-head': 'Head of construction',
                    'Syntax-construction-complement': 'Complement of predicate',
                    'Syntax-construction-argument': 'Argument of construction',
                    'Syntax-temporal-expression': 'Temporal expression',
                    'Government-ROOT': 'Government', 'Government-adposition': 'Adposition. Case government (of Noun+Pronoun)',
                    'Government-Verb': 'Verb. Case and Adposition government',
                    'Government-Noun': 'Noun government', 'Government-Adjective': 'Adjective government',
                    'Government-Numeral': 'Numeral government', 'Government-Governee': 'Governee in government construction',
                    'Government-Adposition-Governee': 'Governee of adposition',
                    'Government-Adposition-Choice': 'Genitive/Partitive adposition choice',
                    'Agreement-ROOT': 'Agreement', 'Agreement-NP': 'NP-agreement', 'Syntax-Verb-object': 'Verb Object',
                    'Syntax-DEFAULT-object-of-Infinitive': 'Infinitive object',
                    'Syntax-Active-object': 'Indicative / Conditional / Potential Active object',
                    'Syntax-object-negative': 'Negative object', 'Syntax-tunnekausatiivi-object': 'Tunnekausatiivi object',
                    'Syntax-Imperative-object': 'Imperative object', 'Syntax-Passive-object': 'Passive object',
                    'Syntax-Nesessiivi-rakenne-object': 'Nesessiivi-rakenne object',
                    'Syntax-Nesessiivi-rakenne-object-negative': 'Nesessiivi-rakenne object (negative)',

                    'Syntax-ablatiivi-aisti': 'ablatiivi-aisti', 'Syntax-ablative-epatoivottu-katsoja': 'ablative-epatoivottu-katsoja', # ??
                    'Syntax-ablative-este': 'ablative-este', 'Syntax-ablatiivi-lähde': 'ablatiivi-lähde', # ??
                    'Syntax-adessiivi-keino-väline': 'adessiivi-keino-väline', 'Syntax-allatiivi-aisti': 'allatiivi-aisti', # ??
                    'Syntax-allatiivi-kommunikaatio': 'allatiivi-kommunikaatio', 'Syntax-allative-omistaminen': 'allative-omistaminen', # ??

                    'Syntax-Construction': 'Construction', 'Construction-Possession': 'Possession construction',
                    'Construction-Existential': 'Existential construction',
                    'Construction-Possession-Positive': 'Possession construction (positive)',
                    'Construction-Possession-Negative': 'Possession construction (negative)',
                    'Construction-Existential-Positive': 'Existential construction (positive)',
                    'Construction-Existential-Negative': 'Existential construction (negative)',
                    'Construction-Että-lauseenvastike-present': 'Että-lauseenvastike present',
                    'Construction-Että-lauseenvastike-perfect': 'Että-lauseenvastike past',
                    'Construction-Että-lauseenvastike-subject-eri-tekijät': 'Että-lauseenvastike subject (eri tekijät)',
                    'Construction-Että-lauseenvastike-verb-eri-tekijät': 'Että-lauseenvastike verb (eri tekijät)',
                    'Construction-Että-lauseenvastike-verb-sama-tekijä': 'Että-lauseenvastike verb (sama tekijä)',
                    'Construction-Different-actors': 'Construction of different actors',
                    'Construction-Same-actors': 'Construction of same actors',
                    'Construction-Nesessiivi-rakenne': 'Nesessiivirakenne',
                    'Construction-Permissiivi-rakenne': 'Permissiivirakenne',
                    'Construction-TUA-Temporaalirakenne': 'Temporaalirakenne: Past temporal construction',
                    'Construction-ESSA-Temporaalirakenne': 'Temporaalirakenne: Present temporal construction',
          
                  'Construction-Negative': 'Negative construction'}

basic_features = list(feature_name_map.keys())
concepts = ["Noun-Paradigm-vowel", "Noun-Paradigm-talo", "Noun-Paradigm-koira", "Noun-Paradigm-kala", "Noun-Paradigm-bussi", "Noun-Paradigm-ovi", "Noun-Paradigm-maa", "Noun-Paradigm-uusi", "Noun-Paradigm-mansikka", "Noun-Paradigm-consonant", "Noun-Paradigm-kysymys", "Noun-Paradigm-aihe", "Noun-Paradigm-valas", "Noun-Paradigm-puhelin", "Noun-Paradigm-olut", "Noun-Paradigm-UNDEFINED", "Noun-Paradigm-nainen", "Noun-Paradigm-kannel", "Noun-Paradigm-manner", "Noun-Paradigm-koditon", "Noun-Paradigm-uutuus", "Noun-Paradigm-other", "Noun-pluralia-tantum", "Noun-Compound-Inflection", "Noun-Possessive suffixes", "Noun-Time", "Noun-Time-All", "Noun-Time-Hour-adessive", "Noun-Time-TOD-adessive+essive", "Noun-Time-Day-essive", "Noun-Time-Week-adessive", "Noun-Time-Month-inessive", "Noun-Time-Season-adessive+essive", "Noun-Time-Year-essive", "Number-ROOT", "Number-Singular", "Number-Plural", "Case-ROOT", "Case-Nominative", "Case-Accusative", "Case-Genitive", "Case-Genitive-Plural", "Case-Partitive", "Case-Partitive-Plural", "Case-Inner-Locative", "Case-Inessive", "Case-Elative", "Case-Illative", "Case-Outer-Locative", "Case-Adessive", "Case-Ablative", "Case-Allative", "Case-Essive", "Case-Translative", "Case-Instructive", "Case-Abessive", "Case-Comitative", "Adjective-ROOT", "Adjective-positive", "Adjective-comparative", "Adjective-superlative", "Morpho-phonemics-ROOT", "Morpho-phonemics-Vowel-harmony", "Morpho-phonemics-Consonant-gradation-double", "Morpho-phonemics-Consonant-gradation-single", "Morpho-phonemics-Consonant-gradation-k-j", "Morpho-phonemics-Derivation", "Morpho-phonemics-Consonant-gradation-A-type-Nouns", "Morpho-phonemics-Consonant-gradation-A-type-Nouns-Active", "Morpho-phonemics-Consonant-gradation-A-type-Nouns-Inactive", "Morpho-phonemics-Consonant-gradation-A-type-Verbs", "Morpho-phonemics-Consonant-gradation-A-type-Verbs-Active", "Morpho-phonemics-Consonant-gradation-A-type-Verbs-Inactive", "Morpho-phonemics-Consonant-gradation-B-type-Nouns", "Morpho-phonemics-Consonant-gradation-B-type-Nouns-Active", "Morpho-phonemics-Consonant-gradation-B-type-Nouns-Inactive", "Morpho-phonemics-Consonant-gradation-B-type-Verbs", "Morpho-phonemics-Consonant-gradation-B-type-Verbs-Active", "Morpho-phonemics-Consonant-gradation-B-type-Verbs-Inactive", "Morpho-phonemics-Consonant-gradation-A-type-uku", "Morpho-phonemics-Consonant-gradation-A-type-uku-Active", "Morpho-phonemics-Consonant-gradation-A-type-uku-Inactive", "Morpho-phonemics-Consonant-gradation-A-type-lki", "Morpho-phonemics-Consonant-gradation-A-type-lki-Active", "Morpho-phonemics-Consonant-gradation-A-type-lki-Inactive", "Verb-ROOT", "Verb-Paradigm", "Verb-Paradigm-sanoa", "Verb-Paradigm-saada", "Verb-Paradigm-tehdä", "Verb-Paradigm-tulla", "Verb-Paradigm-juosta", "Verb-Paradigm-nousta", "Verb-Paradigm-haluta", "Verb-Paradigm-tarvita", "Verb-Paradigm-vanheta", "Verb-Paradigm-other", "Clitics-ROOT", "Clitics-Question", "Clitics-Emphasis", "Clitics-Negation", "Clitics-han", "Clitics-pa", "Possessiveness-ROOT", "Possessiveness-All pos", "Verb-Mood", "Mood-Indicative", "Mood-Imperative", "Mood-Conditional", "Mood-Potential", "Mood-Imperative-Negative", "Mood-Conditional-Negative", "Mood-Potential-Negative", "Mood-Imperative-Passive", "Mood-Conditional-Passive", "Mood-Potential-Passive", "Verb-Voice", "Voice-Active", "Voice-Passive", "Voice-Passive-Present", "Voice-Passive-Imperfect", "Voice-Passive-Perfect", "Voice-Passive-Pluperfect", "Verb-Tense", "Tense-Present", "Tense-Imperfect", "Tense-Perfect", "Tense-Pluperfect", "Tense-Imperfect-Indicative", "Tense-Perfect-Indicative", "Tense-Pluperfect-Indicative", "Tense-Imperfect-Indicative-Negative", "Verb-Polarity", "Polarity-Positive", "Polarity-Negative", "Verb-Person", "Person-1", "Person-2", "Person-3", "Verb-Participle", "Participle-Active", "Participle-Passive", "Participle-Present-Active-Easy", "Participle-Present-Active", "Participle-Present-Passive-Easy", "Participle-Present-Passive", "Participle-Perfect-Active-Easy", "Participle-Perfect-Active", "Participle-Perfect-Passive-Easy", "Participle-Perfect-Passive", "Participle-Agentive-Easy", "Participle-Agentive", "Participle-Negative-Easy", "Participle-Negative", "Participle-Possessive suffixes", "Verb-Infitive", "Infinitive-1", "Infinitive-2", "Infinitive-3", "Infinitive-4", "Infinitive-5", "Infinitive-TUA", "Infinitive-TUA-maybe", "Infinitive-1-Translative", "Infinitive-1-Lative", "Infinitive-2-Instructive-Active", "Infinitive-ESSA-Active", "Infinitive-ESSA-Passive", "Infinitive-3-Inessive-Active", "Infinitive-3-Elative-Active", "Infinitive-3-Illative-Active", "Infinitive-3-Adessive-Active", "Infinitive-3-Abessive-Active", "Infinitive-3-Instructive-Active", "Infinitive-3-Instructive-Passive", "Verb-Transitive_pair", "Verb-Verb_nests", "Verb-Infinitive_bases", "Adverb-ROOT", "Adverb-Comparative", "Adverb-Superlative", "Pronoun-ROOT", "Pronoun-Personal", "Pronoun-Relative", "Pronoun-Demonstrative", "Pronoun-Indefinite", "Pronoun-Indefinite-joku", "Pronoun-Interrogative", "Pronoun-Interrogative-kumpi", "Pronoun-Interrogative-mones", "Pronoun-Reflexive", "Pronoun-Reciprocal", "Pronoun-Indefinite-mikään", "Pronoun-Indefinite-kukaan", "Numeral-ROOT", "Numeral-Cardinal", "Numeral-Cardinal-short", "Numeral-Cardinal-long", "Numeral-Ordinal", "Numeral-Ordinal-short", "Numeral-Ordinal-long", "Numeral-Quantifier", "Lexicon-ROOT", "Lexicon-Definitions", "Verb-Confusable_words", "Noun-Confusable_words", "Verb-SM-level-1", "Verb-SM-level-2", "Verb-SM-level-3", "Verb-SM-level-4", "Syntax-ROOT", "Syntax-Genitive-modifier", "Syntax-Conjunctions", "Syntax-Sentence types", "Syntax-Nollapersoona", "Syntax-Verb-subject", "Syntax-construction-subject", "Syntax-construction-head", "Syntax-construction-complement", "Syntax-construction-argument", "Syntax-temporal-expression", "Government-ROOT", "Government-adposition", "Government-Verb", "Government-Noun", "Government-Adjective", "Government-Numeral", "Government-Governee", "Government-Adposition-Governee", "Government-Adposition-Choice", "Agreement-ROOT", "Agreement-NP", "Syntax-Verb-object", "Syntax-DEFAULT-object-of-Infinitive", "Syntax-Active-object", "Syntax-object-negative", "Syntax-tunnekausatiivi-object", "Syntax-Imperative-object", "Syntax-Passive-object", "Syntax-Nesessiivi-rakenne-object", "Syntax-Nesessiivi-rakenne-object-negative", "Syntax-ablatiivi-aisti", "Syntax-ablative-epatoivottu-katsoja", "Syntax-ablative-este", "Syntax-ablatiivi-lähde", "Syntax-adessiivi-keino-väline", "Syntax-allatiivi-aisti", "Syntax-allatiivi-kommunikaatio", "Syntax-allative-omistaminen", "Syntax-Construction", "Construction-Possession", "Construction-Existential", "Construction-Possession-Positive", "Construction-Possession-Negative", "Construction-Existential-Positive", "Construction-Existential-Negative", "Construction-Että-lauseenvastike-present", "Construction-Että-lauseenvastike-perfect", "Construction-Että-lauseenvastike-subject-eri-tekijät", "Construction-Että-lauseenvastike-verb-eri-tekijät", "Construction-Että-lauseenvastike-verb-sama-tekijä", "Construction-Different-actors", "Construction-Same-actors", "Construction-Nesessiivi-rakenne", "Construction-Permissiivi-rakenne", "Construction-TUA-Temporaalirakenne", "Construction-ESSA-Temporaalirakenne", "Construction-Negative"]



import pandas as pd
import numpy as np

def process_csv(input_file, output_file, remove_columns_list1, keep_topic_list2):
    """
    处理CSV文件，去除list1中的列，只保留list2中的Topic列并重新归一化
    参数:
        input_file: 输入CSV文件路径
        output_file: 输出CSV文件路径
        remove_columns_list1: 要去除的列名列表
        keep_topic_list2: 要保留的Topic列名列表（会被重新归一化）
    """
    # 读取CSV
    df = pd.read_csv(input_file)
    print(f"\n处理文件: {input_file}")
    print(f"原始数据 NaN 数量: {df.isna().sum().sum()}")
    # 1. 总体统计
    total_nan = df.isna().sum().sum()
    print(f"原始数据 NaN 数量: {total_nan}")

    # 2. 按列统计NaN
    print("\n每列的 NaN 数量:")
    nan_per_column = df.isna().sum()
    print(nan_per_column[nan_per_column > 0])  # 只显示有NaN的列

    # 3. 显示具体哪些行有NaN
    if total_nan > 0:
        print("\n包含 NaN 的行索引:")
        rows_with_nan = df[df.isna().any(axis=1)]
        print(f"行号: {rows_with_nan.index.tolist()}")
        
        # 4. 显示具体的NaN位置（行号、列名、值）
        print("\nNaN 的具体位置:")
        for col in df.columns:
            nan_rows = df[df[col].isna()].index.tolist()
            if nan_rows:
                print(f"  列 '{col}': 行 {nan_rows}")
        
        # 5. 显示前几个包含NaN的完整行（方便查看上下文）
        print("\n前5个包含 NaN 的行:")
        print(rows_with_nan.head())
    # 第一步：去除list1中的列
    df = df.drop(columns=remove_columns_list1, errors='ignore')
    
    # 第二步：找出所有Topic列
    all_topic_cols = [col for col in df.columns if col.startswith('Topic')]
    
    # 第三步：去除不在list2中的Topic列
    topic_cols_to_remove = [col for col in all_topic_cols if col not in keep_topic_list2]
    df = df.drop(columns=topic_cols_to_remove, errors='ignore')
    
    # 第四步：对保留的Topic列进行归一化
    # if keep_topic_list2:
    #     # 只对实际存在的Topic列进行归一化
    #     existing_topic_cols = [col for col in keep_topic_list2 if col in df.columns]
        
    #     if existing_topic_cols:
    #         # 检查归一化前的数据
    #         print(f"归一化前 Topic 列 NaN 数量: {df[existing_topic_cols].isna().sum().sum()}")
            
    #         # 计算每行保留的Topic列的总和
    #         topic_sum = df[existing_topic_cols].sum(axis=1)
            
    #         # 【关键检查】找出总和为0或NaN的行
    #         zero_sum_rows = topic_sum == 0
    #         nan_sum_rows = topic_sum.isna()
            
    #         if zero_sum_rows.any():
    #             print(f"⚠️ 警告: 发现 {zero_sum_rows.sum()} 行的 Topic 列总和为 0!")
    #             print(f"  这些行的索引: {df[zero_sum_rows].index.tolist()[:10]}...")  # 只显示前10个
            
    #         if nan_sum_rows.any():
    #             print(f"⚠️ 警告: 发现 {nan_sum_rows.sum()} 行的 Topic 列总和为 NaN!")
    #             print(f"  这些行的索引: {df[nan_sum_rows].index.tolist()[:10]}...")
            
    #         # 重新归一化，使每行的Topic列相加等于1
    #         # 【修复方案】：避免除以0，对于总和为0或NaN的行，保持原值或设为均匀分布
    #         for col in existing_topic_cols:
    #             # 只对总和不为0且不为NaN的行进行归一化
    #             valid_rows = (topic_sum > 0) & (~topic_sum.isna())
    #             df.loc[valid_rows, col] = df.loc[valid_rows, col] / topic_sum[valid_rows]
                
    #             # 对于总和为0的行，设置为均匀分布
    #             if zero_sum_rows.any():
    #                 df.loc[zero_sum_rows, col] = 1.0 / len(existing_topic_cols)
            
    #         print(f"归一化后 NaN 数量: {df[existing_topic_cols].isna().sum().sum()}")
    
    # 最终检查
    print(f"最终数据 NaN 数量: {df.isna().sum().sum()}")
    
    # 保存结果
    df.to_csv(output_file, index=False)
    print(f"处理完成！已保存到 {output_file}")
    print(f"去除的列: {len(remove_columns_list1)} 个")
    print(f"保留的Topic列: {len([col for col in keep_topic_list2 if col in df.columns])} 个")
    
    return df

# 使用示例
df_result = process_csv('/home/yiheng/project/revita/revita/use_weighted/student_train.csv', 
                        '/home/yiheng/project/revita/revita/use_weighted/student_train_clean.csv', concepts, topics)
df_result = process_csv('/home/yiheng/project/revita/revita/use_weighted/student_test.csv', 
                        '/home/yiheng/project/revita/revita/use_weighted/student_test_clean.csv', concepts, topics)
# df_result = process_csv('TextFeatures/Finnish/RevitaFeatures/Source_ Difficulty texts with features - Fi_test.csv', 
#                         'TextFeatures/Finnish/RevitaFeatures/test.csv', concepts, topics)