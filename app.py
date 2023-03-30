import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import iframe

from streamlit_option_menu import option_menu
st.set_page_config(page_title="Code75", page_icon='./Images/mm.png')
    
selected=option_menu(
        menu_title="RUHVSoft LLP",
        options = ["Code-Editor"],
        icons=["code-slash"],
        menu_icon="emoji-laughing",
        default_index=0,
        orientation="horizontal",)
st.title("Select programming language")
language = st.selectbox("options", ["C", "C++","Java", "Python","HTML/CSS/Javascript","Verilog"],label_visibility='collapsed')

if language == "C":
    components.iframe(''' https://www.jdoodle.com/a/63kh''',width=800, height=666, scrolling=False)
    
elif language == "C++":
    components.iframe(''' https://www.jdoodle.com/a/63kl''',width=800, height=666, scrolling=False)
    
elif language == "Java":
    components.iframe(''' https://www.jdoodle.com/a/63k9''',width=800, height=666, scrolling=False)
    
elif language == "Python":
    components.iframe(''' https://www.jdoodle.com/a/63kn ''',width=800, height=666 ,scrolling=False)
    
elif language == "HTML/CSS/Javascript":
    components.iframe(''' https://jdoodle.com/h/2Vv ''',width=800, height=1200 ,scrolling=False)

elif language == "Verilog":
    components.iframe(''' https://jdoodle.com/a/63ks''',width=800, height=666 ,scrolling=False)
