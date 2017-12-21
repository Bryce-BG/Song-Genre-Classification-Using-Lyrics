import numpy as np
from sklearn.cluster import KMeans
import warnings
warnings.simplefilter("ignore", DeprecationWarning)

"""
A script that calls the sklearn's implementation of the kmeans algorithm on our dataset to train for our dataset. 
Then we use these weights to make predictions on our test dataset and output the accuracy of the algorithm on our dataset.
Due to initial innaccuracies in the clustering I created another script "balancedataset.py" that should filter our dataset 
to contain rouphly equal distributions for each genre. This script also loops over each song and then find in which cluster
the majority of the songs for each genre reside. That cluster is defined as the cluster representing that genre. Unfortunitly,
looking at the results it is still clear that the clusters are not accuratly encompossing a specific genre (though it did
increase accuracy from 23 ->35% accuracy).
Author(s): Bryce Bodley-Gomes

"""


def main():
    y_list = []  # a list of the genres for each song
    x_list = []  # a list of lists for the feature weights (the word counts for each song in a sparse list format)
    count = 0
    file = open("ourBalancedTrainDataset.txt", 'r') #changed
    for line in file:
        if line.startswith('%') or line.startswith('#'):
            pass
        else:
            # if count>100:
            #     break
            # count +=1
            wordVal = line.split(',')
            y_list.append(wordVal[2])

            wordVal = wordVal[3:]
            weightx = [0] * 5000
            for x in wordVal:
                weightx[int(x.split(':')[0]) - 1] = int(x.split(':')[1].rstrip())
            x_list.append(weightx)
    file.close()
    print "finished reading"

            # convert lists into numpy arrays
    X = np.array(x_list)
    #Y = np.array(y_list)

    classifier  = KMeans(n_clusters=13)



    classifier.fit(X)  # run firt function on the dataset


    print "Finished Training"



    #Identify what cluster maps to what genre
    genreList = ['Reggae', 'Pop_Rock', 'Country', 'Jazz', 'Vocal', 'New Age', 'Latin', 'Rap', 'RnB', 'International', 'Blues','Electronic', 'Folk']
    genre_to_cluster_mapping = {}

    count = 0
    file = open("ourTrainDataset.txt", 'r') #using full set to more accuratly determien if cluster center aligns
    for line in file:
        if line.startswith('%') or line.startswith('#'):
            pass
        else:
            # if count > 200:
            #     break
            # count += 1
            wordVal = line.split(',')
            genre = wordVal[2]
            resultTempstring = str(classifier.predict(makevec(line)))
            if genre in genre_to_cluster_mapping:
                if resultTempstring in genre_to_cluster_mapping[genre]:
                    genre_to_cluster_mapping[genre][resultTempstring] +=1
                else:
                    genre_to_cluster_mapping[genre][resultTempstring] =1

            else:
                genre_to_cluster_mapping[genre] = {}
                genre_to_cluster_mapping[genre][resultTempstring] =1
    file.close()

    #just to make sure it looks like it mapped correctly. We can also use this to see if the clusters are being dominated by the wrong genre.
    for genre in genre_to_cluster_mapping:
        for cluster in genre_to_cluster_mapping[genre]:
            print "genre_dictionary[%s][%s] = %d" %(genre,cluster,genre_to_cluster_mapping[genre][cluster])

    print "finsihed establishing data cluster -> genre mapping"
    #dictionary of dictionaries format: dict[genre][cluster] = count number classified  for this genre as cluster

    #we will use this to establish in which cluster a songs genre are primarally located in.









    clusterDictionary = {}

    import operator
    for genre in genreList:
        print "list for genre" + str(genre_to_cluster_mapping[genre])
        print "cluster picked for " + genre + ": " + max(genre_to_cluster_mapping[genre].iteritems(), key=operator.itemgetter(1))[0]
        clusterDictionary[genre] = max(genre_to_cluster_mapping[genre].iteritems(), key=operator.itemgetter(1))[0]#max(genre_to_cluster_mapping[genre].iteritems(), key=operator.itemgetter(1))[0]

    # lets see how it mapped
    print clusterDictionary




    #make predictions and get the accuracy
    file = open("ourTestDataset.txt", 'r')  # open the testfile
    correct_count = 0.0
    total = 0.0
    for line in file:  # loop over the lines and preform prediciton and see if the prediction is correct.

        if clusterDictionary[line.split(',')[2]] == str(classifier.predict(makevec(line))):
            correct_count += 1.0
        total += 1

    print "accuracy correct/total", float(correct_count) / float(total)


def makevec(line):
    # take in a bag of words representation of lyrics (and expand it to the sparse form for the algorithm
    wordVal = line.split(',')
    wordVal = wordVal[3:]
    weightx = [0] * 5000
    for x in wordVal:
        weightx[int(x.split(':')[0]) - 1] = int(x.split(':')[1].rstrip())
    return weightx


if __name__ == '__main__':
    main()