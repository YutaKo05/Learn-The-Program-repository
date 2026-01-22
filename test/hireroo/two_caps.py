import math
# def gcd(x,y):
#     while y != 0:
#         x, y = y, x % y
#     return x

def solution(a, b, c):
    # TODO: Implement me!
    # AとBの容器がある
    # CLちょうどの水を測れるかどうか
    
    # 問題の重要なポイント
    # aとbの量だけ互いに引いたり足したりできる
    # 

    # 最大公約数を求めるらしい
    # 3と５だったら理論上全ていける
    # 互い素なので

    # 4,6とかは、偶数を足したり引いたりしても偶数しか出てこないから奇数は絶対作れない
    # 作れる最小の単位という考え方＝AとBの最大公約数を求めればいいに帰着する
    # ライブラリーが使えないのであれば、ユークリッドをつかってやればいい

    # 出力はTure or Falseで
    if c > max(a,b):
        return False

    # 割り切れるかどうか判断
    return c % math.gcd(a, b) == 0


# 反省
# AとBを考慮すればいいのはわかったが、最大公約数を求めるとは発想できないよ、、、
# これ以外だと幅優先探索をすれば解けるらしい

# BFSver
from collections import deque

def solve_bfs(a, b, c):
    # 状態を保存するキュー (現在のAの水量, 現在のBの水量)
    queue = deque([(0, 0)])
    
    # 一度なった状態を記録するセット（無限ループ防止）
    visited = set()
    visited.add((0, 0))
    
    while queue:
        cur_a, cur_b = queue.popleft()
        
        # ゴール判定：どちらかがcリットルになればOK
        if cur_a == c or cur_b == c:
            return True
        
        # 次に取りうる全ての状態を定義
        next_states = [
            (a, cur_b),      # 1. Aを満タンにする
            (cur_a, b),      # 2. Bを満タンにする
            (0, cur_b),      # 3. Aを空にする
            (cur_a, 0),      # 4. Bを空にする
            # 5. AからBへ移す
            (cur_a - min(cur_a, b - cur_b), cur_b + min(cur_a, b - cur_b)),
            # 6. BからAへ移す
            (cur_a + min(cur_b, a - cur_a), cur_b - min(cur_b, a - cur_a))
        ]
        
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                
    return False

# テスト
print(solve_bfs(3, 5, 4)) # -> True