# 당첨 액수는 아래 규칙에 따라 결정됩니다.
#
# 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치 (10억 원)
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만 원)
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치 (100만 원)
# 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치 (5만 원)
# 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치 (5천 원)

from random import randint

# ----------------------------
# generate_numbers
# 이 함수는 파라미터로 정수 n을 받습니다. 무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑고, 그 번호들이 담긴 리스트를 리턴합니다.
# ----------------------------

def generate_numbers(n):
    # 코드를 작성하세요.

    N = n
    result = []

    while N != 0:

        new = randint(1, 45)

        if new in result:
            continue

        result.append(new)
        N -= 1

    return result


# ----------------------------
# draw_winning_numbers
# 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다. 일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다.
# ----------------------------
def draw_winning_numbers():
    # 코드를 작성하세요.

    temp = generate_numbers(7)

    return sorted(temp[:6]) + temp[6:]

# ----------------------------
# count_matching_numbers
# 파라미터로 리스트 list_1과 리스트 list_2를 받고, 두 리스트 사이에 겹치는 번호 개수를 리턴합니다.
# ----------------------------

def count_matching_numbers(list_1, list_2):
    # 코드를 작성하세요.
    result = 0

    for i in list_1:
        if i in list_2:
            result += 1
    return result

# ----------------------------
# check
# 최종 당첨금액 리턴 함수
# ----------------------------


def check(numbers, winning_numbers):
    # 코드를 작성하세요.

    normal = count_matching_numbers(numbers, winning_numbers[:6])
    bonus = count_matching_numbers(numbers, winning_numbers[6:])

    if normal == 5 and bonus == 1:
        return 50000000
    if normal == 5:
        return 1000000
    if normal == 6:
        return 1000000000
    elif normal == 4:
        return 50000
    elif normal == 3:
        return 5000
    else:
        return 0
