# 지난 실습 과제에서 단어장 퀴즈 프로그램을 만들었는데요. 학생들이 문제의 순서가 매번 똑같아서 재미가 없다고 합니다.
#
# 이번에는 random 모듈과 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 내도록 프로그램을 바꿔 보세요.
#
# 같은 단어를 여러번 물어봐도 괜찮고, 프로그램은 사용자가 알파벳 q를 입력할 때까지 계속 실행됩니다.

import random

with open('data/vacabulary.txt', 'r',encoding = "UTF8") as f:

    data = []

    for i in f:
        data.append(i.strip().split(': '))

    voca_len = len(data)

    while True:

        N = random.randint(0, voca_len - 1)

        guess = input(f'{data[N][1]}: ')

        if guess == 'q':
            break

        elif guess == data[N][0]:
            print('맞았습니다.')

        else:
            print(f'틀렸습니다. 정답은 {data[N][0]}입니다.')
