from random import randint

#--------------------------
# 정답 숫자 3개를 뽑아 주는 generate_numbers 함수
#--------------------------

def generate_numbers():
    numbers = []

    # 코드를 작성하세요.

    while len(numbers) != 3:
        temp = randint(0, 10)

        if not (temp in numbers):
            numbers.append(temp)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers



#--------------------------
# 유저에게 숫자 3개를 입력받는 take_guess 함수
#--------------------------

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    # 코드를 작성하세요.
    while len(new_guess) < 3:
        temp = int(input(f"{len(new_guess) + 1}번째 숫자를 입력하세요: "))

        if temp > 9 or temp < 0:
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요')
            continue
        if temp in new_guess:
            print('중복되는 숫자입니다. 다시 입력하세요.')
            continue

        new_guess.append(temp)

    return new_guess

#--------------------------
# 스트라이크 수와 볼 수를 알려 주는 get_score 함
#--------------------------

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.

    for i in range(len(guesses)):
        if guesses[i] == solution[i]:
            strike_count += 1
            continue
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count


ANSWER = generate_numbers()
# print(ANSWER)
tries = 0

# 코드를 작성하세요.

while True:

    tries += 1

    strike, ball = get_score(take_guess(),ANSWER)

    print(f'{strike}S {ball}B')

    if strike == 3:
        break
    else:
        continue

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))

