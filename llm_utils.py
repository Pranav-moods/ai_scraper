import google.generativeai as genai

# Replace with your actual key
genai.configure(api_key="your_google_gemini_api_key_here")

# Use a valid and supported model name
model = genai.GenerativeModel("models/gemini-1.5-flash")

def call_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text
