import openai
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def create_assistant():
    """Define the assistant and test a response using the ChatCompletion endpoint."""
    
    # Define the role and purpose of the assistant
    messages = [
        {"role": "system", "content": "You are an AI assistant for an e-commerce store. Your job is to help users with product queries."},
        {"role": "user", "content": "Tell me about your purpose."}
    ]

    # Call the ChatCompletion endpoint
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Specify the chat model
        messages=messages,  # Pass the conversation context
        max_tokens=150,  # Limit the response length
        temperature=0.7  # Control randomness
    )
    
    # Return the assistant's response
    return response['choices'][0]['message']['content']


# Load the product catalog from the JSON file
def load_catalog():
    with open("app/products.json", "r") as f:
        return json.load(f)

# Get product details by name
def getProductInfo(product_name):
    catalog = load_catalog()
    for product in catalog:
        if product["name"].lower() == product_name.lower():
            return product
    return "Product not found."

# Check product stock availability
def checkStock(product_name):
    catalog = load_catalog()
    for product in catalog:
        if product["name"].lower() == product_name.lower():
            if product["stock"] > 0:
                return f"{product_name} is available."
            else:
                return f"{product_name} is out of stock."
    return "Product not found."


# Test the function
if __name__ == "__main__":
    print(load_catalog())
    print(getProductInfo("Gaming Mouse"))
    print(checkStock("Smart Watch"))
