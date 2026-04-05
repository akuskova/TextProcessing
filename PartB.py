from PartA import tokenize 
from PartA import computeWordFrequencies

def main():
    pass

def intersection(file1, file2):
    list1, list2 = tokenize(file1), tokenize(file2)
    map1, map2 = computeWordFrequencies(list1), computeWordFrequencies(list2)
    common = map1.keys() & map2.keys()
    print(len(common))

if __name__ == "__main__":
    main()
