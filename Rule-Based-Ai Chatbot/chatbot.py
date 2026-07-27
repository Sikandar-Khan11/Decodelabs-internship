# ----------------------------------------
# Project 1: Rule-Based AI Chatbot
# ----------------------------------------

print("=" * 45)
print("      Welcome to Rule-Based AI Chatbot")
print("=" * 45)

while True:

    user = input("\nYou: ").lower()

    # Greetings
    if user == "hi" or user == "hello" or user == "hey":
        print("Bot: Hello! How can I help you?")

    # Asking about chatbot
    elif user == "what is your name":
        print("Bot: My name is RuleBot.")

    elif user == "how are you":
        print("Bot: I am fine. Thank you for asking!")

    elif user == "who made you":
        print("Bot: I was created using Python.")

    elif user == "help":
        print("Bot: You can greet me or ask simple questions.")

    elif user == "thanks":
        print("Bot: You're welcome!")

    # Exit
    elif user == "bye" or user == "exit" or user == "quit":
        print("Bot: Goodbye! Have a great day.")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that.")