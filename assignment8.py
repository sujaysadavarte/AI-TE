"""B4: Simple rule-based chatbot using predefined responses and pattern matching."""
import re
 
# (regex pattern, response). Word boundaries avoid false matches such as
# "hi" inside "this" or "which".
RULES = [
    (r"\b(bye|exit)\b", "Goodbye! Have a nice day."),
    (r"\b(hello|hi|hey)\b", "Hello! How can I help you?"),
    (r"\bhow are you\b", "I am fine. Thank you!"),
    (r"\bwhat is (ai|artificial intelligence)\b",
     "AI stands for Artificial Intelligence."),
    (r"\b(your name|who are you)\b", "I am a simple rule-based AI chatbot."),
    (r"\bhelp\b", "I can answer basic predefined questions."),
]
DEFAULT = "Sorry, I don't understand your question."
 
 
def chatbot_response(user_input):
    text = user_input.lower().strip()
    for pattern, response in RULES:
        if re.search(pattern, text):
            return response
    return DEFAULT
 
 
def is_goodbye(user_input):
    return re.search(r"\b(bye|exit)\b", user_input.lower()) is not None
 
 
if __name__ == "__main__":
    print("Chatbot: Hello! I am a simple AI chatbot.")
    print("Chatbot: Type 'bye' or 'exit' to end the conversation.")
    while True:
        try:
            user_input = input("You: ")
        except EOFError:
            break
        print("Chatbot:", chatbot_response(user_input))
        if is_goodbye(user_input):
            break
