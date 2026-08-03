import streamlit as st
import random

# Inject manifest and service worker
st.markdown("""
<link rel="manifest" href="manifest.json">
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/service-worker.js');
}
</script>
""", unsafe_allow_html=True)

# Chatbot intro
st.title("🌟 PathPilot: Your Friendly Guide")
st.write(
    "Hi there! I’m PathPilot, here to help you feel calmer about exams "
    "and explore fun career ideas."
)

# Chat input
user_input = st.text_input("Tell me how you're feeling today:")

if user_input:
    distress_keywords = ["sad", "depressed", "hopeless", "crying", "anxious"]
    if any(word in user_input.lower() for word in distress_keywords):
        st.warning("💛 It sounds like you’re feeling really low. Please talk to a trusted adult, teacher, or school counselor — you don’t have to go through this alone.")
    else:
        st.success("😊 Thanks for sharing! Let’s explore some career ideas together.")

# 🎯 Quick Career Quiz
st.subheader("Quick Career Quiz")

# Define quiz questions BEFORE using them
quiz_questions = {
    "Do you enjoy solving puzzles and logical problems?": "Data Scientist",
    "Would you like to explore space as an astronaut?": "Astrophysicist",
    "Do you prefer creating art or designing things?": "Graphic Designer",
    "Are you curious about how movies are made?": "Film Director",
    "Do you enjoy helping people feel better?": "Psychologist",
    "Would you like to work with animals?": "Veterinarian",
    "Do you enjoy experimenting with science?": "Chemist",
    "Would you like to invent new technology?": "Engineer",
    "Do you enjoy writing stories or scripts?": "Writer",
    "Would you like to explore the deep ocean?": "Marine Biologist"
}

answers = {}
for question in quiz_questions:
    answers[question] = st.radio(question, ["Yes", "No"], key=question)

if st.button("Show Career Suggestion"):
    matching_professions = [
        profession for question, profession in quiz_questions.items()
        if answers[question] == "Yes"
    ]
    if matching_professions:
        suggested_profession = random.choice(matching_professions)
        st.subheader(f"🌈 You might enjoy becoming a **{suggested_profession}**!")
    else:
        st.info("No worries! Try answering 'Yes' to a few questions for a suggestion.")
