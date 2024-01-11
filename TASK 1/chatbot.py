import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Rule-based responses
def respond_to_greeting():
    return "Hello! How can I assist you today?"

def respond_to_goodbye():
    return "Goodbye! Have a great day!"

def respond_to_thanks():
    return "You're welcome! If you have more questions, feel free to ask."

def respond_to_default():
    return "I'm not sure how to respond to that. If you have a specific question, feel free to ask!"

# Advanced chatbot function
def advanced_chatbot(user_input):
    # Process user input with spaCy
    doc = nlp(user_input)

    # Extract entities (for future enhancements)
    entities = [ent.text for ent in doc.ents]

    # Analyze the user's intent based on the parsed input
    if any(token.text.lower() in ["hello", "hi", "hey"] for token in doc):
        return respond_to_greeting()

    elif any(token.text.lower() in ["bye", "goodbye"] for token in doc):
        return respond_to_goodbye()

    elif any(token.text.lower() in ["thanks", "thank", "thank you"] for token in doc):
        return respond_to_thanks()

    else:
        return respond_to_default()

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye!")
        break
    response = advanced_chatbot(user_input)
    print("Chatbot:", response)
