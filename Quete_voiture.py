import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement des données
donnees = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

# Remove trailing period from 'continent' values
donnees['continent'] = donnees['continent'].str.strip('.')


# Création du widget pour sélectionner le continent
continent_selector = st.selectbox('Continent:', ['Tous les continents', 'US', 'Europe', 'Japan'])

# Titre de l'application
st.title("Analyse data des voitures entre les US, l'Europe et le Japon")

# Fonction de mise à jour du graphique en fonction du continent sélectionné
# Fonction de mise à jour du graphique en fonction du continent sélectionné
def update_plot(continent):
    # Set Seaborn context to avoid tight layout issues
    sns.set_context(rc={"lines.linewidth": 0.8})

    plt.figure(figsize=(16, 8))
    
    # Filtrer les données en fonction du continent sélectionné
    filtered_data = donnees if continent == 'Tous les continents' else donnees[donnees['continent'] == continent]

    # Remove trailing periods and spaces in 'continent' column
    filtered_data['continent'] = filtered_data['continent'].str.strip('.')

    # Display filtered_data for debugging
    st.write("Filtered Data:", filtered_data)

    # Check for NaN values in filtered_data
    st.write("NaN Values in filtered_data:", filtered_data.isnull().sum())

    # Tracé de la distribution de chaque variable pour le continent sélectionné
    for i, col in enumerate(filtered_data.columns[:-1]):
        plt.subplot(2, 4, i+1)
        sns.histplot(filtered_data[col], kde=True)
        plt.title(f'Distribution de {col}')

    # Afficher le heatmap de corrélation
    plt.subplot(2, 4, 8)
    correlation_matrix = filtered_data.corr()

    # Display correlation matrix for debugging
    st.write("Correlation Matrix:", correlation_matrix)

    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=.5)
    plt.title("Heatmap de Corrélation")

    # Tracé de nuages de points pour les paires de variables corrélées pour le continent sélectionné
    plt.subplot(2, 4, 5)
    sns.pairplot(filtered_data, diag_kind='kde')
    plt.suptitle(f'Nuages de points pour les paires de variables corrélées ({continent})')

    return plt



# Afficher le widget et le graphique initial
selected_continent = continent_selector
if selected_continent != 'Tous les continents':
    st.pyplot(update_plot(selected_continent))
else:
    st.warning("Sélectionnez un continent pour afficher le graphique.")
