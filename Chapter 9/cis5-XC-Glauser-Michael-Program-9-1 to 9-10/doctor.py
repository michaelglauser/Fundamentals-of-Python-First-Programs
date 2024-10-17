#Python Programs Chapter 9 Project 5
#Restructure the Doctor program, described in Chapter 5, according to the model/view pattern, so that these areas of responsibility are assigned to separate sets of classes.


import random

history = []

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")

qualifiers = ("Why do you say that? ",
              "You seem to think that? ",
              "Can you explain why? ")

replacements = {"I": "you", "me": "you", "my": "your", "we": "you", "us": "you", "mine": "yours",
                "you": "I", "you": "me", "my viewpoint": "your viewpoint", "your": "my", "yours": "mine"}


class Doctor:
    def __init__(self):
        pass

    def greeting(self):
        return "Good morning. \nI hope you are well today.\nWhat can I do for you?"

    def farewell(self):
        return "Have a nice day!"

    def reply(self, sentence):

        replyToPatientStrategy = random.randint(1, 5)
        if replyToPatientStrategy in (1, 2):
            answer = random.choice(hedges)
        elif replyToPatientStrategy == 3 and len(history) > 3:
            answer = "Let's circle back to something you said earlier." + \
                     change_person(random.choice(history))
        else:
            answer = random.choice(qualifiers) + change_person(sentence)

        history.append(sentence)
        return answer

def change_person(sentence):
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)

def main():
    doctor = Doctor()
    print(doctor.greeting())
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(doctor.farewell())
            break
        print(doctor.reply(sentence))

if __name__ == "__main__":
    main()