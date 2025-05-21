from flask import Flask, render_template, request, jsonify, Response
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure the Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set in .env file")
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')

def stream_gemini_response(prompt):
    try:
        for chunk in model.generate_content(prompt, stream=True):
            if hasattr(chunk, 'text') and chunk.text:
                yield chunk.text
    except Exception as e:
        yield f"An error occurred: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_message = data.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    return Response(stream_gemini_response(user_message), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True) 