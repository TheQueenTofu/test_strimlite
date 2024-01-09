import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement des données
donnees = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

# Création du widget pour sélectionner la région
region_selector = st.selectbox('Région:', ['Toutes les régions', 'US', 'Europe', 'Japon'])

# Fonction de mise à jour du graphique en fonction de la région sélectionnée
def update_plot(region):
    plt.clf()  # Effacer le graphique précédent
    plt.figure(figsize=(12, 6))
    
    # Filtrer les données en fonction de la région sélectionnée
    filtered_data = donnees if region == 'Toutes les régions' else donnees[donnees['Region'] == region]

    # Tracé de la distribution de chaque variable pour la région sélectionnée
    for i, col in enumerate(filtered_data.columns):
        plt.subplot(2, len(filtered_data.columns)//2, i+1)
        sns.histplot(filtered_data[col], kde=True)
   
