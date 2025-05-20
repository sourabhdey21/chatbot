import google.generativeai as genai
import os
from dotenv import load_dotenv

# Configure the Gemini API
API_KEY = "AIzaSyDe78sb7ubnscq0ydZgk3-mI4k744w_lqE"
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("🤖 Welcome to Gemini Bot! Type 'quit' or 'exit' to end the conversation.")
    print("=" * 50)
    
    while True:
        user_input = input("\n👤 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print("\n👋 Goodbye! Thanks for chatting!")
            break
            
        if not user_input:
            continue
            
        print("\n🤖 Gemini: ", end="")
        response = get_gemini_response(user_input)
        print(response)
        print("=" * 50)

if __name__ == "__main__":
    main() 