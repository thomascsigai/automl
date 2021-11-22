import streamlit as st
import pandas as pd
from app.missing_values import cca_func, mean_func, median_func



#Rappel: Pour lancer l'app "streamlit run main.py" à partir du répertoire courant

st.title('AutoML')
uploaded_file = st.file_uploader("Selectionner un dataset",type=['csv','xlsx'],accept_multiple_files=False)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

    st.subheader("Données manquantes")
    select = st.radio("Selectionner une méthode : ", ("Analyse complète des cas", "Mean imputation", "Median imputation"))

    if select == "Analyse complète des cas":
        data = cca_func(data)

    if select == "Mean imputation":
        data = mean_func(data)

    if select == "Median imputation":
        data = median_func(data)




