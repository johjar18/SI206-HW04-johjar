import random


def ask_question():
    tof= False
    while tof is False:
        question_response= input("What is your question?")
        if question_response== 'quit':
            tof= True
            break

        elif '?' in question_response:
            pass
        else:
            print("I can only answer questions!")


def pick_answer():
    random.randint(0, 19)
    answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again",
               "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
ask_question()
