# N과M 10  B_15664
# 비내림차순
# 하지만 문제는 달라지지 않음
# 방법 1: (6) 문제 풀이 + 중복 제거

# 방법 2 : (9) 참고
import sys
from collections import Counter
n, m = map(int, input().split())
temp = list(map(int, input().split()))

# Counter는 요소의 갯수를 세어줌
# ex) temp = [9, 7, 9, 1]
# 그냥 Counter만 썻을 때에는 [9,7,1]
# Counter(temp).items() = [(9,2), (7,1), (1,1)]
temp = list(Counter(temp).items())
temp.sort()

n = len(temp)
num, cnt = map(list, zip(*temp))
# print(num)  # num = [1,7,9]
# print(cnt)  # cnt = [1,1,2]
a = [0]*m  # 정답을 넣는 배열

# (10) 비내림차순이므로 start 추가
def solution(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    for i in range(start, n):
        if cnt[i] > 0:
            cnt[i] -= 1
            a[index] = num[i]
            solution(index+1, i, n, m)
            cnt[i] += 1


solution(0,0,n,m)

