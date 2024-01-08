import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Chargement des données (remplacez 'votre_fichier.csv' par le nom de votre fichier de données)
donnees = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

# Création d'un widget pour sélectionner la région
region_selector = widgets.Dropdown(
    options=['Toutes les régions', 'US', 'Europe', 'Japon'],
    value='Toutes les régions',
    description='Région:'
)

# Fonction de mise à jour du graphique en fonction de la région sélectionnée
def update_plot(region):
    plt.clf()  # Effacer le graphique précédent
    plt.figure(figsize=(12, 6))
    
    # Filtrer les données en fonction de la région sélectionnée
    if region != 'Toutes les régions':
        filtered_data = donnees[donnees['Region'] == region]
    else:
        filtered_data = donnees
    
    # Tracé de la distribution de chaque variable pour la région sélectionnée
    for i, col in enumerate(filtered_data.columns):
        plt.subplot(2, len(filtered_data.columns)//2, i+1)
        sns.histplot(filtered_data[col], kde=True)
        plt.title(f'Distribution de {col}')
        plt.tight_layout()

    # Tracé de nuages de points pour les paires de variables corrélées pour la région sélectionnée
    sns.pairplot(filtered_data, diag_kind='kde')
    plt.suptitle(f'Nuages de points pour les paires de variables corrélées ({region})')
    plt.show()

# Associer la fonction de mise à jour au changement de la valeur du widget
widgets.interactive(update_plot, region=region_selector)

# Afficher le widget et le graphique initial
display(region_selector)
update_plot('Toutes les régions')
