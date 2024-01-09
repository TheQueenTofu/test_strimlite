import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement des données
donnees = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

# Print column names to check the correct name
st.write("Column Names:", donnees.columns)

# Création du widget pour sélectionner la région
region_selector = st.selectbox('Région:', ['Toutes les régions', 'US', 'Europe', 'Japon'])

# Fonction de mise à jour du graphique en fonction de la région sélectionnée
def update_plot(region):
    plt.figure(figsize=(12, 6))
    
    # Filtrer les données en fonction de la région sélectionnée
    filtered_data = donnees if region == 'Toutes les régions' else donnees[donnees['Continent'] == region]

    # Tracé de la distribution de chaque variable pour la région sélectionnée
    for i, col in enumerate(filtered_data.columns):
        plt.subplot(2, len(filtered_data.columns)//2, i+1)
        sns.histplot(filtered_data[col], kde=True)
        plt.title(f'Distribution de {col}')
        plt.tight_layout()

    # Tracé de nuages de points pour les paires de variables corrélées pour la région sélectionnée
    sns.pairplot(filtered_data, diag_kind='kde')
    plt.suptitle(f'Nuages de points pour les paires de variables corrélées ({region})')

    return plt

# Afficher le widget et le graphique initial
selected_region = region_selector
if selected_region != 'Toutes les régions':
    st.pyplot(update_plot(selected_region))
else:
    st.warning("Sélectionnez une région pour afficher le graphique.")
