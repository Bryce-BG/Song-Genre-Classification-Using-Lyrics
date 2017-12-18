from sklearn import tree
import numpy as np
import warnings
from sklearn.svm import LinearSVC
from sklearn import linear_model
from sklearn.ensemble import VotingClassifier

warnings.simplefilter("ignore", DeprecationWarning)
"""
A script that calls the sklearn's implementation of the decisiontree algorithm to train on our dataset. 
Then we use these weights to make predictions on our test dataset and output the accuracy of the algorithm on our dataset.
Author(s): Bryce Bodley-Gomes, Theodore Proulx
results: 0.700603495572 accuracy and takes 1-2 hours to run.
"""


def main():
    y_list = []  # a list of the genres for each song
    x_list = []  # a list of lists for the feature weights (the word counts for each song in a sparse list format)
    count = 0
    file = open("ourTrainDataset.txt", 'r')
    for line in file:
        if line.startswith('%') or line.startswith('#'):
            pass
        else:
            # if count >50:
            #     break
            # count+=1
            wordVal = line.split(',')
            y_list.append(wordVal[2])

            wordVal = wordVal[3:]
            weightx = [0] * 5000
            for x in wordVal:
                weightx[int(x.split(':')[0]) - 1] = int(x.split(':')[1].rstrip())
            x_list.append(weightx)

    print "finished reading in training data"

            # convert lists into numpy arrays
    X = np.array(x_list)
    Y = np.array(y_list)

    clf1Decision = tree.DecisionTreeClassifier()  # create instance of the perceptron
    clf2LinearSVC = LinearSVC()  # create instance of the perceptron
    clf3SGD = linear_model.SGDClassifier()  # create instance of the classifier
    clf4Perceptron = linear_model.Perceptron()  # create instance of the perceptron
    clf4Perceptron.n_iter = 11  # number ot times to itterate



    eclf = VotingClassifier(estimators=[('dt',clf1Decision),  ('svc', clf2LinearSVC), ('sgd',clf3SGD),('per',clf4Perceptron)], voting='hard')
    "finished training on the data"

    clf4Perceptron.fit(X, Y)  # run firt function on the dataset
    clf3SGD.fit(X, Y)  # Stochastic Gradient Descent
    clf2LinearSVC.fit(X, Y)  # support vector classifier
    clf1Decision.fit(X, Y)  # decision tree
    eclf.fit(X,Y) #not sure what this is fitting

    # make predictions and get the accuracy
    file = open("ourTestDataset.txt", 'r')  # open the testfile
    correct_count = 0.0
    total = 0.0
    for line in file:  # loop over the lines and preform prediciton and see if the prediction is correct.
        if line.split(',')[2] == eclf.predict(makevec(line)):
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