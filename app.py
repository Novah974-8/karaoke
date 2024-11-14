from flask import Flask, request, render_template, redirect, url_for
import sqlite3
from api import create_link, create_lyrics  # Importation des fonctions depuis api.py
import multiprocessing

# Je cree de serveur Flask un pour la video et un pour le formulaire
app_form = Flask(__name__)
app_video = Flask(__name__)

# Fonction pour se connecter à la base de données
def get_db_connection():
    conn = sqlite3.connect('data/chansons.db')  # Base de données en local
    conn.row_factory = sqlite3.Row
    return conn

# Route pour la page d'accueil avec le formulaire de soumission
@app_form.route('/')
def index():
    return render_template('index.html')

# Route pour traiter la soumission du formulaire
@app_form.route('/submit', methods=['POST'])
def submit():
    # Récupérer les données du formulaire
    username = request.form['username']
    artist = request.form['artist']
    title = request.form['title']

    # Connexion à la BDD
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Ajouter la chanson à la base de données
    cursor.execute('''
        INSERT INTO DATA (TITLE, ARTIST, PSEUDO)
        VALUES (?, ?, ?)''', (title, artist, username))
    conn.commit()
    
    # Récupérer l'ID
    cursor.execute('SELECT ID FROM DATA WHERE PSEUDO = ? AND TITLE = ?', (username, title))
    id = cursor.fetchone()[0] -1 # -1 pour que qu'il dit il reste combien de chanson
    conn.close()

    # Rediriger vers la page de détails avec les informations soumises
    return redirect(url_for('index_finish',id=str(id), username=username, artist=artist, title=title))

# Route pour afficher les détails après la soumission
@app_form.route('/details')
def index_finish():
    id = request.args.get('id')
    username = request.args.get('username')
    artist = request.args.get('artist')
    title = request.args.get('title')

    return render_template('index_finish.html',id=id, username=username, artist=artist, title=title)


# Route pour afficher la vidéo et les lyrics dans karaoke.html
@app_video.route('/') 
def serveur():
    # Récupérer les informations de la chanson depuis la base de données
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT TITLE, ARTIST, PSEUDO FROM DATA WHERE ID = (SELECT MIN(ID) FROM DATA);')
    song_data = cursor.fetchone()

    
    # Si les données existent, récupérer la vidéo YouTube et les lyrics
    try:
        title, artist, pseudo = song_data
        video_url, video_id = create_link(title, artist)  # Obtenir l'URL de la vidéo YouTube
        lyrics = create_lyrics(video_id, title, artist)  # Obtenir les lyrics via l'API YouTube Transcript
        
        cursor.execute('DELETE FROM DATA WHERE ID = (SELECT MIN(ID) FROM DATA);')
        conn.commit()
        conn.close()

        return render_template('karaoke.html', video_url=video_url, lyrics=lyrics, title=title, artist=artist, pseudo=pseudo)
    
    except:
        cursor.execute('DELETE FROM DATA WHERE ID = (SELECT MIN(ID) FROM DATA);')
        conn.commit()
        conn.close()
        
        return render_template('404.html')

def run_form():
    app_form.run(host='0.0.0.0', port=80, debug=False)

def run_video():
    app_video.run(host='localhost', port=8000, debug=False)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=run_form)
    p2 = multiprocessing.Process(target=run_video)
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
