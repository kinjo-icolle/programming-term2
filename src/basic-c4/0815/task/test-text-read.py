# 成績データを辞書型で定義(空で初期化しておく)
records = {}

# テキストファイルを開く
with open("test-record.txt", encoding="utf-8") as tf:
    for line in tf:
        # 名前と点数を分割する
        l_result = line.split(",")
        name = l_result[0]
        score = int(l_result[1])

        # 名前をキー、点数を値の形式でrecordsに追加する
        records[name] = score

# 合計を求める --- (*1)
sum_v = 0
# for v in records.values():
#     sum_v += v
sum_v = sum(records.values())
# 平均点を計算して結果を表示
ave_v = sum_v / len(records)
print("合計点:", sum_v)
print("平均点:", ave_v)

# 成績データの一覧と平均点との差を表示 --- (*2)
fmt = "| {0:<7} | {1:>4} | {2:>5}"
print("| 名前    | 点数 | 差")
for name, v in sorted(records.items()):
    # 平均点との差を求める
    diff_v = v - ave_v 
    # 小数点以下を丸める --- (*3)
    diff_v = round(diff_v, 1)
    # 書式にそって出力 --- (*4)
    print(fmt.format(name, v, diff_v))

