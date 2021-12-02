# 화씨
# 온도(°F)를
# 섭씨
# 온도(°C)로
# 바꾸어주는
# 프로그램을
# 만들려고
# 합니다.
#
# 화씨
# 온도
# 리스트: [40, 15, 32, 64, -4, 11]
# 섭씨
# 온도
# 리스트: [4.4, -9.4, 0.0, 17.8, -20.0, -11.7]

# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    # 코드를 입력하세요.

    result = []

    for i in fahrenheit:
        result.append(round((i - 32) * 5 / 9, 1))

    return result


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

temperature_list = fahrenheit_to_celsius(temperature_list)

# 리스트의 값들을 화씨에서 섭씨로 변환하는 코드를 입력하세요.
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력
