#written by: Raneem Tarfa

import urllib.request
#note: can transform this to retreive random facts about the song from the net

from googletrans import Translator
translator = Translator()




artist_name= input("Input the artist name: ").strip().lower()
song_title= input("Input your song title (please include accents): ").strip().lower()
dest_lang= input("Translate to: ")

# def lyric_search(search_term, api_key, cse_id, **kwargs):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
#     return res
#
# result = lyric_search(artist_name+" "+song_title, my_api_key, my_cse_id)
# print(result) #print anything that starts with https://www.azlyrics.com/lyrics/artist/song.html

try:
    # if any of letters in song title or artist name has an accent or apostrophe/punctuation remove it
    artist_name = artist_name.replace(" ","")
    song_title = song_title.replace(" ","")
    foreign_letters = "àèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûðÂÊÎÔÛÐãñõÃÑÕäëïöüÿÄËÏÖÜŸåÅæœÆŒßçÇøØ¿¡"

    # this is very slow.. diff way to do this?
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

#issues:

#should try to let ppl write without accents (maybe need to do a google search instead..)
#prob num 2- doesnt have original text (i.e. arabic or korean and google translate can't do romanisation
#prob num 3- prints 3 times if has romanization, original, and translation
        #     (maybe if '[English translation:]' on page, print everything after that

#not all results show up (i.e. stromae)
#artists have different names (bangtan vs BTS)
#maybe do a try: except: print azlyrics does not have this song
#need dictionary keys depending on destination language
#https://sites.google.com/site/opti365/translate_codes

#do a strip/split <i>[?]</i> and that kind of stuff

#https://www.w3schools.com/python/python_json.asp
#https://linuxhint.com/google_search_api_python/
#https://pypi.org/project/googletrans/


#maybe print original ("original (english)") on left, translated ("translated (spanish)") lang on right

#in the try, catch: can look at other sites as well to see as many sites as possible, keep doing that

