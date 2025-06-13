# chatbot/views.py
import openai  # Import the new library
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def ask_ai(request):
    if request.method == 'POST':
        try:

            openai.api_key = "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"

            data = json.loads(request.body)
            user_message = data.get('message')

            if not user_message:
                return JsonResponse({'error': 'No message provided'}, status=400)

            system_prompt = """
            You are 'BridgeBot', a friendly and professional AI assistant for TechBridge Solutions.
            Your purpose is to answer questions about our services and to identify potential clients.
            Our services include: Custom Software Development, IT Support & Managed Services, Cybersecurity Solutions, and Cloud Computing & Migration.
            Your personality should be helpful, a little funny, and very encouraging.
            **Your primary goal is to capture leads.** If a user expresses interest in a service, asks for pricing, or seems like a potential client, your goal is to ask for their name and email address so our team can follow up.
            For example, say: "That's a great question! I can have someone from our team get back to you with more details. What's your name and email address?"
            """

            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ]
            )
            
            ai_message = response.choices[0].message.content
            
            return JsonResponse({'response': ai_message})

        except Exception as e:
            print(f"--- AN EXCEPTION OCCURRED ---")
            print(f"{type(e).__name__}: {e}")
            print(f"-----------------------------")
            return JsonResponse({'error': 'An error occurred while processing your request.'}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)