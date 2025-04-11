# silly-Hug!
# Developed my Kaiden Quinart(Kainat Quaderee)
# LICENSE:  Apache License Version 2.0
# a way to get all huggingface models inside sillytavern


from flask import Flask, request, jsonify
from flask_cors import CORS
from hugchat import hugchat
from hugchat.login import Login
from dotenv import load_dotenv
import os
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load environment variables from .env file
load_dotenv()

hf_email = os.getenv("EMAIL")
hf_passwd = os.getenv("PASS")
MODELID= os.getenv("MODELID")

def get_hugchat_response(prompt, email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()

    # Create chatbot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    if MODELID == 0:
        chatbot.switch_llm(0)
    elif MODELID == 1:
        chatbot.switch_llm(1)
    elif MODELID == 2:
        chatbot.switch_llm(2)
    elif MODELID == 3:
        chatbot.switch_llm(3)
    elif MODELID == 4:
        chatbot.switch_llm(4)
    elif MODELID == 5:
        chatbot.switch_llm(5)
    elif MODELID == 6:
        chatbot.switch_llm(6)
    elif MODELID == 7:
        chatbot.switch_llm(7)
    elif MODELID == 8:
        chatbot.switch_llm(8)
    elif MODELID == 9:
        chatbot.switch_llm(9)
    elif MODELID == 10:
        chatbot.switch_llm(10)
    elif MODELID == 11:
        chatbot.switch_llm(11)
    else:
        print("Invalid MODELID")

    chatbot.new_conversation(switch_to=True)

    # Get the response from the chatbot
    message_result = chatbot.chat(prompt)

    # Assuming the message result is a dictionary with a 'text' key
    if isinstance(message_result, dict) and 'text' in message_result:
        return message_result['text']

    # If not, just return the message_result directly (or handle it as needed)
    return str(message_result)  # Convert any non-serializable object to string

@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    data = request.json

    # Extract messages
    messages = data.get("messages", [])
    if not messages:
        return jsonify({"error": "No messages provided."}), 400

    # Concatenate all message contents to form the prompt
    prompt = "\n".join([msg.get("content", "") for msg in messages])

    # Get response from HuggingChat
    response_text = get_hugchat_response(prompt, hf_email, hf_passwd)
    print (response_text)
    response = {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": "hugchat",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": response_text
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
