word=input("que palabra no entiendes")
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "FACTOS":"una verdad muy dura",
            "AFK":"quedarse quieto"
            }
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("pon otra no tengo esa")