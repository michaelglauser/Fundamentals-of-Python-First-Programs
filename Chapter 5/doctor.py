#Python Programs Chapter 5 Project 9
#In Case Study: Nondirective Psychotherapy, when the patient addresses the therapist personally, the therapist’s reply does not change persons appropriately. To see an example of this problem, test the program with “you are not a helpful therapist.”
#Fix this problem by repairing the dictionary of replacements.


import random

hedges = (
    "Please tell me more.",
    "Many of my patients tell me the same thing.",
    "Please continue."
)
qualifiers = (
    "Why do you say that?",
    "You seem to think that?",
    "Can you explain why? "
    "Let's circle back to something you said earlier."
)
replacements = {"I": "you", "me": "you", "my": "your", "we": "you", "us": "you", "mine": "yours",
                "you": "I", "you": "me", "my viewpoint": "your viewpoint", "your": "my", "yours": "mine"}


def reply(sentence):
    response = random.randint(1, 4)
    if response == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + change_person(sentence)


def change_person(sentence):
    words = sentence.split()
    reply_words = []
    for word in words:
        reply_words.append(replacements.get(word, word))
    return " ".join(reply_words)


def main():
    print("Good morning. \nI hope you are well today.\nWhat can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        if sentence.upper() == "You are not a helpful therapist.":
            print("I'm sorry that I am unable to help you.")
            break
        print(reply(sentence))

if __name__ == "__main__":
    main()
