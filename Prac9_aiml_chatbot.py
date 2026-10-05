# =====================================================================
# PRACTICAL 9: AIML CHATBOT
# ---------------------------------------------------------------------
# UNIVERSAL TEMPLATE: Rule-Based Conversational Agent using AIML
# CORE CONCEPT:
#   AIML (Artificial Intelligence Markup Language) matches user patterns:
#     <category>
#       <pattern>HELLO</pattern>
#       <template>Hello! How can I help you?</template>
#     </category>
#
# EXAM ADAPTATION GUIDE (How to use this template for other questions):
#   - To add new question/answer: Add a <category> block to 'college.aiml'.
#   - Python 3 Compatibility Fix: `time.clock = time.perf_counter` ensures
#     the legacy aiml library runs on modern Python (3.8+).
#   - If AIML library is NOT available in exam: Use Python Dictionary fallback:
#       `faq = {"hi": "Hello!", "courses": "We offer CS & IT."}`
#       `reply = faq.get(user_input.lower(), "Sorry, I don't know.")`
# =====================================================================

import time
time.clock = time.perf_counter  # Fix for Python 3.8+ compatibility

# pyrefly: ignore [missing-import]
import aiml

# 1. Initialize AIML Kernel & Load Knowledge Base (.aiml file)
bot = aiml.Kernel()
bot.learn("college.aiml")

print("=" * 45)
print("College Inquiry Chatbot Ready! (Type 'bye' to exit)")
print("=" * 45)

# 2. Universal Chatbot Loop
while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break

    # Match pattern and retrieve template response
    response = bot.respond(user_input)

    # Fallback if no pattern matched
    if not response:
        response = "Sorry, I only have info on college timings, courses, and admissions."

    print("Bot:", response)
