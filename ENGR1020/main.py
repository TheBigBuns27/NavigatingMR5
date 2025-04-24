import streamlit as st
import harvestData as h
import backend as b
#For running: streamlit run main.py [-- script args]

st.title(":blue[Welcome to] :orange[MR5] :blue[Navigation Tool!]")
st.write("This website is a navigation tool for the MR5 building of UVA. ")

if st.query_params.get("password") == "wahoowa":
    st.write("Hello admin!")
    st.write("In order to make a change to the room assignments, please follow these steps")
    st.write("Step 1. Download this excel sheet.")
    with open("ENGR1020/rooms.xlsx", "rb") as f:
        st.download_button("EXCEL SHEET", f, "rooms.xlsx")
    st.write("Step 2. Make the necessary changes to the contents of each room. Ex: Christ Lab #2 --> Smith Lab #2")
    st.write("NOTE: Contact the team if you want to make changes to the room numbers themselves")
    st.write('Step 3. Ensure that the name of the file you are done with is "rooms.xlsx"')
    st.write("Step 4. Email the finished excel file to Connor Labiak rnv8zq@virginia.edu.")

else:
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
