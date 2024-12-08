
# ShopBot - AI E-Commerce Assistant

ShopBot is an AI-powered assistant for e-commerce platforms. It uses OpenAI's GPT-4 to provide users with information about products, including availability and details, through a simple and interactive web interface.

## Features
- Retrieve product details from a JSON-based catalog.
- Check product stock availability.
- Continuous conversation with AI.
- Simple and user-friendly web interface.

---

## How It Works

The application is designed using Flask for the backend and HTML/CSS/JavaScript for the frontend. It interacts with OpenAI's API to provide intelligent responses to user queries about products in an e-commerce catalog.

### Workflow
1. **User Interaction**:
   - The user types a query into the chat interface (e.g., "Tell me about the EcoFriendly Water Bottle").
   - The input is sent to the Flask server via a POST request.

2. **Processing User Queries**:
   - The Flask server receives the input and appends it to a chat history (maintained in memory).
   - The server uses the OpenAI API with the GPT-4 model to analyze the query.

3. **Function Calls**:
   - OpenAI decides if it needs to call a predefined function (e.g., `getProductInfo` or `checkStock`) to fetch details from the product catalog.
   - If a function call is invoked, the Flask server processes the call and retrieves the required information from the catalog (`products.json`).

4. **Response**:
   - The AI's response, including function results if applicable, is sent back to the user and displayed in the chat interface.

5. **Continuous Interaction**:
   - The process repeats, maintaining context from previous messages for a seamless conversation.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (you can get one from [OpenAI](https://platform.openai.com/signup/))

### Steps
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   # Windows
   .\env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenAI API key:
   - Create a `.env` file in the root directory.
   - Add the following line to the `.env` file:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     ```

---

## Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000
   ```

---

## Project Structure

```plaintext
├── app/
│   ├── app.py                       # Flask application
│   ├── openai_integration.py        # OpenAI interaction functions
│   ├── products.json                # Product catalog
│   └── static/                      # Static files (CSS, JS, images)
│       ├── css/
│       │   └── styles.css           # Styling for the interface
│       └── js/
│           └── scripts.js           # JavaScript for handling chat
│   └── templates/                   # HTML templates
│       └── index.html               # Main UI
├── .env                             # API key file
├── requirements.txt                 # Python dependencies
├── README.md                        # Documentation
```

---

## Key Functions

### Backend (Flask)
- **`create_assistant(messages)`**:
   - Connects to OpenAI API to handle user input and generate responses.
   - Supports function calling to retrieve product details or check stock availability.

- **`getProductInfo(productName)`**:
   - Searches the JSON-based product catalog for details about a specific product.

- **`checkStock(productName)`**:
   - Checks if a specific product is available in stock.

### Frontend (HTML/JavaScript)
- **Dynamic Chat Interface**:
   - Users can type messages, and responses are displayed in a real-time chat box.
   - Input is sent to the backend via AJAX requests using `fetch`.

---

## Usage

1. Type your query into the input box (e.g., "Tell me about the EcoFriendly Water Bottle").
2. The assistant will respond with relevant information from the product catalog.
3. Continue the conversation as needed. To stop, simply close the browser.

---

## Dependencies
- Flask
- OpenAI Python SDK
- Python-dotenv

Install these dependencies with:
```bash
pip install -r requirements.txt
```

---

## Example Interaction

### User Query
```
Tell me about the EcoFriendly Water Bottle.
```

### Assistant Response
```
Product: EcoFriendly Water Bottle
Description: A reusable water bottle made from eco-friendly materials.
Price: $19.99
Stock: Available
```

---

## Troubleshooting

### Common Issues
- **API Key Error**:
   Ensure your `.env` file contains the correct API key for OpenAI.

- **Dependencies Not Found**:
   Run `pip install -r requirements.txt` again to ensure all packages are installed.

- **Server Not Running**:
   Ensure your virtual environment is active and run `python app.py`.

---

## License
This project is for demonstration purposes only. Contact the author for licensing information.
