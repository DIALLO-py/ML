#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 19:14:28 2024

@author: ibrahima-bailodiallo
"""

# -*- coding: utf-8 -*-
#"""
#Config streamlit.
#"""

import pandas as pd
import numpy as np
import streamlit as st
import io
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px    # pour avoir des plots inter-actif


df=pd.read_csv("detailed-reviews-of-all.csv")


#""" diviser en 4 page"""
st.sidebar.title("Sommaire")
pages = ["Contexte du projet","Exploration des données", "Analyse de données","Modélisation"]
page = st.sidebar.radio("Aller vers la page",pages)



if page == pages[0]:
    
    st.write("### Contexte du projet")
    
    st.write("""Ce projet s'inscrit dans un contexte << E-reputation >>. L'internet est un espace d'échange entre utilisateurs (Adminsitartion vs Citoyens). 
             Tous les sujets y sont abordés + ou - .
             L'objectif est d'analyser et de suivre les tendances afin de connaitre les points de tensions.
             Ces dernières donnent des indicateurs clès qui vont permettre d'agir efficacement en matière d'actions et de communication""")
    
    st.image("image.png")
 
elif page == pages[1]:
    
    st.write("## Exploration des données")
    
    st.dataframe(df.head()) #st.dataframe pour afficher le tableau 
    
    st.write("Dimensions du dataframe")
    st.write(df.shape)
    
    st.write("Information relatives au dataframe")
    buffer = io.StringIO()  # rediriger la sortie vers le buffer puis recuperer le contenu est puis l'afficher 
    df.info(buf=buffer)
    info_string = buffer.getvalue()
    
    st.text(info_string)
    
    if st.checkbox("Afficher les valeurs manquantes"):
        st.dataframe(df.isna().sum())
        
    if st.checkbox("Afficher les doublons"):
        st.write(df.duplicated().sum())
  
#Traitement des données#
    
    
elif page == pages[2]:
    
    st.write("## Analyse de données")
    
    fig = sns.displot(x='rating', data=df, kde=True)
    plt.title("Distribution de la variable cible rating")
    st.pyplot(fig)
    
    fig2 = px.scatter(df, x='rating', y='published_at', title="Evolution des avis en fonction des années")
    st.plotly_chart(fig2)
    
    fig3, ax = plt.subplots()
    sns.heatmap(df.corr(),ax=ax)
    plt.title ('Matrice de correlation des variables du dataframe')
    st.write(fig3)
    
elif page == pages[3]:
    
    st.write("## Modélisation")
    
    model_choisi = st.selectbox(label = "Modèle", options = ["linear", "regression", "KMN"])
    
    def train_model(model_choisi):
        
        if model_choisi == "linear" :
            y_pred=1
        elif model_choisi == "regression" :
            y_pred = 2
        elif model_choisi == "KMN" :
            y_pred = 3
        
        return y_pred
    
    st.write(train_model(model_choisi))
    