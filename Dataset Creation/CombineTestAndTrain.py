from collections import defaultdict

def main():

	"""
	this script takes and combines the two mxm datasets test and train (with BOW lyrics for each song) into one complete file
	Author: Bryce Bodley-Gomes
	"""
    file = open("mxm_dataset_test.txt", "r")
    outputfile = open("mxm_dataset_combined.txt", "w+")
    for line in file:
       outputfile.write(line)




    file = open("mxm_dataset_train.txt", "r")
    for line in file:
        if line.startswith("#") or line.startswith("%"):
            pass  # skip comments and instructions (added from test file at top of this file)
        else:
            outputfile.write(line)

    outputfile.close()














if __name__ == '__main__':
    main()

