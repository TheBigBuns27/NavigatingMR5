import streamlit as st
import harvestData as h
import backend as b
#For running: streamlit run main.py [-- script args]

st.title(":blue[Welcome to] :orange[MR5] :blue[Navigation Tool!]")
st.write("This website is a navigation tool for the MR5 building of UVA. ")
st.write("Please enter a professor's name, OR enter a room number and directions will be shown.")
roomNums = h.roomNums()
locations = h.locations()
col1, col2 = st.columns(2)
start = "Checkpoint " + str(st.query_params.get("checkpoint"))

with col1:
    end1 = st.selectbox("Please choose a room number", roomNums)
with col2:
    end2 = st.selectbox("Please choose a professor or location name", locations)
accessibility = bool(st.checkbox("Accessibility Needed?"))

if end1 != "BLANK" and end2 != "BLANK":
    st.write("Only select from 1 dropdown.")
    end = "2 selected"
elif end1 != "BLANK":
    st.write("Below are directions to get to " + str(end1) + ":")
    end = str(end1)
    count = 1
    for direction in b.navigateMR5(start, end, accessibility):
        st.write("Step " + str(count) + ". " + direction)
        count += 1
elif end2 != "BLANK":
    st.write("Below are directions to get to " + str(end2) + ":")
    end = h.convertRoomToInt(end2)
    count = 1
    for direction in b.navigateMR5(start, end, accessibility):
        st.write("Step " + str(count) + ". " + direction)
        count += 1
else:
    end = "0"



