#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:16:16 2024

@author: ibrahima-bailodiallo
"""

import pandas as pd
import numpy as np
import streamlit as st
import io
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px                 # pour avoir des plots inter-actif
import emoji


df=pd.read_csv("detailed-reviews-of-all.csv")




#""" diviser en 4 page"""
st.sidebar.title("AGOR'AI App")
pages = [" Unlock the Power of Your Data","Data Master", "Analyse de données","Modélisation"]
page = st.sidebar.radio("Explore the App",pages)



if page == pages[0]:
    
    st.write("""## About """ + emoji.emojize(':raised_hand:'))
    
    st.write("## Empower your decisions , your e-Reputation with actionable insights !")
    
    st.write(""" **AGOR'AI App** harnesses the power of trend analysis and sentiment tracking to deliver key indicators.
                Enabling you to make informed moves with confidences """)
                
    st.image("Kesk’ia-2.png")

elif page == pages[1]:
    
    st.write("# Upload your Dataset")
    uploaded_file = st.file_uploader('Choose a file')      #Button upload
    if uploaded_file is not None :
        df = pd.read_csv(uploaded_file)
        st.write('*Raw Data*')
        st.dataframe(df.head())             #st.dataframe pour afficher le tableau 
        st.write('Size of Dataset')
        st.write(df.shape)
        
        if st.checkbox("Cleaned Data"):
            #Traitement Data 
            df.drop_duplicates(inplace=True,subset=['review_id_hash']) # enlever les donnèes dupliquèes
            # Vérifier si l'ID spécifié est présent dans le DataFrame (saint quentin en yvelines on a enleve la prefcture)
            if 'ChIJ33ku9dSG5kcR6x56v_XLBBE' in df['place_id'].values:
                # Exclure les lignes avec cet ID si elles existent
                df2 = df[df['place_id'] != 'ChIJ33ku9dSG5kcR6x56v_XLBBE']
                df2 = df2.drop(['place_id','review_id_hash','published_at_date','response_from_owner_date',
                                'review_translated_text','response_from_owner_translated_text'], axis=1)
                st.dataframe(df2.head())
                st.write(" The number of reviews is : ")
                st.write(df2.shape)
                st.write('Place Name')
                st.write(df2.place_name.value_counts())
                #Creer la lsite des places uniques
                place_name = df2['place_name'].unique()
                #ajouter le menu deroulant
                selected_place = st.selectbox('filter place name', place_name)
                #filtrer le dataset selon la selection
                filtered_df = df2[df2['place_name']==selected_place]
                #afficher place_name et son nombre d'avis
                #for index, row in filtered_df.iterrows():
                    st.write(f"PlaneName : {row[place_name]}, Counts Avis : {row[")
            else:
                # Optionnel : ajouter une logique si l'ID n'existe pas, par exemple un log ou une action spécifique
                print("L'ID spécifié n'existe pas dans le DataFrame.")
                
        
    

    
    # st.write("Information relatives au dataframe")
    # buffer = io.StringIO()  # rediriger la sortie vers le buffer puis recuperer le contenu est puis l'afficher 
    # df.info(buf=buffer)
    # info_string = buffer.getvalue()
    
    # st.text(info_string)
    
    # if st.checkbox(" Print Rating"):
    #     st.dataframe(df['rating'].describe().T)
        
    # if st.checkbox("Afficher les doublons"):
    #     st.write(df.duplicated().sum())
    