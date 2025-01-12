import nltk
import spacy
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data
nltk.download('punkt')

# Load Spacy's small English model
nlp = spacy.load('en_core_web_sm')

# Define an expanded set of conversation pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello, how can I help you?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created using NLTK and Spacy. How can I assist you?",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How can I assist you today?",]
    ],
    [
        r"what can you do?",
        ["I can help answer your questions, provide information, and have a friendly chat with you.",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!",]
    ],
    [
        r"what is natural language processing?",
        ["Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language.",]
    ],
    [
        r"what is spacy?",
        ["Spacy is an open-source software library for advanced natural language processing in Python.",]
    ],
    [
        r"who created you?",
        ["I was created using NLTK and Spacy by a developer who loves working with natural language processing.",]
    ],
    [
        r"what is your purpose?",
        ["My purpose is to assist you with your questions and have a friendly conversation with you.",]
    ],
    [
        r"tell me a fun fact",
        ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",]
    ],
    [
        r"what is the weather like today?",
        ["I'm not connected to a live weather service, but you can check the current weather on your favorite weather website or app.",]
    ],
    [
        r"quit",
        ["Goodbye! Have a nice day!",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't have an answer for that. Can you ask something else?",]
    ],
]

# Initialize the chatbot with pairs and reflections
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def chat():
    print("Hi, I'm a chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Bot: Goodbye! Have a nice day!")
            break
        
        # Process user input using Spacy
        doc = nlp(user_input)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        print("Entities:", entities)  # Debug print
        
        response = chatbot.respond(user_input)
        print("Bot:", response)

# Main function to run the chatbot
if __name__ == "__main__":
    chat()
