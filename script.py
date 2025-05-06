import google.generativeai as genai
import get_api_key

genai.configure(api_key=get_api_key.api)

# model instance
model = genai.GenerativeModel("gemini-1.5-flash")

description = '''
You are just a simple chatbot, made for helping others
'''
output = model.start_chat()

while True:
    user = input("Me: ")
    if user.lower() in ['exit', 'quit']:
        break

    prompt = f"""description: {description}
User: {user}
Answer based on the description I gave you."""

    response = output.send_message(prompt)
    print("Bot:", response.text)
