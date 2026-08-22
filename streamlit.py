import streamlit as st

# 🌟 App title and intro
st.set_page_config(page_title="PathPilot", page_icon="🎓", layout="centered")
st.title("PathPilot")
st.subheader("Your student-friendly career and wellness companion 🌱")

# 🧠 About section
st.write("""
PathPilot helps students explore unique career paths, reduce exam stress, and stay mindful.
Discover exciting professions, take fun quizzes, and learn how to balance study and well-being.
""")

# 🎲 Quiz section
st.header("🎲 Quick Career Quiz")
question = st.radio(
    "Which activity sounds most fun to you?",
    ["Designing apps", "Helping people", "Exploring nature", "Solving puzzles"]
)

if st.button("Show suggestion"):
    if question == "Designing apps":
        st.success("You might enjoy becoming a Software Developer or UX Designer!")
    elif question == "Helping people":
        st.success("You could explore Psychology, Teaching, or Healthcare careers!")
    elif question == "Exploring nature":
        st.success("Environmental Science or Wildlife Conservation might be perfect for you!")
    else:
        st.success("Try Data Science or Engineering — your logic skills shine!")

# 💬 Footer
st.markdown("---")
st.caption("Made with 💖 using Streamlit | PathPilot © 2026")
