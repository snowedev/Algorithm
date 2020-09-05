# 테트로미노 #B_14500
# 하늘 색: N * (M-3)
# 주황 색: (N-2) * (M-1)
# 회전 혹은 좌우 대칭변환이 가능한 블럭의 모든 경우의 수 19가지
# 블럭이 이동 가능한 반경은 최대 <= N * M
# 따라서 19 * 500 * 500 < 20 * 250000이므로 브루트 포스 가능
# 방법 1은 19가지의 블럭을 코딩하는 것
# 방법 2는 19가지의 블럭을 튜플에 넣어두고 코딩하는 것

blocks = (
    ((0,1), (0,2), (0,3)),
    ((1,0), (2,0), (3,0)),
    ((1,0), (1,1), (1,2)),
    ((0,1), (1,0), (2,0)),
    ((0,1), (0,2), (1,2)),
    ((1,0), (2,0), (2,-1)),
    ((0,1), (0,2), (-1,2)),
    ((1,0), (2,0), (2,1)),
    ((0,1), (0,2), (1,0)),
    ((0,1), (1,1), (2,1)),
    ((0,1), (1,0), (1,1)),
    ((0,1), (-1,1), (-1,2)),
    ((1,0), (1,1), (2,1)),
    ((0,1), (1,1), (1,2)),
    ((1,0), (1,-1), (2,-1)),
    ((0,1), (0,2), (-1,1)),
    ((0,1), (0,2), (1,1)),
    ((1,0), (2,0), (1,1)),
    ((1,0), (2,0), (1,-1)),
)
# 가로 m, 세로 n
n, m = map(int, input().split())
# 입력한 수를 가로에 넣고 그걸 세로로 n 만큼 반복하여 리스트 생성
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0  # 답이 될 값

for i in range(n):
    for j in range(m):
        for block in blocks:
            ok = True
            s = a[i][j]  # 4개의 정사각형으로 이루어진 블럭 중 첫 시작 점

            # 19개의 블럭을 다 계산해 봄
            for dx, dy in block:
                x, y = i+dx, j+dy
                if 0 <= x < n and 0 <= y < m:
                    # 4개로 이루어진 블럭의 나머지 3개까지 합산
                    s += a[x][y]
                else:
                    ok = False
                    break
            # 최댓값을 저장
            if ok and ans < s:
                ans = s

print(ans)
