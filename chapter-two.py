import streamlit as st

st.title("Chai Maker app")

if st.button("make chai"):
    st.success("chai is brewed")
    
add_masala=st.checkbox("Add masala")

if add_masala:
    st.write("Masala added to your chai")
    
tea_type=st.radio("Pick your chai base:", ["Milk","Water","Sugar"])
st.write(f"Tea type is {tea_type}")

flavour=st.selectbox("Choose your flavour:",["Adrak","Honey","Saffron"])
st.write("You choose:",flavour)

sugar=st.slider("Sugar level(spoon)",0,5,2)
st.write("Selected sugar level",sugar)

cups=st.number_input("How many cups",min_value=1,max_value=10,step=1)
st.write("Selected cups are",cups)

name=st.text_input("Enter your name")
if name:
    st.write("Welcome",name,"! Your chai is on the way")
    
dob=st.date_input("Select your date of birth")
if dob:
    st.write("Your dob is",dob)