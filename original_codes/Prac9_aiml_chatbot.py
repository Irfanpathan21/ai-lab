# =====================================================================
# PRACTICAL 9: AIML CHATBOT
# 4-STEP FRAMEWORK (Hinglish Guide)
# Goal: AIML (Artificial Intelligence Markup Language) rule-based
#       knowledge file ko load karke student ke questions ka answer dena.
# =====================================================================

# pyrefly: ignore [missing-import]
import aiml

# STEP 1: CHATBOT ENGINE BANANA
# aiml.Kernel() chatbot ka core brain hota hai.
bot = aiml.Kernel()

# STEP 2: KNOWLEDGE BASE LOAD KARNA (.aiml file)
# 'college.aiml' file me patterns (<pattern>) aur unke answers (<template>) hote hain.
bot.learn("college.aiml")

print("=" * 45)
print("Welcome to College Inquiry Chatbot!")
print("Type 'bye' or 'exit' to quit the chat.")
print("=" * 45)

# STEP 3: CONVERSATION LOOP (User se baat karne ka loop)
while True:
    # Q1. User ka question lena
    user_input = input("\nYou: ").strip()

    # Q3. STOPPING CONDITION: Kab chat band karni hai?
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day ahead!")
        break

    # Q4. RESPONSE GENERATION: AIML rules ke basis par reply nikaalna
    response = bot.respond(user_input)

    # Agar AIML file me koi pattern match nahi hua to default fallback reply
    if not response:
        response = "Sorry, I do not have information about that. Please ask about college courses, admission, or timings."

    print("Bot:", response)
