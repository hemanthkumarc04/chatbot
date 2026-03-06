import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google import genai
import os

# Initialize Gemini Client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 1. This renders your webpage
def home(request):
    return render(request, 'index.html')

# 2. This handles the text question from your JavaScript
@csrf_exempt
def ask_ai(request):
    if request.method == 'POST':
        try:
            # Parse the JSON text sent from the frontend
            data = json.loads(request.body)
            user_question = data.get('question')

            if not user_question:
                return JsonResponse({'error': 'No question provided'}, status=400)

            print(f"--- DEBUG: Received question: {user_question} ---")

            # Send the text to Gemini Flash-Lite
            response = client.models.generate_content(
                model='gemini-2.5-flash-lite', 
                contents=user_question
            )
            
            # Send the text back to the frontend in a JSON key called 'answer'
            return JsonResponse({'answer': response.text})
            
        except Exception as e:
            print(f"API Error: {e}") 
            return JsonResponse({'error': str(e)}, status=500)
            
    return JsonResponse({'error': 'Invalid request method'}, status=405)