import streamlit as st
from sending_email import sent_email

st.header('Contact Us')

with st.form(key= 'email_forms'):
    user_email = st.text_input('Your email adderss')
    user_message = st.text_area('your message')
    message = f'''\
subject : Message from {user_email}

from: {user_email}
{user_message}
'''
    button = st.form_submit_button('Submit')
    if button:
        sent_email(message)
        st.info('Thanks for contacting us! we will get back to you soon')
