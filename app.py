import streamlit as st

# Full Page Layout
st.set_page_config(page_title="FAU ISM 6427C", layout="wide")

# Header with an Image
st.image("https://img2.wikia.nocookie.net/__cb20120628082105/collegefootballmania/images/4/4b/NCAA-Florida_Atlantic_Owls-logo.png")
st.title("FAU ISM 6427C")
st.write("Welcome to the course repository for FAU's ISM 6427C class.")

# Sidebar
st.sidebar.header("Course Information")
st.sidebar.write("Instructor: Dr. John Doe")
st.sidebar.write("Semester: Spring 2025")
st.sidebar.write("Office Hours: By Appointment")

# Main Content
st.subheader("About This Class")
st.write("This class focuses on practical applications of AI and data science tools, including the use of platforms like Streamlit for project deployment.")


st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')

