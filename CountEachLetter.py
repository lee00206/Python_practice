def main():
    filename = input("파일명을 입력하세요: ").strip()

    infile = open(filename, "r")    

    counts = 26* [0]
    for line in infile:
        countLetters(line.lower(), counts)

    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + ": " + str(counts[i]) + "번 나타납니다.")

    #print(counts)
    infile.close()

def countLetters(line, counts):
    #print( "line = ", line, "_________")
    
    for ch in line:
        if ch.isalpha():
            #print(" ch = " , ch, "ord = ", ord(ch), " index = ", ord(ch) - ord('a'))            
            counts[ord(ch) - ord('a')] += 1

main()


