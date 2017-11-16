from collections import defaultdict

def main():
    """
    take the combined mxm dataset (produced by CombineTestAndTrain) and merge it with the genres from msd-topMAGD-genreAssignment.cls
	this script outputs a dataset containing entries in the form of <track_id, mxm_id, genre, BOW>
	Author: Bryce Bodley-Gomes
    """

    BOW_file = open("mxm_dataset_combined.txt", "r") #bow id list
    genre_file = open("msd-topMAGD-genreAssignment.cls", "r") #genre id list
    combined_genre_bow_file = open("ourDataset.txt", "w+") #output
    #wipe out file contents in case this file already exists
    combined_genre_bow_file.seek(0)
    combined_genre_bow_file.truncate()

    genredictionary = defaultdict(float) #dictionary: id -> genre

    for line in genre_file: #read genres and ID from file to reduce disk access requests
        genredictionary[line.split("	")[0]] = line.split("	")[1][0:-1]

    genre_file.close() #no need for this file anymore


    for line in BOW_file: #itterate over all songs in file
        if line.startswith("#"  or line.startswith("%")):
            combined_genre_bow_file.write(line) #write out comments and instructions
        else:
            vec = line.split(',')
            if vec[0] in  genredictionary:
                theGenre = genredictionary[vec[0]]
                vec.insert(2, theGenre)
                outputLine = ",".join(vec)
                combined_genre_bow_file.write(outputLine)


















if __name__ == '__main__':
    main()

