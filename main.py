import streamlit as st
import random
import wikipedia

st.set_page_config(page_title="Smart Chatbot", page_icon="🤖")
st.title("🤖 Conversational ChatBot")

# --- Chat history ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Clear history button ---
if st.button("🗑️ Clear Chat History"):
    st.session_state.chat_history = []
    st.rerun()

# --- Chatbot logic ---
def get_response(user_input):
    user_input = user_input.strip().lower()

    # Arithmetic operations
    try:
        result = eval(user_input, {"__builtins__": None}, {})
        if isinstance(result, (int, float, bool)):
            return f"The result is: {result}"
    except:
        pass

    # Logic-based responses
    logical_answers = {
        "true and true": "True",
        "true and false": "False",
        "false and true": "False",
        "false and false": "False",
        "true or true": "True",
        "true or false": "True",
        "false or true": "True",
        "false or false": "False",
        "not true": "False",
        "not false": "True"
    }
    if user_input in logical_answers:
        return logical_answers[user_input]

    # Conversational responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm functioning well. How about you?"
    elif "your name" in user_input:
        return "I'm a smart chatbot built with Streamlit."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Try a math question or logic expression!"

# --- Extra Features Handler ---
def handle_extra_features(user_input):
    # Joke Generator
    if "tell me a joke" in user_input:
        jokes = [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why was the math book sad? Because it had too many problems.",
            "Parallel lines have so much in common… it’s a shame they’ll never meet."
        ]
        return random.choice(jokes)

    # Weather Mock
    elif "weather" in user_input:
        # Simulate weather (can integrate real API if needed)
        return "Today's weather is sunny with a high of 28°C and a low of 18°C. ☀️"

    # Wikipedia Search
    elif "search wikipedia for" in user_input:
        try:
            query = user_input.replace("search wikipedia for", "").strip()
            summary = wikipedia.summary(query, sentences=2)
            return f"📚 Here's what I found about *{query}*:\n\n{summary}"
        except Exception as e:
            return "Sorry, I couldn't find that on Wikipedia."

    return None  # no match

# --- Input box ---
user_input = st.text_input("You:", placeholder="Ask me something... (e.g. 5 + 3 * 2, not true, hello)")

# --- Process input ---
if user_input:
    extra_response = handle_extra_features(user_input.lower())
    if extra_response:
        bot_response = extra_response
    else:
        bot_response = get_response(user_input)

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

# --- Display conversation ---
for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")

# --- Suggested questions ---
with st.expander("💡 Suggestions to try"):
    st.markdown("""
### 🤖 Basic Conversation
- `Hi`
- `How are you?`
- `What's your name?`
- `Bye`

### ➕ Arithmetic
- `5 + 3 * 2`
- `10 / 2`
- `100 - 37`

### 🧠 Logic
- `not false`
- `true and false`
- `false or true`

### 🎭 Fun Features
- `Tell me a joke`
- `What's the weather today?`
- `Search Wikipedia for Python`
- `Search Wikipedia for Artificial Intelligence`
""")