from collections import defaultdict

def main():
    """
    make a list of the types of genre we are using and how many times they show
	Author: Bryce Bodley-Gomes
    """
    genredictionary = defaultdict(float)

    file2 = open("msd-topMAGD-genreAssignment.cls", "r")

    for line in file2:
        genredictionary[line.split("	")[1][0:-1]] += 1



    print genredictionary













if __name__ == '__main__':
    main()

