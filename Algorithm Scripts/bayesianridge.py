from sklearn import linear_model
import numpy as np
import warnings
warnings.simplefilter("ignore", DeprecationWarning)




"""
A script that calls the sklearn's implementation of the percepton algorithm on our dataset to train the feature vector wieghts for our dataset.
Then we use these weights to make predictions on our test dataset and output the accuracy of the algorithm on our dataset.
Author(s): Bryce Bodley-Gomes, Theodore Proulx
"""

def main():
    y_list = [] #a list of the genres for each song
    x_list = [] # a list of lists for the feature weights (the word counts for each song in a sparse list format)


    gen_list = ["Pop_Rock", "Jazz", "Latin", "Country", "RnB", "Reggae", "Rap", "Vocal", "International", "New Age", "Electronic", "Blues", "Folk"]

    file = open("ourTrainDataset.txt", 'r')

    count = 0
    for line in file:
        if line.startswith('%') or line.startswith('#'):
            pass
        else:
            count += 1
            if count > 20:
                break
            wordVal = line.split(',')
            y_list.append(float(gen_list.index(wordVal[2])))

            wordVal = wordVal[3:]
            weightx = [0.0]*5000
            for x in wordVal:
                weightx[int(x.split(':')[0])-1] = int(x.split(':')[1].rstrip())
            x_list.append(weightx)
    print "done training"


	#convert lists into numpy arrays
    X = np.array(x_list)
    Y = np.array(y_list)

    print X
    print Y

    classifier = linear_model.BayesianRidge() #create instance of the perceptron
    classifier.fit(X, Y) #run firt function on the dataset

    print "done"
    #make predictions and get the accuracy
    file = open("ourTestDataset.txt", 'r') #open the testfile
    correct_count=0.0
    total =0.0
    for line in file: #loop over the lines and preform prediciton and see if the prediction is correct.
        if gen_list.index(line.split(',')[2]) == round(classifier.predict(makevec(line))):
            correct_count+=1.0
        total+=1


    print "accuracy correct/total", float(correct_count)/float(total)










#(loss = "perceptron",penalty = penalty,alpha = alpha, l1_ratio = 0,fit_intercept = fit_intercept,max_iter = max_iter,tol = tol,shuffle = shuffle,verbose = verbose,random_state = random_state,learning_rate = "constant",eta0 = eta0,power_t = 0.5warm_start = warm_start,class_weight = class_weight,n_jobs = n_jobs,n_iter = n_iter)

def makevec(line):
	#take in a bag of words representation of lyrics (and expand it to the sparse form for the algorithm
    wordVal = line.split(',')
    wordVal = wordVal[3:]
    weightx = [0] * 5000
    for x in wordVal:
        weightx[int(x.split(':')[0]) - 1] = int(x.split(':')[1].rstrip())
    return weightx


if __name__ == '__main__':
    main()
