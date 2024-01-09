import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement des données
donnees = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

# Print column names to check the correct name
st.write("Column Names:", donnees.columns)

# Remove trailing period from 'continent' values
donnees['continent'] = donnees['continent'].str.rstrip('.')

# Création du widget pour sélectionner le continent
continent_selector = st.selectbox('Continent:', ['Tous les continents', 'US', 'Europe', 'Japan'])

# Fonction de mise à jour du graphique en fonction du continent sélectionné
def update_plot(continent):
    plt.figure(figsize=(12, 6))
    
    # Filtrer les données en fonction du continent sélectionné
    filtered_data = donnees if continent == 'Tous les continents' else donnees[donnees['continent'] == continent]

    # Tracé de la distribution de chaque variable pour le continent sélectionné
    for i, col in enumerate(filtered_data.columns):
        plt.subplot(2, len(filtered_data.columns)//2, i+1)
        sns.histplot(filtered_data[col], kde=True)
        plt.title(f'Distribution de {col}')
        plt.tight_layout()

    # Tracé de nuages de points pour les paires de variables corrélées pour le continent sélectionné
    sns.pairplot(filtered_data, diag_kind='kde')
    plt.suptitle(f'Nuages de points pour les paires de variables corrélées ({continent})')

    return plt

# Afficher le widget et le graphique initial
selected_continent = continent_selector
if selected_continent != 'Tous les continents':
    st.pyplot(update_plot(selected_continent))
else:
    st.warning("Sélectionnez un continent pour afficher le graphique.")
