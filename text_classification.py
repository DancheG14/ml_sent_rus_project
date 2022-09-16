import io
import streamlit as st
import requests



st.title('Определение тональности текста')
text = st.text_input('Введите текст', 'Я люблю распределенные вычисления')
result = st.button('Определите тональность')
if result:
  response = requests.post
    
