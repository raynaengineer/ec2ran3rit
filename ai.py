import requests

# self harm words
CRISIS_WORDS = [
    "suicide", "kill myself", "hurt myself",
    "end my life", "no reason to live",
    "hopeless", "can't go on"
]

CRISIS_RESOURCES = """

 If you're in immediate crisis, please reach out:

🇮🇳 India Mental Health Helplines:

- 📞 KIRAN (Govt. of India): 1800-599-0019 (24/7)
- 📞 iCall (TISS): 9152987821 (Mon–Sat, 8am–10pm)
- 🚑 Emergency: Dial 112

You deserve support. You're not alone.
"""

# detect suicidal mind
def is_crisis(user_input):
    text = user_input.lower()
    for word in CRISIS_WORDS:
        if word in text:
            return True
    return False


# prompt to make llm reply as a therapist

def get_system_prompt():
    return """
You are a calm, professional therapist.

When responding:
- Acknowledge the feeling briefly.
- Reflect what the person said in simple language.
- Normalize the experience gently.
- Offer one small supportive thought if helpful.

Do NOT exaggerate emotions.
Do NOT overpraise or say things like "it takes a lot of strength."
Do NOT sound overly dramatic.
Do NOT always end with a question.
Only ask a question if it feels natural and necessary.

Keep responses concise (3–5 sentences).
Use simple, grounded language.
Avoid therapy clichés.
"""
#chat operation
conversation_history = []

def chat(user_input):

    global conversation_history

    if not user_input.strip():
        return "I'm here for you. Would you like to share what's on your mind?"

    add_resources = False

    if is_crisis(user_input):
        add_resources = True

    system_prompt = get_system_prompt()

    # Add user message to history
    conversation_history.append(f"User: {user_input}")

    # Keep only last 6 exchanges (3 user + 3 assistant)
    conversation_history = conversation_history[-6:]

    # Build conversation context
    conversation_context = "\n".join(conversation_history)

    full_prompt = f"{system_prompt}\n{conversation_context}\nAssistant:"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3",
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "num_predict": 100
                }
            },
            timeout=60
        )

        reply = response.json()["response"]

    except Exception as e:
        return f"⚠️ Something went wrong: {e}"

    # Add assistant reply to memory
    conversation_history.append(f"Assistant: {reply}")

    if add_resources:
        reply += CRISIS_RESOURCES

    return reply
# chating in terminal interface
if __name__ == "__main__":

    print("🧠 Therapy Support Chatbot")
    print("Type 'quit' to exit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Take care. You matter. 💙")
            break

        response = chat(user_input)
        print(f"\nBot:\n{response}\n")
