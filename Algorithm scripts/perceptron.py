#import sklearn.linear_model.perceptron
from sklearn import linear_model
from collections import defaultdict


import numpy as np
#from sklearn import datasets

def main():
    y_list = []
    x_list = []




    file = open("ourDataset.txt", 'r')
    usecount = 0
    for line in file:
        if line.startswith('%') or line.startswith('#'):
            pass
        else:
            wordVal = line.split(',')
            y_list.append(wordVal[2])

            wordVal = wordVal[3:]
            weightx = [0]*5000
            for x in wordVal:
                weightx[int(x.split(':')[0])-1] = int(x.split(':')[1].rstrip())

            x_list.append(weightx)
            if usecount ==127402:
                print weightx
            if usecount<127403:
                usecount+=1
            else:
                break



    X = np.array(x_list)
    Y = np.array(y_list)

    print "len Y", len(Y)
    print "len X:" , len(X)
    classifier = linear_model.Perceptron()
    classifier.fit(X, Y)


    #predictions
    file = open("test.txt", 'r') #open the testfile
    correct_count=0.0
    total =0.0
    for line in file: #loop over the lines and preform prediciton and see if the prediction is correct.
        if line.split(',')[2] == classifier.predict(makevec(line)):
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