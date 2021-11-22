import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

import django
django.setup()
chapter_titles = [
    [1, 'Sentence Constructions', 19],
    [2, 'Parts Of Speech', 27],
    [3, 'Kinds Of Nouns', 7],
    [4, 'Countable And Uncountable Nouns', 6],
    [5, 'The Noun - Number', 10],
    [6, 'The Noun - Gender', 4],
    [7, 'The Noun - Case', 5],
    [8, 'More About Pronouns', 16],
    [9, 'More About Adjectives', 16],
    [10, 'More About Verbs And Modals', 24],
    [11, 'Syntax - Subject-Verb Agreement', 9],
    [12, 'Conjugation Of Verbs', 19],
    [13, 'Time And Tense With Mood', 29],
    [14, 'Verbal Noun, Gerund And Participle', 9],
    [15, 'More About Adverbs And Adverbials', 17],
    [16, 'More About Prepositions', 19],
    [17, 'Appropriate Prepositions', 27],
    [18, 'More About Conjunctions', 7],
    [19, 'Articles And Determiners', 17],
    [20, 'Modifiers', 4],
    [21, 'Structural And Non-Structural Words', 3],
    [22, 'Narration/Reporting', 24],
    [23, 'Voice Change/Describing A Process', 15],
    [24, 'Phrases', 10],
    [25, 'Sentences And Its Clauses/Joining/Splitting', 23],
    [26, 'Transformation Of Sentences', 13],
    [27, 'Wh-Questions', 26],
    [28, 'Formation Of Words/Antonyms', 23],
    [29, 'Word Family/One Part Of Speech To Others', 13],
    [30, 'Same Word Used As Different', 8],
    [31, 'Words Commonly Confused', 21],
    [32, 'Group Verbs/Phrasal Verbs', 14],
    [33, 'Idioms', 8],
    [34, 'Nominal Compounds', 11],
    [35, 'Punctuation And Capitalization', 7],
]


from learn.models import Chapter 

def populate():
    for slno, title, page_no in chapter_titles:
        Chapter.objects.create(title = title, slno=slno, no_of_pages=page_no)

if __name__=="__main__":
    print('Pease wait... Populating Database')
    populate()
    print('Populating done')