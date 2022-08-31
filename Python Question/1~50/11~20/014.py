# 서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.

import datetime

KST = datetime.datetime.now()

print('%d-%02d-%02d' %(KST.year, KST.month, KST.day))