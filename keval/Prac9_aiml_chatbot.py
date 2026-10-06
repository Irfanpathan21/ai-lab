import aiml

# Create chatbot
bot = aiml.Kernel()

# Load AIML knowledge base
bot.learn("college.aiml")

print("College Chatbot")
print("Type 'bye' to exit.")
print("Name:- Keval Doshi")
print("SAP ID:- 53013240009")

while True:

    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot:", bot.respond(user_input))
        break

    response = bot.respond(user_input)

    # Default response if knowledge is not available
    if response == "":
        response = "Sorry, I don't have information about that."

    print("Bot:", response)
