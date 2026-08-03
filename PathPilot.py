import random
import streamlit as st



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
        import streamlit as st
import random

# Career Tab
with tab2:
    st.subheader("Career Tab – Discover Rare Careers")

    # Pool of questions
    questions_pool = [
        "Do you enjoy solving puzzles and logical problems?",
        "Would you like to explore space as an astronaut?",
        "Do you prefer creating art or designing things?",
        "Are you curious about how movies are made?",
        "Do you enjoy helping people feel better?",
        "Would you like to work with animals?",
        "Do you enjoy experimenting with science?",
        "Would you like to invent new technology?",
        "Do you enjoy writing stories or scripts?",
        "Would you like to explore the deep ocean?"
    ]

    # Randomly select 3 questions each time
    selected_questions = random.sample(questions_pool, 3)

    # Display questions
    for i, q in enumerate(selected_questions, 1):
        st.write(f"Q{i}: {q}")
        st.radio("Your answer:", ["Yes", "No"], key=f"q{i}")

    # Submit button
    if st.button("Submit Quiz"):
        st.success("🎉 Thanks! Based on your answers, PathPilot will suggest rare careers for you.")
