#Analyze the text of the book of John from the Bible and display how many times each of these words show up in the text - 'Father', 
#'God', 'Christ', 'Spirit', 'life', 'man' (case sensitive). The text file is available here (note: all punctuation marks, chapter 
#and verse references have been removed to allow to analyze each word

def main():
    infile = open("book-of-John-text.txt", "r")
    words = infile.read()
    #no_special = words.replace("!", "")
    #no_special = no_special.replace(")", "")
    #no_special = no_special.replace('"', "")
    #no_special = no_special.replace(",", "")
    #no_special = no_special.replace(".", "")
    #no_special = no_special.replace("'s", "")
    #no_special = no_special.replace("-", "")
    #no_special = no_special.replace("]", "")
    #no_special = no_special.replace("[", "")
    #no_special = no_special.replace("  ", " ")

    #lower_case = no_special.lower()
    Johnwords = words.split(" ")
    FreqDict = {}

    for word in Johnwords:
        if word in FreqDict:
            FreqDict[word] += 1
        else:
            FreqDict[word] = 1

    #for key in FreqDict:
        #print(key, ":", FreqDict[key])
    print("Father", ":", FreqDict["Father"])
    print("God", ":", FreqDict["God"])
    print("Christ", ":", FreqDict["Christ"])
    print("Spirit", ":", FreqDict["Spirit"])
    print("spirit", ":", FreqDict["spirit"])
    print("life", ":", FreqDict["life"])
    print("man", ":", FreqDict["man"])
    #Close the File
    infile.close()

main()