from flask import Flask, request, jsonify, render_template
from openai_integration import create_assistant

app = Flask(__name__)

# Initialize the message history
messages = [{"role": "system", "content": "You are an AI assistant for an e-commerce store."}]

@app.route("/")
def index():
    """Render the chat interface."""
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Handle user input and return AI response."""
    global messages
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Append user input to messages
    messages.append({"role": "user", "content": user_input})

    # Get assistant response
    updated_messages, response = create_assistant(messages)
    messages = updated_messages

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
