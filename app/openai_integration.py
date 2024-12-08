import openai
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the product catalog from JSON
def load_catalog():
    """Loads the product catalog from a JSON file."""
    with open("app/products.json", "r") as f:
        return json.load(f)

# Function to retrieve product information
def getProductInfo(productName):
    """Retrieve product details by name."""
    catalog = load_catalog()
    for product in catalog:
        if productName.lower() in product["name"].lower():
            return {
                "id": product["product_id"],
                "name": product["name"],
                "description": product["description"],
                "price": product["price"],
                "stock": product["stock"]
            }
    return {"error": "Product not found."}

# Function to check stock availability
def checkStock(productName):
    """Check if a product is in stock."""
    product = getProductInfo(productName)
    if "error" in product:
        return {"error": "Product not found."}
    return {"name": product["name"], "in_stock": product["stock"] > 0}

# Function to process function calls from OpenAI
def process_function_call(function_call):
    """Handle the function call and return results."""
    function_name = function_call.get("name")
    arguments = json.loads(function_call.get("arguments", "{}"))

    if function_name == "getProductInfo":
        return getProductInfo(arguments.get("productName", ""))
    elif function_name == "checkStock":
        return checkStock(arguments.get("productName", ""))
    else:
        return {"error": "Function not supported."}

# Main assistant logic
def create_assistant(messages):
    """Create an AI assistant that can interact with product data."""

    # Define the functions schema
    functions = [
        {
            "name": "getProductInfo",
            "description": "Retrieve product details by name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "productName": {"type": "string", "description": "The name of the product to retrieve details for."}
                },
                "required": ["productName"]
            }
        },
        {
            "name": "checkStock",
            "description": "Check if a product is in stock.",
            "parameters": {
                "type": "object",
                "properties": {
                    "productName": {"type": "string", "description": "The name of the product to check stock for."}
                },
                "required": ["productName"]
            }
        }
    ]

    # Call the OpenAI ChatCompletion endpoint
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        functions=functions,
        function_call="auto"
    )

    # Handle function calls
    message = response["choices"][0]["message"]
    if "function_call" in message:
        function_call = message["function_call"]
        function_result = process_function_call(function_call)
        messages.append({"role": "assistant", "content": f"Function Result: {function_result}"})
        return messages, f"Function Result: {function_result}"

    # Append and return assistant response
    messages.append({"role": "assistant", "content": message.get("content", "No response.")})
    return messages, message.get("content", "No response.")

# Chat loop
def chat_with_assistant():
    """Allows continuous chat with the assistant."""
    print("Welcome to ShopBot! You can ask about products or type 'exit' to end the conversation.")
    
    # Initialize chat history
    messages = [{"role": "system", "content": "You are an AI assistant for an e-commerce store."}]
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("ShopBot: Goodbye! Have a great day!")
            break
        
        # Append user input to messages
        messages.append({"role": "user", "content": user_input})
        
        # Get assistant response
        messages, response = create_assistant(messages)
        print(f"ShopBot: {response}")

