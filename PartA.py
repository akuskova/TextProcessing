import sys
def main():
    pass

def tokenize(textFilePath): # returns a list of tokens
    tokens = []
    newToken = ""
    with open(textFilePath, 'r') as file:
        for line in file:
            line = line.casefold()
            for char in line:
                if char.isalnum():
                    newToken += char
                else:
                    if newToken != "":
                        tokens.append(newToken)
                        newToken = ""

    if newToken != "":
        tokens.append(newToken)

    return tokens

def computeWordFrequencies(listOfTokens): # returns a hash map of frequencies
    tokenMap = {}
    for item in listOfTokens:
        if item not in tokenMap:
            tokenMap[item] = 1
        else:
            tokenMap[item] = tokenMap.get(item) + 1
    return tokenMap


def print(frequencies): # prints frequencies
    for x,y in frequencies.items():
        sys.stdout.write(f"{x} => {y} \n")


if __name__ == "__main__":
    main()



