from PartA import tokenize 
from PartA import computeWordFrequencies
import sys

def main():
    pass
'''
O(n) - linear to the sizes of the files
'''
def intersection(file1, file2):
    list1, list2 = tokenize(file1), tokenize(file2)
    map1, map2 = computeWordFrequencies(list1), computeWordFrequencies(list2)
    common = map1.keys() & map2.keys()
    print(len(common))

if __name__ == "__main__":
    main()
    file1, file2 = sys.argv[1:3]
    intersection(file1, file2)