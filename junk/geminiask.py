from google import genai
import os


def main():
    api_key = "AIzaSyBEy8AvhkZ3xp76s81jwk0fS9oOv5dvK6k"
    client = genai.Client(api_key=api_key)

    chat = client.chats.create(model="gemini-flash-latest")


    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break

        print("Thinking...")

        try:

            response = chat.send_message(user_input)

            print(f"\nGemini: {response.text}")
            print("-" * 200)

        except Exception as e:
            print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()