import requests

def get_chat_response(api_key, endpoint, message):
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    data = {
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }

    try:
        response = requests.post(endpoint, json=data, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def main():
    api_key = "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"
    endpoint = "https://api.openai.com/davinci-oo3/v1/completions"  # Replace with your API endpoint

    print("ChatGPT Chatbot")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = get_chat_response(api_key, endpoint, user_input)
        if response:
            print("ChatGPT:", response)

if __name__ == "__main__":
    main()
