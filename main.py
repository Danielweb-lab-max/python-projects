import json  # Import the json module to handle JSON data
from difflib import get_close_matches  # Import get_close_matches to find close matches for user input

def getKnowledgeBase(filepath):
    # Open the JSON file in read mode
    with open(filepath, 'r') as file:
        # Load the data from the file
        data = json.load(file)
    # Return the data
    return data

def addDataToKnowledgeBase(filepath, data):
    # Open the JSON file in write mode
    with open(filepath, 'w') as file:
        # Dump the data into the file with an indentation of 2 spaces
        json.dump(data, file, indent=2)

def findBestMatches(userInput, questions):
    # Find the closest matches to the user input from the list of questions
    matches = get_close_matches(userInput, questions, n=1, cutoff=0.6)
    # Return the best match if it exists, otherwise return None
    return matches[0] if matches else None

def getAnswerForQuestion(question, knowledgeBase):
    # Iterate through the questions in the knowledge base
    for q in knowledgeBase['questions']:
        # If the question matches, return the corresponding answer
        if q['question'] == question:
            return q['answer']

def chatBot():
    # Load the knowledge base from the JSON file
    knowledgeBase = getKnowledgeBase('knowledge_base.json')
    while True:
        # Prompt the user for input
        userInput = input("You: ")
        # If the user types "quit", exit the loop
        if userInput.lower() == "quit":
            break
        # Find the best match for the user input from the questions in the knowledge base
        bestMatch = findBestMatches(userInput, [q["question"] for q in knowledgeBase['questions']])
        if bestMatch:
            # If a match is found, get the corresponding answer and print it
            answer = getAnswerForQuestion(bestMatch, knowledgeBase)
            print(f'Bot: {answer}')
        else:
            # If no match is found, prompt the user to teach the bot a new answer
            print("Bot: I do not know the answer. Can you teach me?")
            new_answer = input("Type answer or 'skip' to skip: ")
            if new_answer.lower() != 'skip':
                # If the user provides an answer, add the new question and answer to the knowledge base
                knowledgeBase["questions"].append({"question": userInput, "answer": new_answer})
                # Save the updated knowledge base to the JSON file
                addDataToKnowledgeBase('knowledge_base.json', knowledgeBase)
                print("Bot: Thank you, I learned something new")

# If the script is run directly, start the chatbot
if __name__ == '__main__':
    chatBot()
