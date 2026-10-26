#create a simple chatbot using python
import random

responses = [
    "Hello! How can I help you today?",
    "Hi there! What's on your mind?",
    "Hey! What can I do for you?",
    "Greetings! How may I assist you?"
]

def get_response(user_input):
    return random.choice(responses)
print("Welcome to the Simple Chatbot! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)