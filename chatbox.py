#Simple Rule-Based Chatbot for Codesoft AI Internship
print("Chatbot started! Type 'exit' to stop.")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input:
        print("Chatbot: Hello! How can I assist you today?")

    elif "how are you" in user_input:
        print("Chatbot: I'm doing well, thank you for asking!")

    elif "name" in user_input:
        print("Chatbot: I am a simple rule-based chatbot created for CodSoft AI Internship.")

    elif "exit" in user_input:
        print("Chatbot: Goodbye! Have a great day!")
        break

    else:
        print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")