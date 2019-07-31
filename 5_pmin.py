# 프로그램 명: pmin
# 제한시간: 1 초
# 수열이 주어질 때 이 수열에 있는 수 중 최소값의 위치를 모두 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄은 수열의 개수 n 이다.( 1 <= n <= 100 )
# 다음 줄에는 n 개의 수가 주어진다. ( 모든 수는 1000 이하의 음이 아닌 정수) 차례대로 첫번째 , 두번째 , ....
# 출력
# 최소값의 위치를 순서대로 출력한다.
# 입출력 예
# 입력
#
# 4
# 5 2 10 2
#
# 출력
#
# 2 4
# [질/답] [제출 현황] [푼 후(4)]
# [ 채 점 ] [홈으로]  [뒤 로]

input_number = int(input())
list_a_string = input().split()
list_a = [int(a) for a in list_a_string]
# print(list_a)

i = 0
while i < len(list_a):
    if list_a[i] == min(list_a):
        print(i+1, end=' ')
    i += 1
