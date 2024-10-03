# coding:

str = input("Enter Your Message: ")

words = str.split(" ")

coding = input("Enter 1 for Coding or 0 for Decoding: ")

coding = True if (coding=="1") else False

print(coding)

if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "zdf"
            r2 = "fdv"
            strnew = r1 + word[1:] + word[0] + r2
            nwords.append(strnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))


else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            strnew = word[3:-3]
            strnew = strnew[-1] + strnew[:-1]
            nwords.append(strnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

# Project Succesful ;)