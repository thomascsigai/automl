import streamlit as st
import pandas as pd

#Rappel: Pour lancer l'app "streamlit run main.py" à partir du répertoire courant


st.title('AutoML')
uploaded_file = st.file_uploader("Selectionner un dataset",type=['csv','xlsx'],accept_multiple_files=False)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)


