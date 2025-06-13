# ----------------------------------------------------------------------
# This is the file mad_libs.py

# The intent is to give you practice writing a complete, interactive
# Python program using a lot of Python data types, especially lists,
# sets, and dictionaries.

# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
# ----------------------------------------------------------------------

# Things to do:

# Define a bunch of templates in which some of the words begin with a colon (:).
# The words that begin with a colon are the words that you will ask the user
# to fill in. An example of a template is:
#
#     "The :color :animal :action over the :adjective :plant."
#
# You should define a list of at least 10 templates. Be creative!

# Your app should begin by selecting a random template. Then, for each word
# that begins with a colon in the template, prompt the user for a word
# that fits the description. Make sure that their input is between 1 and 30
# characters long, to prevent them from making too much of a mess of things.

# After the user has filled in all of the words, print the completed
# template with the user's words filled in. Then after a blank line, print
# a line crediting the author of the template. Then, print a couple of blank
# lines and ask them if they want to play again. If they say "yes" (or "sí"
# or "oui") or any acceptable version of an affirmative answer, start over
# with a new random template. Otherwise, say "no", print "Thanks for playing!"
# and exit the program.

# Here are some constraints:

#   1. The templates should be a list of dictionaries, in which each entry
#      has a "text" fields and an "author" field. The "text" field should
#      contain the template string, and the "author" field should contain
#      the name of the person who wrote the template.
#
#   2. The possible "yes" answers should be stored in a set.
import random
templates = [
    {"text": "My :adjective :animal learned how to :verb a :noun!", "author": "Seth Klein"},
    {"text": "The :color :animal :action over the :adjective :plant.", "author": "Jane Doe"},
    {"text": "A :adjective :noun danced with a :color :animal.", "author": "John Smith"},
    {"text": "The :noun was :adverb :verb by the :color :adjective.", "author": "Emily Davis"},
    {"text": "In the :place, a :color :animal was :verb with a :noun.", "author": "Michael Brown"},
    {"text": "The :adjective :noun jumped over the :color fence.", "author": "Sarah Wilson"},
    {"text": "A :color :animal and a :adjective :noun went to the :place.", "author": "David Johnson"},
    {"text": "The :noun was so :adjective that it made everyone laugh.", "author": "Laura Lee"},
    {"text": "A :color balloon floated over the :adjective garden.", "author": "Chris Martin"},
    {"text": "The :animal danced gracefully under the :color sky.", "author": "Pat Taylor"},
    {"text": "A :noun and a :adjective friend played in the park.", "author": "Kimberly Clark"}
]
while True:
    print("Welcome to the Mad Libs game!")
    template = random.choice(templates)
    word = input(f"Fill in the word for the template: {template['text']}\n")
    word = word.strip().lower()
    if len(word) < 1 or len(word) > 30:
        print("Invalid input. Please enter a word between 1 and 30 characters.")
        continue
    for key in template['text'].split():
        if key.startswith(':'):
            template['text'] = template['text'].replace(key, word, 1)
    print(f"Completed template: {template['text']}")
    print(f"Author: {template['author']}")
    play_again = input("Do you want to play again? (yes/no)\n").strip().lower()
    if play_again not in {"yes", "sí", "oui"}:
        print("Thanks for playing!")
        break
