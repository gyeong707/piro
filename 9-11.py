##단어장 만들기 예제##

voca = open("vocabulary.txt", 'w')

while True:
    name = input("영어 단어를 입력하세요: ")
    if name == "q":
        break
    voca.write(name)
    voca.write(":")
    voca.write(input("한국어 뜻을 입력하세요: "))
    voca.write("\n")

voca.close()