from collections import defaultdict
"""
a script to indicate the  fact that we lose (unrofrunitly) about half the dataset as there are not matching ID's in both datasets
Author: Bryce Bodley-Gomes
"""
def main():
    ids = defaultdict(float)
    mxmid = defaultdict(float)

    file = open("mxm_dataset_test.txt", "r")
    for line in file:
        if line.startswith("#"):
            pass #skip comments
        else:
            vec = line.split(',')
            ids[vec[0]] +=1
            mxmid[vec[1]] +=1 #only intrested in the trackid and mxmtrack id (first 2 elements)


    vectorarray2 = []
    x = 0
    file = open("mxm_dataset_train.txt", "r")
    for line in file:
        if line.startswith("#"):
            pass  # skip comments
        else:
            vec = line.split(',')
            ids[vec[0]] += 1
            mxmid[vec[1]] += 1  # only intrested in the trackid and mxmtrack id (first 2 elements)

    print len(mxmid)

    print 'found the key match', 'TRQPCZG128F9316746' in ids

    file2 = open("msd-topMAGD-genreAssignment.cls", "r")
    # for line in file:
    countMatched =0
    countUnmatched =0
    mat = False
    for key, value  in ids.iteritems():
        mat = False
        for line in file2:
            if line.split('\t')[0] in ids:

                countMatched +=1
                mat = True
                break #exit and go to look for next pair
            else:
                pass
        if not mat:
            countUnmatched+=1



    print "matched", countMatched
    print "unmatched", countUnmatched










if __name__ == '__main__':
    main()

