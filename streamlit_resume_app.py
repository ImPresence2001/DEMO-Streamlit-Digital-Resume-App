from pathlib import Path
import streamlit as st
from PIL import Image
import requests
from json import load
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "filename.pdf"#YOUR CV GOES HERE
img_display = current_dir / "images" / "display_picture.png"

#PAGE CONFIG
st.set_page_config(
    page_title = 'Resume: YOURNAME',
    page_icon = '📄',
)
#LOAD LOTTIE FOR ANIMATION
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
            return None
    return r.json()
#LOTTIE ASSETS
skills_anime = load_lottieurl('https://lottie.host/1eecd6a7-4118-40f3-a505-fcc0ce6ce213/UEq8E8mabd.json')

#WEBPAGE CSS
def css(file_name):
     with open(file_name) as f:
          st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
css("style/style.css")
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
img_display = Image.open(img_display)

#CERTIFICATE IMAGES GOES HERE
cert1 = Image.open('images/certificates/Cert1.png')
cert2 = Image.open('images/certificates/Cert2.png')
cert3 = Image.open('images/certificates/Cert3.png')

# HOME SECTION
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(img_display, width=260)

with col2:
    st.header("YOUR NAME HERE")
    st.write('DATA ANALYST | BACKEND DEVELOPER')
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    #YOU CAN ADD MANY AS YOU LIKE
    st.write(
         """
- 📫 YOUREMAIL@gmail.com
- 🌐 Facebook: [YOUR FACEBOOK ACCOUNT](https://www.facebook.com/)
- 🌐 Instagram: [YOUR INSTAGRAM ACCOUNT](https://www.instagram.com/)
"""
    )

select = option_menu(
    menu_title = None,
    options = ['Skills', 'Experiences', 'Certificates'],
    icons = ['activity', 'book', 'patch-check'],
    default_index = 0,
    orientation = 'horizontal',
)

if select == 'Skills':
     st.header('Skills')
     st.write('---')
     col1, col2 = st.columns(2, gap="small")
     with col1:
          st.write(
          """
- ✅ SKILLS HERE
- ✅ SKILLS HERE
- ✅ SKILLS HERE
- ✅ SKILLS HERE
- ✅ SKILLS HERE

"""
)
     with col2:
          st_lottie(skills_anime, height=200, key='Skills')
     st.header('Hard Skills')
     st.write('---')
     col1, col2 = st.columns(2, gap="small")
     with col1:
          st.write(
          """
- ✅ Databases: 
- ✅ Web Frameworks: 
- ✅ Programming Languages: 

"""
)
     with col2:
          st.empty()
     
     

if select == 'Experiences':
     st.header('Experiences')
     st.write('---')
#ADD MANY JOB EXPERIENCE AS YOU LIKE
     st.subheader('Job Position | Company Name')
     st.write(
          """
October 2023 - December 2023
- Lorem ipsum: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
"""
     )
     st.subheader('Job Position | Company Name')
     st.write(
          """
January 2024 - March 2024
- Duis aute: Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
     )

if select == 'Certificates':
     st.header('Certificates')
     st.write('---')
#ADD MANY CERT AS YOU LIKE
#Certificate 1
     st.subheader('Certificate: Title')
     st.write(
          """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
"""
     )
     st.image(cert1, caption='Title - Subtitle')
     st.write('##')

#Certificate 2
     st.subheader('Certificate: Title')
     st.write(
          """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
"""
     )
     st.image(cert2, caption='Title - Subtitle')
     st.write('##')

#Certificate 3
     st.subheader('Certificate: Title')
     st.write(
          """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
"""
     )
     st.image(cert3, caption='Title - Subtitle')
     st.write('##')
