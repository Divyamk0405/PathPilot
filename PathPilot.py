import random
import streamlit as st

# Career quiz questions
quiz_questions = {
    "Do you enjoy solving puzzles?": "Scientist",
    "Do you like helping others?": "Teacher",
    "Do you enjoy drawing or painting?": "Artist",
    "Do you love exploring nature?": "Biologist",
    "Do you enjoy building things?": "Engineer",
}

profession_images = {
    "Scientist": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Scientist.jpg",
    "Teacher": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Teacher.jpg",
    "Artist": "https://upload.wikimedia.org/wikipedia/commons/4/47/Artist.jpg",
    "Biologist": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Biologist.jpg",
    "Engineer": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Engineer.jpg",
}

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
        st.warning(
            "💛 It sounds like you’re feeling really low. Please talk to a trusted adult, "
            "teacher, or school counselor — you don’t have to go through this alone."
        )
    else:
        st.success("😊 Thanks for sharing! Let’s explore some career ideas together.")

# Career quiz section
st.subheader("🎯 Quick Career Quiz")

answers = {}
for question in quiz_questions:
    answers[question] = st.radio(question, ["Yes", "No"], key=question)

if st.button("Show Career Suggestion"):
    matching_professions = [
        profession
        for question, profession in quiz_questions.items()
        if answers[question] == "Yes"
    ]

    if matching_professions:
        suggested_profession = random.choice(matching_professions)
        st.subheader(f"🌈 You might enjoy becoming a **{suggested_profession}**!")
        st.image(
            profession_images[suggested_profession],
            caption=suggested_profession,
            use_container_width=True,
        )
    else:
        st.info("No worries! Try answering 'Yes' to a few questions for a suggestion.")