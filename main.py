import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1,col2 = st.columns(2)

with col1:
    st.image('images/me.png', width= 400)

with col2:
    st.title('What is Love?')
    content =''' Love can be crazy but can never be easy it will test us from time to time. 
    It doesnt matter who we are with but , how nice the person is Love will find the ways to test it.
    because not everyone gets this change to love someone there whole life.'''
    st.info(content)


st.write('this is new row ...')

df = pd.read_csv('data.csv', sep =';')

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+(row['image']),width= 300)
        st.write(f"[Source code:]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/'+(row['image']),width= 300)
        st.write(f"[Source code:]({row['url']})")
