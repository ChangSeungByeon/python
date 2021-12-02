# strip 는 문자열의 양 끝에 연속된 화이트 스페이스를 없애준다 -> 공백, 탭, 엔터
# --> 문자열.strip()
#
# split 는 문자열 내 특정 문자로 나누어 list 로 반환한다.
# --> 문자열.split(" 구분자 ") (구분자를 넣지 않으면 화이트 스페이스 기준으로 나눈다.)
#
# with open('파일명 및 위치', 'r') as f:
#     for line in f: # for 문으로 불러준다.
#         stripstring = line.strip()
#         splitstring = line.split()