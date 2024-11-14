from youtubesearchpython import VideosSearch
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from lyricsgenius import *


# Fonction pour créer le lien vers la vidéo YouTube
def create_link(title, artist):
    videosSearch = VideosSearch(title + " " + artist, limit=1)
    result = videosSearch.result()['result'][0]
    video_id = result['id']
    return f"https://www.youtube.com/embed/{video_id}", video_id


# Fonction pour obtenir les lyrics de la vidéo YouTube
def create_lyrics(video_id, title, artist):
    # S'il y a un probleme avec les paroles de Youtube alors on prendra les paroles de Genius
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['fr', 'en', 'es'])
        lyrics = "\n".join([line['text'] for line in transcript])
        return lyrics
    except TranscriptsDisabled:
        genius = Genius("cBe8YGq_s7vMRuVRx4L0XAiam8_zRAH8aX1yJaSadFNOdqJ5rwPVfK6eOuhFXfeQ") # Token de Genius
        song = genius.search_song(title, artist)
        return song.lyrics
