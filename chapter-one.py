import streamlit as st

st.title("Streamlit learn")
st.subheader("Streamlit Learning Template")
st.text("Welcome to our first interactive app")
st.write("Choose your favourite language")

language=st.selectbox("Your fav language:",["Java","Python","C/C++",".net"])

st.write(f"You choose {language}. Excellent choice!")

st.success("Congrats")

