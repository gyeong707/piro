###로또###
from random import randint

#무작위로 1과 45사이의 서로 다른 숫자 여섯개를 뽑아 오름차순으로 정렬되어 있는 리스트를 리턴시켜주는 함수
#참가자의 여섯개의 번호를 뽑는데도 쓰이고 보너스를 제외한 당첨번호 여섯개를 뽑는데에도 쓰임.
def generate_numbers():
    count = 0
    numbers = []
    while count < 6:
        num = randint(1, 45)
        if num in numbers:
            continue
        else:
            numbers.append(num)
            count += 1

    numbers.sort()
    print(numbers)
    return numbers


#generate_numbers를 이용해 뽑은 6개의 숫자에 보너스 번호를 포함시킨 리스트를 리턴함.
#일곱개의 번호는 서로 달라야하며, 첫 여섯개만 정렬되어 있으면 됨.
def draw_winning_numbers():
    bonus = randint(1, 45)
    numbers = generate_numbers()
    if bonus not in numbers:
        numbers.append(bonus)
        print(numbers)
        print(type(numbers))
        return numbers
    else:
        return draw_winning_numbers()


#파라미터로 리스트1과 리스트2를 받고, 두 리스트 사이의 겹치는 번호 개수를 리턴해줌.
def count_matching_numbers(users, computers):
    equal = 0
    bonus = 0
    for users_num in users:
        if users_num in computers:
            if users_num == computers[6]:
                bonus += 1
            equal += 1
    print("equal : %d, bonus : %d" % (equal, bonus))
    return equal, bonus

#파라미터로 참가자의 번호 여섯개가 있는 리스트 numbers와 당첨 일반 번호 여섯 개와 보너스 한 개가 있는
#리스트 winning_numbers를 받고, 규칙에 따라 당첨금액을 리턴.
def check(users, computers):
    equal, bonus = count_matching_numbers(users, computers)
    print(equal)
    print(bonus)
    if equal == 6:
        return 1000000000
    elif equal == 5 and bonus == 1:
        return 50000000
    elif equal == 5:
        return 1000000
    elif equal == 4:
        return 50000
    elif equal == 3:
        return 5000
    else:
        return 0

users = generate_numbers()
computers = draw_winning_numbers()
print(type(users))
print(type(computers))
win = check(users, computers)
print("당첨금액 : %d" % win)


