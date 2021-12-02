# 피보나치 수열(Fibonacci Sequence)라고 들어 보셨나요?
#
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# 1,1,2,3,5,8,13,21,34,55,...
#
# 우선 피보나치 수열의 1번 항과 2번 항은 각각 1입니다. 3번 항부터는 바로 앞 두 항의 합으로 계산됩니다. 예를 들어서 3번 항은 1번 항(1)과 2번 항(1)을 더한 2이며, 4번 항은 2번 항(1)과 3번 항(2)을 더한 3입니다.
#
# 피보나치 수열의 첫 50개 항을 차례대로 출력하는 프로그램을 작성해 보세요.

i_1 = 1
i_2 = 1

n = 0

while n < 50:

    if i_1 <= i_2:
        print(i_1)
        i_1 += i_2

    else:
        print(i_2)
        i_2 += i_1

    n += 1