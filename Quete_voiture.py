import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Chargement des données (remplacez 'votre_fichier.csv' par le nom de votre fichier de données)
donnees = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

# Nettoyer les espaces et les points dans la colonne 'continent'
donnees['continent'] = donnees['continent'].str.strip().str.rstrip('.')

# Création d'un widget pour sélectionner le continent
continent_selector = widgets.Dropdown(
    options=['Tous les continents', 'US', 'Europe', 'Japan'],
    value='Tous les continents',
    description='Continent:'
)

# Fonction de mise à jour du graphique en fonction du continent sélectionné
def update_plot(continent):
    # Set Seaborn context to avoid tight layout issues
    sns.set_context(rc={"lines.linewidth": 0.8})

    plt.figure(figsize=(16, 8))
    
    # Filtrer les données en fonction du continent sélectionné
    filtered_data = donnees if continent == 'Tous les continents' else donnees[donnees['continent'] == continent]

    if filtered_data.empty:
        widgets.warning(f"Aucune donnée disponible pour le continent {continent}. Veuillez sélectionner un autre continent.")
        return plt

    # Tracé de la distribution de chaque variable pour le continent sélectionné
    for i, col in enumerate(filtered_data.columns[:-1]):
        plt.subplot(2, 4, i+1)
        sns.histplot(filtered_data[col], kde=True)
        plt.title(f'Distribution de {col}')

    # Afficher le heatmap de corrélation
    plt.subplot(2, 4, 8)
    correlation_matrix = filtered_data.corr().fillna(0)
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=.5)
    plt.title("Heatmap de Corrélation")

    # Tracé de nuages de points pour les paires de variables corrélées pour le continent sélectionné
    plt.subplot(2, 4, 5)
    sns.pairplot(filtered_data, diag_kind='kde')
    plt.suptitle(f'Nuages de points pour les paires de variables corrélées ({continent})')

    plt.show()

# Associer la fonction de mise à jour au changement de la valeur du widget
widgets.interactive(update_plot, continent=continent_selector)

# Afficher le widget et le graphique initial
display(continent_selector)
update_plot('Tous les continents')
