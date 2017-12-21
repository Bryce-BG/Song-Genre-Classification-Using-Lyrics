
def main():
    y_list = []  # a list of the genres for each song
    x_list = []  # a list of lists for the feature weights (the word counts for each song in a sparse list format)
    count = 0
    file = open("ourTrainDataset.txt", 'r')

    genreList = ['Reggae', 'Pop_Rock', 'Country', 'Jazz', 'Vocal', 'New Age', 'Latin', 'Rap', 'RnB', 'International',
                 'Blues', 'Electronic', 'Folk']

    genre_counts = {}

    for genre in genreList: #instantiate dictionary
        genre_counts[genre]=0


    outFile =  open("ourBalancedTrainDataset.txt", "w+")
    for line in file:
        if line.startswith('%') or line.startswith('#'):
            outFile.write(line)
        else:
            arr = line.split(',')
            if genre_counts[arr[2]] <1000: #cap value for number of songs
                genre_counts[arr[2]] +=1
                outFile.write(line)
    file.close()

    print genre_counts






    #


if __name__ == '__main__':
    main()