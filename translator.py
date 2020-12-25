#written by: Raneem Tarfa

import urllib.request
#note: can transform this to retreive random facts about the song from the net

from googletrans import Translator
translator = Translator()




artist_name= input("Input the artist name: ").strip().lower()
song_title= input("Input your song title (please include accents): ").strip().lower()
dest_lang= input("Translate to: ")


try:
    # if any of letters in song title or artist name has an accent or apostrophe/punctuation remove it
    artist_name = artist_name.replace(" ","")
    song_title = song_title.replace(" ","")
    foreign_letters = "àèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûðÂÊÎÔÛÐãñõÃÑÕäëïöüÿÄËÏÖÜŸåÅæœÆŒßçÇøØ¿¡"

    for char in artist_name:
        if char in foreign_letters:
            artist_name = artist_name.replace(char, "")

    for char in song_title:
        if char in foreign_letters:
            song_title = song_title.replace(char, "")

    url= "https://www.azlyrics.com/lyrics/"+artist_name+"/"+song_title+".html"
    fstream = urllib.request.urlopen(url)
    page_text = fstream.read().decode('utf-8').strip()
    start = 'Sorry about that. -->'
    end = '<!-- MxM banner -->'
    s = page_text
    s=(s.split(start))[1].split(end)[0]
    lyrics=s.replace("<br>","").replace("</div>","").replace("</i>","").replace("<i>","")
except:
    #for foreign songs, replace letter with eng counterpart (use a dict for this)
    artist_name = artist_name.replace(" ", "-")
    song_title = song_title.replace(" ", "-")
    url= "https://genius.com/"+artist_name+"-"+song_title+"-lyrics"
    fstream = urllib.request.urlopen(url)
    page_text = fstream.read().decode('utf-8').strip()

translation = translator.translate(lyrics, dest=dest_lang)
print(translation.text)
