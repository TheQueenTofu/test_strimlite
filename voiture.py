# Chargement des données (remplacez 'votre_fichier.csv' par le nom de votre fichier de données)
donnees = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

# Analyse de corrélation
correlation_matrix = donnees.corr()

# Tracé d'une carte thermique (heatmap) de la matrice de corrélation
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matrice de corrélation')
plt.show()

# Tracé de la distribution de chaque variable
plt.figure(figsize=(12, 6))
for i, col in enumerate(donnees.columns):
    plt.subplot(2, len(donnees.columns)//2, i+1)
    sns.histplot(donnees[col], kde=True)
    plt.title(f'Distribution de {col}')
    plt.tight_layout()

# Tracé de nuages de points pour les paires de variables corrélées
sns.pairplot(donnees, diag_kind='kde')
plt.suptitle('Nuages de points pour les paires de variables corrélées')
plt.show()

