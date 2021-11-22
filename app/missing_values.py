import streamlit as st
import pandas as pd

def cca_func(data):
    data_cca = data.dropna()
    st.write(data_cca)
    st.write(data_cca.isnull().mean().sort_values(ascending = True))
    return data_cca


def mean_func(data):
    st.write("Mean")

def median_func(data):
    st.write("Median")