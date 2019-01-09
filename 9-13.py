##단어 퀴즈##
voca = open("vocabulary.txt", "r")

for line in voca:
    data = line.strip().split(":")
    mean = input("%s: " % data[1])
    if mean == data[0]:
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 %s입니다.\n" % data[0])


