#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 19:30:20 2024

@author: ibrahima-bailodiallo
"""



import pandas as pd

import numpy as np
import seaborn as sns
import sklearn.model_selection import train_test_split
import sklearn.model_selection import randomForestRefr



# lire mon csv
df = pd.read_csv( " nom_du_csv")

#voir la tête du dataset (5 lignes)
pd.head()

#Voir structure de la dataframe
pd.info()

#Resumé statistique de mes variables quatitatives
pd.describe()

#Affiché un graphique de mes donnees : nuage de points et histogrammes de chaque variable en diagonal 
sns.pairplot(df)


###### Creation modèle ########

#Creer un dataframe uniquement avec les variables numériques
df_num = df.select_dtypes(exclude="objet")

#Voir sa tête
def_num.head()
#Voir le nom de ces colonnes
def_num.colunms

#Features : Variables caractéristique
X = df_num.drop("price", axis=1)                    #Enlever la variable "price"

#Target: Variables cibles
y = df["price"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size=0.2, random_state=seed

)                                                   #Je fais diviser et utiliser 20% de mes données pour test et 80% pour l'entrainement'
#print Nombre de valeur pour train et test
print(X_train.shape, y_train.shape,, X_test.shape,, y_test.shape)

#Modele de regression linéaire multiple 
lr = LinearRegression()                                 #importer le modèle
lr.fit(X_train, y_train)                                #initialise le modèle et entrainement sur les trains

## Model de forêt aléatoire 
rf =  RandomForestreRegressor()
rf.fit(X_train, y_train)

##### Evaluer le modèle
def evaluate_model(model):
    train_preds = model.predict(X_train)                #Prediction sur les donnees d'entrainement                   
    test_preds = model.predict(X_test)                  #Prediction sur les donnees de test                
    
    #Calcul erreur quadrique sur les donnees d'entrainement et de test'
    rmse_train = mean_squared_error(y_train,train_preds, squared=False)                   #squared=False : pour ne pas calculer le mse
    rmse_test = mean_squared_error(y_test,test_preds, squared=False)
    
    #Ces 2 valeurs permmetront d'évaluer le modèle qu'on va contruire
    return rmse_train, rmse_test
                                    
                                
###Evaluer les modéles 
evaluate_model(lr)                  # ==> (300,150)      ==> monn erreur est de 150$, si on dit le prix est de XXXX donc il faut rajouter + ou -  150  
evaluate_model(rf)                  #==> (90, 130)      ==> le modèle rf est mieux que lr car il est aléatoire //linear


######################### pour importer le modele sur streamlit, besoin de faire un save avant ###########

import joblib 
joblib.dump(rf,"final_model.joblib")            # j'enregistre mon model rf en final_model': je dois le voir enregistrer en final_model.joblib

####### une fois le modele save . Il faut creer un nouveau fichier App.py ####

import streamlit as st
import numpy as np
import joblib

#1#Description Application 

st.tille("Prediiction du prix d'une voiture en fonctiond de ses caractéristiques")
st.subheader("application réaliser par DIALLO Ibrahima-Bailo")
st.markdown("Cette application utilise un modèle Machine learning pour prédire le prix d'une voiture")


#Chargement du model 
model = joblib.load("nom_du_model")


#définition d'une fonction d'interférence : prend en entree les features( caracteristiques) et retourne la prediction
def interference(symboling, width, height, engine_size)
    new_data = np.array([symboling, width, height, engine_size])             #on contruit un nouveau dataset à partir des Entrees utilisateurs
    pred = model(new_data, reshape(-1, 1))                                  #Calcul de prédiction avec le nouveau dataset
    return pred        


#L'utlisateur saisi une valeur pour chaque caracterisque de la voiture': en se basant sur pd.describe(), on définit les valeurs à saisir

#st.number_input : saisi valeur par le user sur streamlit + value par defaut
symboling = st.number_input(label = 'symboling', min_value=0, value=3)   
lenght = st.number_input('lenght:', value=150)  
width = st.number_input('width:', value=75)
height = st.number_input('height:', 50)
engine_size = st.number_input('engine_size:', 120)

# creation le bouton "Predict", qui retourne la prediction du modele quadnd on clique sur ce dernier 
if st.button("predict") :
    interference(symboling, width, height, engine_size) 
    resulat = " le prix (en dolars) de cette voiture  est égale à : " + str(prediction[0])
    st.success(resulat)







