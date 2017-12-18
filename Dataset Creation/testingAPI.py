from musixmatch import Musixmatch
import pickle
import json

apiKey = ""
musixmatch = Musixmatch(apiKey)

def main():
    #result = musixmatch.track_get(track_id=8457641) #1 (get song information)
    #result = musixmatch.track_lyrics_get(track_id=8457641)
    #pickle.dump(result, open("save2.p", "wb"))

    # Load the variable back from the pickle file.

    result = pickle.load(open("save2.p", "rb"))


    #print result["message"]['body']['lyrics']['lyrics_body']



    good = open("ourDataset.txt", "r")  #read in the dataset

    outputFile = open("lyricsDataset.txt", "w+")

    for line in good:
        if line.startswith("#")  or line.startswith("%"):
            continue
        else:
            line
            #result = musixmatch.track_lyrics_get(track_id=8457641)


    print result["message"]['body']['lyrics']['lyrics_body'].rstrip("\n...\n*******This Lyrics is NOT for Commercial use *******")

    #some= json.loads(result)




if __name__ == '__main__':
    main()