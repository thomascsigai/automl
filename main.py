import streamlit as st
import pandas as pd

#Rappel: Pour lancer l'app "streamlit run main.py" à partir du répertoire courant

def acc_func():
    data_cca = data.dropna()
    st.write(data_cca)
    st.write(data_cca.isnull().mean().sort_values(ascending = True))
    return data_cca

def mean_func():
    st.write("Mean")

def median_func():
    st.write("Median")

st.title('AutoML')
uploaded_file = st.file_uploader("Selectionner un dataset",type=['csv','xlsx'],accept_multiple_files=False)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

    st.subheader("Données manquantes")
    select = st.radio("Selectionner une méthode : ", ("Analyse complète des cas", "Mean imputation", "Median imputation"))

    if select == "Analyse complète des cas":
        data = acc_func()

    if select == "Mean imputation":
        mean_func()

    if select == "Median imputation":
        median_func()




