import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Chargement des données (remplacez 'votre_fichier.csv' par le nom de votre fichier de données)
donnees = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

# Création d'un widget pour sélectionner le continent
continent_selector = st.selectbox('Sélectionnez un continent', ['Tous les continents', 'US', 'Europe', 'Japan'])

# Filtrer les données en fonction du continent sélectionné
if continent_selector != 'Tous les continents':
    filtered_data = donnees[donnees['continent'] == continent_selector]
else:
    filtered_data = donnees

# Affichage du titre
st.title("Analyse des données des voitures entre les US, l'Europe et le Japon")

# Afficher le nombre de données disponibles pour le continent sélectionné
st.write(f"Nombre de données pour le continent {continent_selector}: {len(filtered_data)}")

# Afficher les statistiques descriptives
st.write("Statistiques descriptives:")
st.write(filtered_data.describe())

# Afficher les colonnes uniques de la colonne 'continent'
st.write("Uniques valeurs dans la colonne 'continent':", filtered_data['continent'].unique())

# Afficher le nuage de points pour les variables corrélées
st.write(f'Nuage de points pour les variables corrélées ({continent_selector}):')
sns.pairplot(filtered_data, diag_kind='kde')
st.pyplot()

# Afficher le heatmap de corrélation
st.write(f"Heatmap de corrélation ({continent_selector}):")
correlation_matrix = filtered_data.select_dtypes(include=['float64', 'int64']).corr().fillna(0)
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=.5)
st.pyplot()
