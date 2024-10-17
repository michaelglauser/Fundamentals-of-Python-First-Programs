#Python Programs Chapter 5 Project 4
#Make the following modifications to the original sentence-generator program:
#a. The prepositional phrase is optional. (It can appear with a certain probability.)
#b. A conjunction and a second independent clause are optional: The boy took a drink and the girl played baseball.
#c. An adjective is optional: The girl kicked the red ball with a sore foot.
#You should add new variables for the sets of adjectives and conjunctions.

import random

articles = ("A", "AN", "THE")
nouns = ("BOY", "GIRL", "BALL", "FOOT")
verbs = ("DRINK", "SWING", "THROW", "SLIDE", "KICK")
prepositions = ("WITH", "BY")
adjectives = ("RED", "SORE")
conjunctions = ("AND")


def sentence():
    first = independent_clause()
    if random.randint(1, 5) == 1:
        return first + " " + random.choice(conjunctions) + \
            " " + independent_clause()
    else:
        return first


def independent_clause():
    return noun_text() + " " + verb_text()


def noun_text():
    if random.randint(1, 3) == 1:
        adj = random.choice(adjectives) + " "
    else:
        adj = " "
    return random.choice(articles) + " " + adj + random.choice(nouns)


def verb_text():
    if random.randint(1, 3) == 1:
        prep_phrase = " " + prepositional_text()
    else:
        prep_phrase = ""
    return random.choice(verbs) + " " + noun_text() + prep_phrase


def prepositional_text():
    return random.choice(prepositions) + " " + noun_text()


def main():
    number = int(input("Enter the number of sentence :"))
    for count in range(number):
        print(sentence())


if __name__ == "__main__":
    main()
