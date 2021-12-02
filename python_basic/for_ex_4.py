# '피타고라스 정리'라고 들어 보셨나요? 직각삼각형에서, 빗변의 제곱이 두 직각변의 제곱의 합과 같다는 정리입니다.
#
# 거기서 나온 '피타고라스 삼조'라는 개념이 있는데요. 피타고라스 삼조란, 피타고라스 정리(a^2 + b^2 = c^2a  를 만족하는 세 자연수 쌍 (a, b, c)입니다.
#
# a<b<c라고 가정할 때, a+b+c=400을 만족하는 피타고라스 삼조는 단 하나인데요. 이 경우, a * b * c는 얼마인가요?

result = False

a = 0
b = 0
c = 0

for i in range(1, 400):
    for j in range(1, 400):

        if i > j:
            continue

        k = 400 - i - j

        if k <= 0:
            break

        if i ** 2 + j ** 2 == k ** 2:
            result = True
            a = i
            b = j
            c = k

    if result:
        break
print(a * b * c)