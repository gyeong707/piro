from random import randint

voca = open("vocabulary.txt", "r")
dic_voca = {}
for line in voca:
    data = line.strip().split(":")
    dic_voca[str(data[1])] = str(data[0])
print(dic_voca)
#단어장의 모든 자료를 담았다....#

keys = list(dic_voca.keys())
print(keys)

while True:
    random_number = randint(0, len(keys)-1)
    print("난수 : %d" % random_number)
    korean_word = keys[random_number]
    english_word = dic_voca[korean_word]

    sol = input("%s: " % korean_word)
    if sol.strip() == english_word:
        print("맞았습니다!")
    elif sol.strip() == "q":
        print("프로그램을 종료합니다.")
        break
    else:
        print("틀렸습니다. 정답은 %s 입니다." % english_word)