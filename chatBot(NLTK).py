import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import numpy as np

nltk.download('punkt')
nltk.download('wordnet')


lemmatizer = WordNetLemmatizer()

faq_data = {
    "do you offer delivery": "Yes, we offer home delivery within 5 km.",
    "what are your opening hours": "We’re open from 8 AM to 10 PM every day.",
    "do you have gluten free options": "Yes, we have gluten-free bread and cookies.",
    "where is your bakery located": "We’re located at 123 Main Street, Cairo.",
    "what payment methods do you accept": "We accept cash, credit cards, and mobile payments."
}

def preprocess(text):
    tokens = word_tokenize(text.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmas

def get_response(user_input):
    user_tokens = set(preprocess(user_input))
    best_match = None
    best_score = 0

    for question, answer in faq_data.items():
        question_tokens = set(preprocess(question))
        common_words = user_tokens & question_tokens
        score = len(common_words)

        if score > best_score:
            best_score = score
            best_match = answer

    if best_score == 0:
        return "Sorry, I didn't understand your question. Could you rephrase it?"
    else:
        return best_match


print("Welcome to the Bakery Bot! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    response = get_response(user_input)
    print("Bot:", response)
