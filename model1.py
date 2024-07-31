response_dict={
    "Hello":"Hi there! How can I help you today",
    "Weather":"The weather today is clear",
    "news":"Demonstrations in kenya still ongoing"
}

def get_response(user_input):
    user_input=user_input.lower()
    for keyword in response_dict:
        if keyword in response_dict:
            return response_dict[keyword]
        else:
            return "I'm sorry. I don't understand that.Can you rephrase?"
def chat():
    print("Hi! I am your assistant. Type 'bye' to exit")
    while True:
        user_input=input("You: ")
        if user_input.lower()=="bye":
            print("AI:Goodbye")
            break
        else:
            response=get_response(user_input)
            print(f"AI:{response}")
chat()

