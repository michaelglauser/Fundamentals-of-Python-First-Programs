#Python Programs Chapter 5 Project 10
#Conversations often shift focus to earlier topics. Modify the therapist program to support this capability.
#Add each patient input to a history list. Then, occasionally choose an element at random from this list, change persons, and prepend (add at the beginning) the qualifier “Earlier you said that” to this reply.
#Make sure that this option is triggered only after several exchanges have occurred.


import random
history = []
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
    probability = random.randint(1, 4)
    if probability in (1,2):
        return random.choice(hedges)
    elif probability == 3 and len(history) > 3:
        return "Let's circle back to something you said earlier." + change_person(random.choice(history))
    else:
        history.append(sentence)
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