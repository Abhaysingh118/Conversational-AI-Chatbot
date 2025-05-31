
# 🤖 Smart Chatbot with Streamlit

This is a simple yet interactive conversational chatbot built using **Streamlit**. The chatbot can perform arithmetic and logic operations, respond to basic conversation prompts, tell jokes, simulate weather, and fetch summaries from Wikipedia.

## 🚀 Features

- **Conversational Responses**
  - Greets the user
  - Responds to common questions like "What's your name?" or "How are you?"

- **Arithmetic Solver**
  - Understands and evaluates expressions like `5 + 3 * 2`, `100 - 37`, etc.

- **Logic Evaluator**
  - Supports Boolean logic like `true and false`, `not true`, `false or true`, etc.

- **Fun Features**
  - `Tell me a joke` — returns a random tech joke.
  - `What's the weather today?` — returns a mock weather response.
  - `Search Wikipedia for <query>` — fetches a short summary for a given topic.

- **Chat History**
  - Maintains and displays a running chat log.
  - Clear button to reset the conversation.

- **Suggested Questions**
  - Built-in expandable help section to guide users on what to ask.

## 📦 Requirements

- Python 3.x
- Streamlit

Install dependencies using:

```bash
pip install streamlit 
```

## ▶️ Running the App

To run the chatbot locally, use:

```bash
streamlit run app.py
```

## 📁 File Structure

```
smart-chatbot/
├── app.py           # Main chatbot application
└── README.md        # Project documentation
```

## 💡 Examples to Try

```text
Hi
What's your name?
How are you?
Bye
5 + 3 * 2
true or false
not false
Tell me a joke
What's the weather today?
Search Wikipedia for Artificial Intelligence
```

## ✨ Future Improvements

- Integrate real-time weather API (e.g., OpenWeatherMap)
- Add natural language processing (NLP) for better understanding
- Support voice input/output
- Add support for persistent storage of chat history

---

Built with ❤️ using Streamlit.
