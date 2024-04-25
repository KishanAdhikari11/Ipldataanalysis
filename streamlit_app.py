import streamlit as st
import pandas as  pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly
st.set_page_config(page_title="IPL Dashboard",
                   page_icon=":bar_chart",
    layout="wide")
    

st.title("IPL dashboard")
st.markdown('_Prototype v0.4.1')

@st.cache_data
def load_csv(filepath):
    df=pd.read_csv(filepath)
    return df

search_query=st.text_input("Enter player name:")
upload_file=st.file_uploader("Choose a file")
df=load_csv("./match_data.csv")
st.dataframe(df)

another_file=st.file_uploader("Choose another file")
df=load_csv("./match_info_data.csv")
st.dataframe(df)