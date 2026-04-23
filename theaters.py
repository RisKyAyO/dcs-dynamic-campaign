"""
Donnees des theatres d'operations disponibles dans DCS World.
"""

THEATERS = {
    "Caucasus": {
        "description": "Theatre du Caucase -- zone de conflit Georgie/Russie",
        "airfields": {
            "blue": ["Batumi", "Kobuleti", "Kutaisi", "Tbilisi-Lochini"],
            "red":  ["Maykop-Khanskaya", "Krymsk", "Anapa", "Mozdok"],
        },
        "targets": [
            "SAM site Gudauta", "Pont de Zugdidi", "Depot de Sokhumi",
            "Radar de Gudauta", "Convoi N1 RN10", "Base d'Anapa",
            "POL Krymsk", "QG blinde de Tskhinvali",
        ],
    },
    "Syria": {
        "description": "Theatre de Syrie -- Mediterranee orientale",
        "airfields": {
            "blue": ["Ramat David", "Hatzerim", "Incirlik"],
            "red":  ["Bassel Al-Assad", "Tiyas", "Shayrat"],
        },
        "targets": [
            "SAM site Palmyra", "Entrepot d'Alep", "Depot de Deir ez-Zor",
            "Pont de l'Euphrate", "QG de Hama", "Raffinerie de Homs",
            "Radar cotier Lattaquie", "Base navale de Tartous",
        ],
    },
    "PersianGulf": {
        "description": "Theatre du Golfe Persique",
        "airfields": {
            "blue": ["Al Dhafra", "Al Minhad", "Al Ain"],
            "red":  ["Bandar Abbas", "Havadarya", "Sirri Island"],
        },
        "targets": [
            "Plateforme petroliere Sirri", "SAM site de Bandar Abbas",
            "Radar de Havadarya", "Depot de missiles Qeshm",
            "Fregate IRIN au large", "POL Bandar-e Lengeh",
        ],
    },
}
