from sklearn.neural_network import MLPClassifier
import numpy as np
import warnings
warnings.simplefilter("ignore", DeprecationWarning)

def main():
    y_list = [] #a list of the genres for each song
    x_list = [] # a list of lists for the feature weights (the word counts for each song in a sparse list format)




    file = open("ourTrainDataset.txt", 'r')

    count = 0
    for line in file:
        if line.startswith('%') or line.startswith('#'):
            pass
        else:
            count += 1
            if count > 1000:
                break
            wordVal = line.split(',')
            y_list.append(wordVal[2])

            wordVal = wordVal[3:]
            weightx = [0]*5000
            for x in wordVal:
                weightx[int(x.split(':')[0])-1] = int(x.split(':')[1].rstrip())
            x_list.append(weightx)
    print "done reading"


	#convert lists into numpy arrays
    X = np.array(x_list)
    Y = np.array(y_list)


    classifier = MLPClassifier() #create instance of the perceptron
    classifier.fit(X, Y) #run firt function on the dataset

    print "done training"
    #make predictions and get the accuracy
    file = open("ourTestDataset.txt", 'r') #open the testfile
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