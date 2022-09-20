def main ():
    infile = open("sometext.txt","r")
    count = wordCount(infile)
    printAnswer(count)

def wordCount(infile):

    count = {}
    reader = infile.readlines()

    for line in reader:
        
        words = line.split()

        for word in words:
            word = word.replace("."," ")
            if word[-1] == ",":
                word = word.replace(","," ")
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
                    
            if word in count:
                count[word] += 1
            else:
                 count[word] = 1

    return count

def printAnswer(count):
    
    print("Word | Frequency")
    for key in count:
        print(key, "--", count[key])

main ()



