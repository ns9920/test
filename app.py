import streamlit as st
import requests

def read_json_file(file_name):
  response = requests.get(file_name)
  data = response.json()
  return data

st.title("Streamlit App to Read JSON File")

file_name = st.text_input("Enter the file name:")

if file_name:
  data = read_json_file(file_name)
  st.json(data)

st.button("Read JSON File")
