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
    {"text": "My :adjective :animal learned how to :verb a :noun", "author": "Seth Klein"},
    {"text": "I was at the :place when I saw a/an :adjective :noun that made me :verb with :emotion", "author": "Seth Klein"},
    {"text": "Hello Professor :name, I cannot attend today's lecture because I have been trapped in my :room. There is an :adjective :animal between me and the door, and it will not let me leave. :adverb, :name", "author": "Seth Klein"},
    {"text": "The camping trip was great! I hiked through a :adjective forest and got to :verb in a lake, but I lost my :noun.", "author": "Seth Klein"},
    {"text": "Today I saw a/an :animal for the first time and it wasn't what I expected. It was :adjective and was :verb-ing.", "author": "Seth Klein"},
    {"text": "I just crushed a fitness goal. I :past-tense-verb around the :place and past the :noun too!", "author": "Seth Klein"},
    {"text": "I have a phobia of :plural-noun. If I saw one, I'd :verb away. It makes me feel so :emotion.", "author": "Seth Klein"},
    {"text": "It's not easy owning a/an :animal. They can be :adjective and you always have to :verb after them.", "author": "Seth Klein"},
    {"text": "The prices of :plural-noun are outrageous! I bought :number of the :adjective one(s) for the price of $:number!", "author": "Seth Klein"},
    {"text": "I spend too much :verb-ing. It takes a/an :adjective amount of my time, especially since I always commute to the :place to do it.", "author": "Seth Klein"}
]
yes_responses = ("yes", "y", "sí", "oui", "ok")

def get_input(p):
    while True:
        user_input = input(p).strip()
        if len(user_input) >= 1 and len(user_input) <= 30:
            return user_input
        else:
            print("Input must be between 1 and 30 characters. Please try again.")

def fill_template(template):
    placeholders = [word[1:] for word in template.split() if word.startswith(":")]
    placeholders = [word[:-1] if word[-1] in ".,!?;" else word for word in placeholders]
    
    user_inputs = {}

    for placeholder in placeholders:
        user_inputs[placeholder] = get_input(f"Enter a(n) {placeholder}: ")

    for placeholder, user_input in user_inputs.items():
        template = template.replace(f":{placeholder}", user_input)

    return template

while True:
    template_entry = random.choice(templates)
    template = template_entry["text"]
    author = template_entry["author"]

    print("Welcome to Mad Libs!")
    print("Fill in the following words:")

    template = fill_template(template)
    print("Here's your completed story:\n")
    print(template)

    print(f"- {author}\n\n")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again not in yes_responses:
        print("Thanks for playing!")
        break