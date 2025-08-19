responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "hey": "Hey! What's up?",
    "how are you": "I'm doing great, thank you! How about you?",
    "i'm fine": "Glad to hear that!",
    "who are you": "I'm a simple chatbot made in Python.",
    "what is your name": "You can call me ChatBot.",
    "what can you do": "I can respond to simple messages and help you learn Python.",
    "tell me a joke": "Why don’t programmers like nature? It has too many bugs.",
    "thanks": "You're welcome!",
    "thank you": "No problem!",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "See you later!",
    "what time is it": "I'm not wearing a watch, but Python can help with that!",
    "what is python": "Python is a powerful, easy-to-learn programming language.",
    "help": "You can say things like 'hi', 'how are you', 'tell me a joke', or 'bye'.",
    "do you like music": "I don't have ears, but I hear Python is music to many developers' code.",
    "how old are you": "I'm timeless — created just now, actually.",
    "who created you": "I was written by a Python programmer for educational purposes.",
    "are you real": "I'm as real as your imagination!"
}

print("Welcome to the Python ChatBot!")
print("You can ask me questions like:")

for question in responses:
    print("•", question)

print("\nType your message below (type 'bye' or 'goodbye' to exit):")

while True:
    message = input("You: ").strip().lower()

    if message in responses:
        print("Bot:", responses[message])
        if message in ["bye", "goodbye"]:
            break
    else:
        print("Bot: I'm not sure how to respond to that.")