import streamlit as st
import requests

st.markdown(
    """
    <style>
    body {
        background-color: #ffefd5;
        color: #000;
    }
    .title {
        font-family: 'Comic Sans MS', cursive;
        color: #ff6347;
        text-align: center;
    }
    .subtitle {
        font-family: 'Comic Sans MS', cursive;
        color: #4682b4;
        text-align: center;
    }
    .response {
        background-color: #f0e68c;
        padding: 20px;
        border-radius: 10px;
        font-family: 'Comic Sans MS', cursive;
    }
    .section-title {
        color: #32cd32;
        font-family: 'Comic Sans MS', cursive;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title">🤖 SIDI Chatbot - Science et Technologie 🌟</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
    <p>Salut les jeunes explorateurs!</p>
    <p>Je suis <strong>SIDI</strong>, votre ami en science et technologie.</p>
    <p>Posez-moi n'importe quelle question, et je vous donnerai une réponse!</p>
</div>
""", unsafe_allow_html=True)

# Boîte de texte pour l'entrée de l'utilisateur avec un bouton pour envoyer la question
st.markdown('<h3 class="section-title">Pose ta question ici 👇:</h3>', unsafe_allow_html=True)
col1, col2 = st.columns([10, 1])
with col1:
    user_input = st.text_input("", key="question", label_visibility="collapsed", placeholder="Pose ta question ici")
with col2:
    send_button = st.button("➡️")

# Gérer l'envoi de la question lorsque l'icône est cliquée
if send_button and user_input:
    # Envoyer la question au serveur Flask et obtenir la réponse
    FLASK_URL = "http://localhost:5000/chatbot"  # Mettez à jour avec votre URL Flask
    try:
        response = requests.post(FLASK_URL, json={'question': user_input})
        response.raise_for_status()  # Gérer les erreurs HTTP
        chatbot_response = response.json().get('response')
        
        # Afficher la réponse du chatbot
        st.markdown(f'<div class="response"><strong>Question</strong>: {user_input}<br><br>{chatbot_response}</div>', unsafe_allow_html=True)
    
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de la communication avec le chatbot : {e}")

# Ajouter des éléments visuels supplémentaires
st.markdown("""
<div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-top: 20px;">
    <h3 style="color: #ff6347; font-family: 'Comic Sans MS';">Conseil du jour 🧠</h3>
    <p style="font-family: 'Comic Sans MS';">
        Chaque jour est une nouvelle opportunité d'apprendre quelque chose de nouveau. Sois curieux et n'aie pas peur de poser des questions !
    </p>
</div>
""", unsafe_allow_html=True)
