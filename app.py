import streamlit as st
import joblib
model = joblib.load('sentiment-analysis')
st.title('Senriment-analysis')
ip = st.text_input('Enter your review')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])  
 
