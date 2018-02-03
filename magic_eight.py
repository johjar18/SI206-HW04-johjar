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





ask_question()
