# :의 왼쪽에는 해달 월의 며칠인지, 그리고 오른쪽에는 그 날의 매출이 적혀 있습니다.
#
# data 폴더의 chicken.txt 파일을 읽어 들이고, strip과 split을 써서 12월 코빠닭의 하루 평균 매출을 출력하세요. 평균을 구하기 위해서는 총 매출을 총 일수로 나누면 됩니다.
#
# 참고로 현재 제공된 파일에는 31일이 있지만, 어떤 달은 31일이 아닐 수도 있습니다. 이 점을 고려해서 확장성 있는 코드를 작성해 주시길 바랍니다.
#
# 출력 결과는 아래와 같습니다.

sell_sum = 0
days = 0

with open('data/chicken.txt','r',encoding='UTF8') as ch:
    for i in ch:
        days += 1
        data = i.split()
        sell_sum += int(data[1])

print(sell_sum/days)