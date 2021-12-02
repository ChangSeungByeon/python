def calculate_change(payment, cost):
    # 코드를 작성하세요.
    money_alone = payment - cost

    money_50 = money_alone // 50000
    money_10 = (money_alone - money_50 * 50000) // 10000
    money_5 = (money_alone - money_50 * 50000 - money_10 * 10000) // 5000
    money_1 = (money_alone - money_50 * 50000 - money_10 * 10000 - money_5 * 5000) // 1000

    print("50000원 지폐: {}장".format(money_50))
    print("10000원 지폐: {}장".format(money_10))
    print("5000원 지폐: {}장".format(money_5))
    print("1000원 지폐: {}장".format(money_1))


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)