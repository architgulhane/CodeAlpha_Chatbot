import random

responses = {
    "hi": ["Hello!", "Hey there!", "Hi!"],
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a bot, but I'm doing fine. How can I help you?", "Doing well, thank you! How can I assist?"],
    "bye": ["Goodbye! Have a great day!", "See you later!", "Bye!"],
    "default": ["Sorry, I don't understand that.", "Can you rephrase that?", "I'm not sure I get you."]
}

def chatbot():
    print("ChatBot: Hi! Type something to start a conversation (type 'exit' to quit)")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("ChatBot: Bye!")
            break
        response_list = responses.get(user_input, responses["default"])
        response = random.choice(response_list)
        print("ChatBot:", response)

if __name__ == "__main__":
    chatbot()
