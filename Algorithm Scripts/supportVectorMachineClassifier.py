from sklearn.svm import LinearSVC
import numpy as np

import warnings
warnings.simplefilter("ignore", DeprecationWarning)

"""
A script that calls the sklearn's implementation of the Stochastic Gradient Descent algorithm on our dataset to train for our dataset. 
Then we use these weights to make predictions on our test dataset and output the accuracy of the algorithm on our dataset.
Author(s): Bryce Bodley-Gomes, Theodore Proulx
"""


def main():
    y_list = []  # a list of the genres for each song
    x_list = []  # a list of lists for the feature weights (the word counts for each song in a sparse list format)

    file = open("ourTrainDataset.txt", 'r')
    count = 0
    for line in file:
        if line.startswith('%') or line.startswith('#'):
            pass
        else:
            count+=1
            if count>50:
                break
            wordVal = line.split(',')
            y_list.append(wordVal[2])

            wordVal = wordVal[3:]
            weightx = [0] * 5000
            for x in wordVal:
                weightx[int(x.split(':')[0]) - 1] = int(x.split(':')[1].rstrip())
            x_list.append(weightx)

    print "finished reading"

            # convert lists into numpy arrays
    X = np.array(x_list)
    Y = np.array(y_list)

    classifier = LinearSVC()  # create instance of the perceptron

    classifier.fit(X, Y)  # run firt function on the dataset
    print "Finished Training"
    # make predictions and get the accuracy
    file = open("ourTestDataset.txt", 'r')  # open the testfile
    correct_count = 0.0
    total = 0.0
    for line in file:  # loop over the lines and preform prediciton and see if the prediction is correct.
        if line.split(',')[2] == classifier.predict(makevec(line)):
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