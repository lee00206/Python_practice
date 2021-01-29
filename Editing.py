def main():
    filename = input("파일명을 입력하세요: ").strip()

    infile = open(filename, "r+")
    outfile = open("Morning_replace.txt", "w+")

    word = input("제거할 문자열을 입력하세요: ")

    for line in infile:
        line = line.lower()
        line = line.replace(word, "")
        outfile.write(line)
    
    infile.close()
    outfile.close()

main()

    
