# Karaoké 🎤

Une application web de karaoké qui permet aux utilisateurs de soumettre et de chanter leurs chansons préférées avec les paroles.

## Fonctionnalités

- Soumission de chansons avec nom d'utilisateur, artiste et titre
- Lecture de vidéos YouTube intégrées
- Affichage automatique des paroles
- Système de file d'attente pour les chansons
- Interface utilisateur intuitive et responsive

## Prérequis

- Python 3.8 ou supérieur
- Autres dépendances Python (voir section Installation)

## Installation

Installez les dépendances :

Dans un terminal écriver:
```bash
pip install flask
pip install youtube-search-python
pip install youtube-transcript-api
pip install lyricsgenius
```

## Lancement

Pour démarrer l'application :

Toujours dans un terminal
```bash
python app.py
```

L'application lance deux serveurs :
- Serveur du formulaire : http://0.0.0.0:80
    Ce serveur sert à remplir un formulaire afin de choisir sa chanson.
    De plus il sera acccéssible sur tout les équipement de votre réseaux en tapant dans un navigateur votre addresse IP.

- Serveur de lecture : http://localhost:8000
    Ce sert sert a afficher les parole et la video.
    Il sera accéssible uniquement sur l'ordianteur qui aura lancé le serveur pour des raison de liscence

## Structure du Projet

```
karaoke-en-ligne/
├── app.py              # Application principale Flask
├── api.py             # Fonctions d'API pour YouTube et Genius
├── data/
│   └── chansons.db    # Base de données SQLite
├── templates/
│   ├── index.html     # Page du formulaire
│   ├── karaoke.html   # Page de lecture
│   └── index_finish.html  # Page de confirmation
└── static/
    └── css/            # Styles CSS
        └── index.css    
        └── index_finish.css
        └── karaoke.css
```

## Configuration des API

L'application utilise deux API externes :
1. YouTube Data API (via youtube-search-python)
2. Genius API pour les paroles

## Utilisation

1. Accédez à la page principale (port 80)
2. Soumettez une chanson avec :
   - Votre nom d'utilisateur
   - Le nom de l'artiste
   - Le titre de la chanson
3. Accédez à la page de karaoké (port 8000) sur l'ordinateur qui l'a lancé
4. Attendez votre tour
6. Chanter !!!

## Contributeurs

- Noah Techer
- Anthony Hoareau
- Miguel Ilata

## Notes Importantes

- L'application nécessite une connexion Internet stable pour la lecture des vidéos YouTube
- Les paroles sont récupérées automatiquement via YouTube Transcript API ou Genius
- En cas d'échec de récupération des paroles via YouTube, le système bascule automatiquement sur Genius

## Token

Génius: cBe8YGq_s7vMRuVRx4L0XAiam8_zRAH8aX1yJaSadFNOdqJ5rwPVfK6eOuhFXfeQ
>>>>>>> 51491c6 (Premier commit - import du projet)
>>>>>>> 190119f (Ajout du projet Karaoke)
