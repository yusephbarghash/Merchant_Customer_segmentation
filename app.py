
import pandas as pd
import numpy as np
import streamlit as st

rfm = pd.read_csv('rfm_clusters.csv')
top_cluster_Mer = pd.read_csv('top_cluster_Mer.csv')

def main():
    st.title('Check your points: 😊')
    try:
        user_input = st.text_input('Enter Your ID: ', )
        user_id = int(user_input)
        if user_id>33518:
            st.warning("Please enter a valid ID.")
            user_id = None
    except (ValueError, UnboundLocalError, IndexError):
        st.warning("Please enter a valid ID.")
    try:
        
        if st.button("Check"):
            lst = list(top_cluster_Mer[top_cluster_Mer['Cluster'] == int(rfm[rfm['User_Id'] == user_id]['Cluster'])]['Mer_Name'])[::-1]
            points = int(rfm[rfm['User_Id'] == user_id]['Monetary'] * 10)
            st.text(f'you have a {points} points to spend it on : \n\t{lst[0]}\n\t{lst[1]}\n\t{lst[2]}\n\t{lst[3]}')
    except:
        st.text("")

main()
