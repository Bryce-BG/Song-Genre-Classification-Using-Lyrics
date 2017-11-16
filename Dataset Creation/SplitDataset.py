

"""
script to split up our combined dataset into test and train datasets with 90% train, 10% test
Author(s): Bryce Bodley-Gomes
"""



def main():
    train = 90 #percent of the databse to put in train file
    test = 10
    split_ratio = [train,test] #no verification but test + train should = 100


    inFile =  open("ourDataset.txt", "r")
    ourTrainFile = open("ourTrainDataset.txt", "w+") #
    ourTestFile = open("ourTestDataset.txt", "w+")

    num_lines = sum(1 for line in inFile) -18 #get the number of songs so we can split them up by %

    trainCount = num_lines/100*train #the number of lines that equates to whatever percentage we have selected

    inFile.seek(0) #return to start of file
    for line in inFile:
        if trainCount>0: #go until we use up the allocated percentage
            if not line.startswith('%') or not line.startswith('%'):
                trainCount-=1
            ourTrainFile.write(line)
        else: #write out remaining lines to testfile
            ourTestFile.write(line)


    ourTestFile.close()
    ourTrainFile.close()
    inFile.close()










if __name__ == '__main__':
    main()