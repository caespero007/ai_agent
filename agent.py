from openai import OpenAI
from dotenv import load_dotenv
from tools import open_youtube

load_dotenv()

client = OpenAI()

tools = [
    {
        "type": "function",
        "name": "open_youtube",
        "description": "Open YouTube in the web browser.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.responses.create(
        model="gpt-5-mini",
        input=user_input,
        tools=tools
    )

    print("AI:", response.output_text)