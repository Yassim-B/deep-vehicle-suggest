from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics.pairwise import euclidean_distances

app = Flask(__name__)
CORS(app)

# Chargement et prétraitement des données au démarrage de l'application
df = pd.read_csv('./data/vehicles.csv')

# Sélection des colonnes numériques pour le calcul de la moyenne et le prétraitement
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
means = df[numeric_columns].mean()
df.fillna(means, inplace=True)

# Encodage de la variable catégorielle Motorisation
motorisation_encoder = LabelEncoder()
df['Motorisation'] = motorisation_encoder.fit_transform(df['Motorisation'])

# Création d'un dictionnaire inversé pour mapper les entiers aux libellés de motorisation
motorisation_labels = dict(zip(motorisation_encoder.classes_, motorisation_encoder.transform(motorisation_encoder.classes_)))

# Sélection des caractéristiques pertinentes pour l'entraînement du modèle
features = df[['Sieges', 'Consommation', 'Prix', 'Design', 'Kilometrage', 'Motorisation']]

# Standardisation des données
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Entraînement du modèle KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(features_scaled)

# Fonction pour recommander les véhicules les plus proches
def get_nearest_vehicles(scaler, df, sieges, consommation, prix, design, kilometrage_maxi, motorisation):
    # Préparation des données de l'utilisateur
    user_data = pd.DataFrame({
        'Sieges': [sieges],
        'Consommation': [consommation],
        'Prix': [prix],
        'Design': [design],
        'Kilometrage': [kilometrage_maxi],
        'Motorisation': [motorisation_encoder.transform([motorisation])[0]]
    })

    # Standardisation des données de l'utilisateur
    user_data_scaled = scaler.transform(user_data)

    # Standardisation des données du dataset
    features_scaled = scaler.transform(features)

    # Calcul des distances euclidiennes
    distances = euclidean_distances(user_data_scaled, features_scaled).flatten()

    # Ajout des distances au dataframe
    df['Distance'] = distances

    # Triage des véhicules par distance et retour des plus proches
    nearest_vehicles = df.sort_values(by='Distance').head(50).reset_index(drop=True)  # Limite à 50 véhicules

    # Mapper les entiers de motorisation aux libellés correspondants
    nearest_vehicles['Motorisation'] = motorisation_encoder.inverse_transform(nearest_vehicles['Motorisation'])

    return nearest_vehicles

# Route POST pour recommander les véhicules
@app.route('/recommander', methods=['POST'])
def recommander():
    data = request.json

    sieges = data.get('sieges')
    consommation = data.get('consommation')
    prix = data.get('prix')
    design = data.get('design', None)
    kilometrage_maxi = data.get('kilometrage_maxi', None)
    motorisation = data.get('motorisation', None)

    recommendations = get_nearest_vehicles(scaler, df, sieges, consommation, prix, design, kilometrage_maxi, motorisation)

    # Ajouter la propriété count avec le nombre de véhicules recommandés
    count = recommendations.shape[0]
    response = {
        'count': count,
        'vehicles': recommendations.to_dict(orient='records')
    }

    return jsonify(response)

# Route GET de test pour vérifier si l'API fonctionne
@app.route('/coucou', methods=['GET'])
def coucou():
    return "coucou"

if __name__ == '__main__':
    app.run(debug=True)
