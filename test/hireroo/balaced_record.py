# これfreeeのテストで出そうだよ
def solution(time, deposits, withdraws, salaries):
    # TODO: Implement me!
    # 前提
    # 時間 時刻が変動していった時にどのようになるのかを考えて行けば良い
    # 預金 [時刻,収入]
    # 出金 [[時間,出金金額]]
    # 給与 [時刻スタート,時刻終了,収入]

    # 例みたいなの
    # 入力: time = 4, deposits = [[1, 2]], withdraws = [[2, 2]], salaries = [[1, 3, 1]]
    # 出力: [0, 3, 2, 2]
    # ０→０
    # 1→預金されて２,給与で１なので３
    # 2→2出金され、給与で１なので3-2+1=2
    # 3→給与は１〜３までなので、2のまま
    # よって0,3,2,2になる

    # ループ終了は時刻まで
    # ループでやるのはやばい

    # 発想の逆転
    # 毎日の収支を出すだけでいいそこだけ考えろ
    # 全部入れるのではなく、関心を分離せよ
    # 箱を用意
    daly_amount_changes = [0]*time

    # 入金
    # depositsから2つのパラメータを取り出して、時間と金額を取得し、金額だけ、配列にぶち込む
    for t,amount in deposits:
        if 0<= t < time:
            daly_amount_changes[t] += amount

    # 出金
    # depositesと同じでマイナスバージョンにすればいい
    for t,amount in withdraws:
        if 0<= t < time:
            daly_amount_changes[t] -= amount

    # 給与
    # 注意すべきなのは、開始と終了があるからその期間足すということを留意する
    for start, end, amount in salaries:
        for t in range(start,end):
            daly_amount_changes[t] += amount


    # 出力すべきもの
    # 長さTの整数型配列を出力すればいい
    # これを行うために何をすべきか？？
    # 時刻による残高を出力する

    # 資産残高のリスト
    balance_history = [] 
    current_balance = 0

    for amount_change in daly_amount_changes:
        # daly_amount_changesで拾ってきた値を残高にぶち込む
        current_balance +=amount_change
        balance_history.append(current_balance)

    return balance_history
