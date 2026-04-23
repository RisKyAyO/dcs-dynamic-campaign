# ✈️ DCS Dynamic Campaign

Un moteur de **campagne dynamique** pour [DCS World](https://www.digitalcombatsimulator.com/), inspiré de [DCS Liberation](https://github.com/dcs-liberation/dcs_liberation). Génère des missions aléatoires, suit l'état du front et simule l'évolution d'une campagne aérienne.

> Projet personnel — pas d'affiliation avec Eagle Dynamics.

## 🎯 Fonctionnalités

- Génération aléatoire de missions (STRIKE, CAP, CAS, SEAD, RECON)
- Suivi du score Blue/Red basé sur les résultats de missions
- 3 théâtres disponibles : Caucase, Syrie, Golfe Persique
- Sauvegarde/chargement de campagne en JSON
- Rapport d'état détaillé par jour

## 🚀 Utilisation

```bash
python campaign.py
```

Ou importer dans ton propre script :

```python
from campaign import Campaign

camp = Campaign(theater="Syria", name="Opération Levant")
mission = camp.generate_mission()
print(mission)
camp.complete_mission(mission.id, success=True)
camp.next_day()
camp.status_report()
camp.save("ma_campagne.json")
```

## 📁 Structure

```
dcs-dynamic-campaign/
├── campaign.py      # Moteur principal (Mission, Campaign)
├── theaters.py      # Données des théâtres (terrains, cibles)
└── README.md
```

## 🗺️ Théâtres supportés

| Théâtre     | Zone                          |
|-------------|-------------------------------|
| Caucasus    | Géorgie / Russie              |
| Syria       | Syrie / Méditerranée orientale |
| PersianGulf | Iran / EAU / Golfe Persique   |

## 🔮 Idées d'évolution

- Interface web Flask pour visualiser le front sur une carte
- Intégration avec l'API Mission Editor de DCS (Lua)
- Gestion d'un escadron avec des pilotes nommés et un carnet de vol

## 📝 Licence

MIT
