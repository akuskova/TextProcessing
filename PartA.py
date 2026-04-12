import sys
def main():
    pass

'''
O(n) - linear to the size of the file, since isalnum, isascii, append and lower are constant
'''
def tokenize(textFilePath):
    tokens = []
    newToken = ""
    with open(textFilePath, "r", encoding='utf-8', errors="replace") as file:
        for line in file:
            for char in line:
                if char.isalnum() and char.isascii():
                    newToken += char
                else:
                    if newToken != "":
                        tokens.append(newToken.lower())
                        newToken = ""
            if newToken != "":
                tokens.append(newToken.lower())
                newToken = ""
    return tokens
'''
O(n) - linear to the number of the tokens, since hash operations are constant (on average)
'''
def computeWordFrequencies(listOfTokens):
    tokenMap = {}
    for item in listOfTokens:
        if item not in tokenMap:
            tokenMap[item] = 1
        else:
            tokenMap[item] = tokenMap.get(item) + 1
    return tokenMap

'''
O(nlogn) - since sorted() runs in O(nlogn) and for loop is iterating over dictionary in O(n), O(nlogn) dominates
'''
def print(frequencies):
    frequencies = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))
    for x,y in frequencies.items():
        sys.stdout.write(f"{x} => {y} \n")


if __name__ == "__main__":
    textFilePath = sys.argv[1]
    tokens = tokenize(textFilePath)
    frequencies = computeWordFrequencies(tokens)
    print(frequencies)



