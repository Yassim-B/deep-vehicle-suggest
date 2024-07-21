import pandas as pd
import random

# Listes de marques et modèles pour différents types de véhicules
marques_modeles_voiture = {
    'Toyota': ['Corolla', 'Camry', 'Prius', 'RAV4', 'Highlander', 'Yaris', 'C-HR', 'Avalon', 'Land Cruiser', 'Supra', 'Tacoma'],
    'Honda': ['Civic', 'Accord', 'CR-V', 'Pilot', 'Fit', 'Odyssey', 'HR-V', 'Passport', 'Ridgeline', 'Insight', 'Clarity'],
    'BMW': ['Série 3', 'Série 5', 'X3', 'X5', 'Série 7', 'X1', 'X6', 'Z4', 'M3', 'M5', 'i8'],
    'Ford': ['Focus', 'Mustang', 'Escape', 'Explorer', 'Fiesta', 'Edge', 'Fusion', 'Expedition', 'Bronco', 'F-150', 'Ranger'],
    'Chevrolet': ['Cruze', 'Malibu', 'Equinox', 'Tahoe', 'Spark', 'Traverse', 'Impala', 'Trailblazer', 'Silverado', 'Blazer', 'Bolt'],
    'Nissan': ['Sentra', 'Altima', 'Rogue', 'Murano', 'Versa', 'Pathfinder', 'Maxima', 'Kicks', 'Leaf', 'GT-R', 'Titan'],
    'Hyundai': ['Elantra', 'Sonata', 'Tucson', 'Santa Fe', 'Kona', 'Accent', 'Palisade', 'Veloster', 'Ioniq', 'Nexo', 'Venue'],
    'Kia': ['Forte', 'Optima', 'Sportage', 'Sorento', 'Soul', 'Telluride', 'Rio', 'Stinger', 'Seltos', 'Carnival', 'K900'],
    'Volkswagen': ['Jetta', 'Passat', 'Tiguan', 'Atlas', 'Golf', 'Beetle', 'Arteon', 'ID.4', 'Taos', 'Polo', 'Touareg'],
    'Mercedes': ['Classe C', 'Classe E', 'GLC', 'GLE', 'Classe A', 'Classe S', 'GLA', 'GLB', 'CLS', 'Classe G', 'AMG GT'],
    'Audi': ['A3', 'A4', 'A6', 'Q5', 'Q7', 'Q3', 'A8', 'Q8', 'TT', 'R8', 'e-tron'],
    'Lexus': ['ES', 'RX', 'NX', 'GX', 'IS', 'UX', 'LS', 'LX', 'RC', 'LC', 'HS'],
    'Mazda': ['Mazda3', 'Mazda6', 'CX-5', 'CX-9', 'MX-5', 'CX-3', 'CX-30', 'Mazda2', 'RX-8', 'BT-50', 'MPV'],
    'Subaru': ['Impreza', 'Legacy', 'Outback', 'Forester', 'Crosstrek', 'Ascent', 'BRZ', 'WRX', 'Levorg', 'Exiga', 'Tribeca'],
    'Tesla': ['Model S', 'Model 3', 'Model X', 'Model Y', 'Roadster', 'Cybertruck'],
    'Volvo': ['S60', 'S90', 'XC40', 'XC60', 'XC90', 'V60', 'V90', 'S40', 'C30', 'S80', 'V50'],
    'Porsche': ['911', 'Cayenne', 'Macan', 'Panamera', 'Taycan', 'Boxster', 'Cayman'],
    'Jaguar': ['XE', 'XF', 'XJ', 'E-PACE', 'F-PACE', 'I-PACE', 'F-TYPE'],
    'Land Rover': ['Range Rover', 'Discovery', 'Defender', 'Evoque', 'Velar', 'Freelander'],
    'Ferrari': ['488', '812 Superfast', 'Portofino', 'GTC4Lusso', 'F8 Tributo', 'SF90 Stradale'],
    'Lamborghini': ['Huracan', 'Aventador', 'Urus', 'Gallardo', 'Murcielago'],
    'Aston Martin': ['DB11', 'Vantage', 'DBS', 'Rapide', 'Vanquish', 'DBX'],
    'Bentley': ['Continental', 'Bentayga', 'Flying Spur', 'Mulsanne'],
    'Rolls-Royce': ['Phantom', 'Ghost', 'Wraith', 'Dawn', 'Cullinan'],
    'Maserati': ['Ghibli', 'Levante', 'Quattroporte', 'GranTurismo', 'GranCabrio'],
}

types_moteur = [
    'Essence', 'Diesel', 'Électrique'
]

def voiture_aleatoire():
    marque = random.choice(list(marques_modeles_voiture.keys()))
    modele = random.choice(marques_modeles_voiture[marque])
    sieges = random.randint(1, 7)  # Supposons que les voitures ont entre 1 et 7 sièges
    consommation = round(random.uniform(5, 15), 1)  # Consommation aléatoire entre 5 et 15 litres/100km
    prix = random.randint(15000, 100000)  # Prix aléatoire entre 15,000 et 100,000 euros
    design = round(random.uniform(3, 5), 1)  # Design aléatoire entre 3 et 5 étoiles
    motorisation = random.choice(types_moteur)
    kilometrage = random.randint(0, 300000)  # Kilométrage aléatoire entre 0 et 300 000 km

    return {
        'Marque': marque,
        'Modele': modele,
        'Sieges': sieges,
        'Consommation': consommation,
        'Prix': prix,
        'Design': design,
        'Motorisation': motorisation,
        'Type': 'Voiture',
        'Kilometrage': kilometrage  # Ajout de la colonne 'Kilometrage'
    }

# Générer un jeu de données de voitures
voitures = [voiture_aleatoire() for _ in range(1000)]  # Générer 1000 voitures aléatoires

# Convertir en DataFrame
df = pd.DataFrame(voitures)

# Sauvegarder en CSV
df.to_csv('./../vehicles.csv', index=False)
