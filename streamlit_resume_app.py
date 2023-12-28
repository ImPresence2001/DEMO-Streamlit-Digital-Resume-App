from json import load
from turtle import left
import streamlit as st
from PIL import Image
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title = 'Resume: YOURNAME',
    page_icon = '👩‍💻',
    layout = 'wide',
    #initial_sidebar_state = "expanded",
)

#load lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
            return None
    return r.json()

#load lottie assets
about_animation = load_lottieurl("https://lottie.host/d35e66dd-b0d6-4587-abe6-9fbaef60c02d/x2zjMLWHhe.json")
contact_animation = load_lottieurl('https://lottie.host/c8e8aa0f-bbe6-44b6-8298-4773552537a0/JPhsQE5J5B.json')
home_animation = load_lottieurl('https://lottie.host/1eecd6a7-4118-40f3-a505-fcc0ce6ce213/UEq8E8mabd.json')
educ_animation = load_lottieurl('https://lottie.host/a53fbb43-5e5a-46e2-8800-20018c8e9030/5TlK4i24Da.json')

# web page css
def css(file_name):
     with open(file_name) as f:
          st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
css("style/style.css")

#image load assets
img_dp = Image.open('images/dp500.png')

selected = option_menu(
    menu_title = None,
    options = ['Home', 'About', 'Skills', 'Experiences', 'Certificates'],
    icons = ['house', 'file-person', 'activity', 'book', 'patch-check'],
    default_index = 0,
    orientation = 'horizontal',
)


#nav bar when home is selected
if selected == 'Home':
     with st.container():
          st.write('---')
          image_column, text_column, blank_column = st.columns(3)
          with image_column:
               st.image(img_dp)
          with text_column:
               st.subheader("Hi! I'm YOURNAME")
               st.write('Bachelor of Science in COURSE')# IT DEPENDS ON YOU
               st.caption(
                    '''
                    --> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                    ---
                    Contact me on:

                    Facebook: [your name](your link here)

                    Instagram [@yourname](your link here)

                    Phone Number: [(+63) 9123456789](), [(+63) 9987654321]()
                    '''
                    )
          with blank_column:
              st.lottie(home_animation, height=450, key='home')
               
          st.write('---')
          st.write('##')

          contact_form = """
        <form action="https://formsubmit.co/YOUR EMAIL ADDRESS HERE" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
          left_column, mid_column, right_column = st.columns(3)
          with left_column:
            st_lottie(contact_animation, height=400, key='contact_me')
          with mid_column:
            st.header('Get In Touch With Me!')
            st.markdown(contact_form, unsafe_allow_html=True)
          with right_column:
            st.subheader("""
                References:
                - FIRST MI LAST | Teacher | (+63) 9xxxxxxxxx
                - FIRST MI LAST | Data Analyst | (+63) 9xxxxxxxxx
                """)

     

#about info
if selected == 'About':
     st.write('---')
     st.title('About Me')
     st.write('##')
     leftmost_column_about, left_column_about, right_column_about = st.columns(3)
     with leftmost_column_about:
        st.subheader(
                """
                My Personal Details:
                - Full Name: [Full Name]
                - Nationality: [Nationality]
                - Religion: [Religion]
                - Gender: [Gender]
                - Marital Status: [Status]
                - Birth Date: [MM/DD/YYYY]
                - Birth Place: [Address]
                - Current Address: [Current Address]
                """)
     with left_column_about:
        st.subheader("""
                What I always do:
                - Lorem ipsum: Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
                - Lorem ipsum: Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
                - Lorem ipsum: Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
                - Lorem ipsum: Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
                """) #add as many as you like
     with right_column_about:
         st_lottie(about_animation, height=350, key='about_me')
    
     st.write('---')
     left_educ, right_educ = st.columns((1,2))
     with left_educ:
         st.lottie(educ_animation, height=300, key='education')
     with right_educ:
         st.subheader(
                """
                Educational Attainment
                ##
                ##
                - Elementary | YYYY-YYYY | Name of your school
                - Junior Secondary | YYYY-YYYY | Name of your school
                - Senior Secondary | YYYY-YYYY | Name of your school
                - Tertiary | YYYY-YYYY | Name of your school
                """)#you can edit, just follow the format


if selected == 'Skills':
     st.title(f'{selected}!')


if selected == 'Experiences':
     st.title(f'{selected}!')


if selected == 'Certificates':
     st.title(f'{selected}!')
