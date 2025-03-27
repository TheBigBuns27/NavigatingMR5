import streamlit as st
#For running: streamlit run main.py [-- script args]

st.title(":blue[Welcome to] :orange[MR5] :blue[Navigation Tool!]")
st.write("THIS CAN BE A QUICK EXPLANATION AREA")
options = ["Entrance 1", "Bathroom 1", "Staircase 1", "Lab 1", "ETC."]
x = st.selectbox("Please choose a destination", options)
st.write("Below are directions to get to " + str(x) + ":")