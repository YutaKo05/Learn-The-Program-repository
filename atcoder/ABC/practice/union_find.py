# 標準入力
N = int(input())
intervals = []
for _ in range(N):
  L,R = map(int,input().split())
  intervals.append([L,R])

# Lの大きさでソートする
intervals.sort()
# 1個だけ入れておく
ans = [intervals[0]]

# 条件式
for i in range(1,N):
  # 現在のl,rを入れる
  current_l, current_r = intervals[i]
  # 現在答えの配列に入っている一番後ろの区間
  last_ans_l, last_ans_r = ans[-1] 
  # 条件
  # 「今の区間の始まり」が「答えの終わり」以下であれば
  if current_l <= last_ans_r:
    ans[-1][1] = max(last_ans_r, current_r)  
  else:
    # 隙間があるから、新しく区間を追加
    ans.append([current_l, current_r])

# 出力
for l, r in ans:
    print(l, r)
  
  
# ロジック
# 合体するかしないかの条件みたいなものとしては
# Rの要素がL以上
# 最大値最小値参照
# 区間計測して中に入るかどうかみたいな？
# 値を取得しながら区間を作っていく？？
# LのリストとRのリストを取得してソートする？

# でも繋がっている繋がっていないはどうする？
# 2次元配列にする？？

# 反省
# 2次元配列を使うことは、わかった。
# ソートする必要もあることはわかった。
# for文と条件式の組み立てが自力じゃできなかった。
# 嫌いな部分（理解があんまりいっていないところ）
# 現在の値と答えの値の比較とそれぞれの値を用意して比較するような処理が苦手



def solution(intervals):

    intervals.sort()
    # 一番初めの値は入れてる 
    ans = [intervals[0]]
    
    for i in range(len(intervals)):
        # 現在の値を取得
        current_start,current_end = intervals[i]
        # 配列に入ってる値を参照
        prev_start,prev_end = ans[-1]

        # 重なりがある場合 区間の始まりが前回の終わり以下である
        if current_start <= prev_end:
            # 答えの配列の一番後ろのendの部分にprev_endかcurrent_endのうちの最大値を入れる
            ans[-1][1] = max(prev_end,current_end)
        else:
            # 区間の重なりがない場合:2次元配列として足す
            ans.append([current_start,current_end])
    return ans 


def solution(nums):
    n = len(nums)
    # 結果を格納するリストを、要素数n、初期値0で作成
    result = [0] * n
    
    for i in range(n):
        # 1. 自分自身をカウント（[nums[i]] という部分配列）
        count = 1
        
        # 2. 左側に向かってチェック
        left = i - 1
        while left >= 0 and nums[left] < nums[i]:
            count += 1
            left -= 1
            
        # 3. 右側に向かってチェック
        right = i + 1
        while right < n and nums[right] < nums[i]:
            count += 1
            right += 1
            
        # 合計値を結果リストに格納
        result[i] = count
        
    return result

# テスト
print(solution([3, 4, 1, 6, 2]))  # 出力: [1, 3, 1, 5, 1]