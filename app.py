from flask import Flask, render_template, request, jsonify
import random
import openai  # Si tu veux utiliser GPT-3, assure-toi d'installer openai avec pip install openai

app = Flask(__name__)

# Configure ta clé API OpenAI ici (si tu utilises GPT-3)
# openai.api_key = 'YOUR_API_KEY'

# Exemple de "réponses IA" basiques
responses = [
    "Bonjour, comment puis-je vous aider ?",
    "Je suis là pour vous assister.",
    "Quel est votre problème aujourd'hui ?",
    "Je peux vous répondre sur divers sujets !"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message'].lower()  # Mettre tout en minuscule pour éviter les erreurs de casse

    # Dictionnaire de réponses plus intelligentes
    responses_dict = {
        "bonjour": "Bonjour, comment puis-je vous aider ?",
        "quoi": "Je suis un chatbot simple. Que puis-je faire pour vous ?",
        "comment ça va": "Je vais bien, merci ! Et vous ?",
        "merci": "Avec plaisir !",
    }

    # Si l'input correspond à une des clés dans responses_dict, on renvoie la réponse correspondante
    for key in responses_dict:
        if key in user_input:
            return jsonify({'response': responses_dict[key]})

    # Si tu veux utiliser GPT-3 pour répondre de manière plus avancée
    try:
        # Utilisation de GPT-3 pour générer une réponse
        openai.api_key = 'YOUR_API_KEY'  # Remplace par ta clé API OpenAI
        response = openai.Completion.create(
            model="text-davinci-003",  # Choisis le modèle GPT-3 approprié
            prompt=user_input,
            max_tokens=100
        )
        return jsonify({'response': response.choices[0].text.strip()})
    except Exception as e:
        return jsonify({'response': "Désolé, une erreur est survenue."})

    # Réponse par défaut si rien n'est compris
    return jsonify({'response': "Désolé, je n'ai pas compris."})

if __name__ == "__main__":
    app.run(debug=True)