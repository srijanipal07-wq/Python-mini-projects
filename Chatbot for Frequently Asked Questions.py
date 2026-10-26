print("Welcome to FAQ Chatbot!")

while True:
    question = input("You: ").lower()

    if question == "hello":
        print("Bot: Hello! How can I help you?")

    elif question == "name":
        print("Bot: I am a FAQ chatbot.")

    elif question == "course":
        print("Bot: We offer different courses.")

    elif question == "fees":
        print("Bot: Please contact the college office.")

    elif question == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't know the answer.")