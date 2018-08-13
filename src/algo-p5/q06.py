# TODO:randomモジュールをimportしてください。


# 変数定義部
goal_pos = 10   # ゴールの位置
cur_pos = 0 # 現在の位置

# 関数定義部
def shake_dice():
    """
    サイコロを振る

    Parameters
    ----------
    なし

    Returns
    -------
    int
        サイコロを振って出た目
    """
    # TODO:input()関数を用いて、「サイコロを振ります。Enterキーを押してください。」のメッセージを表示してください。
    # 入力待ちになり、キーボードから任意の文字が入力可能ですが、特に使う必要がないため、戻り値の代入は不要です。


    # TODO:下記のコードをランダムに1〜6の数字から取得するように変更してください。
    dice_num = 1

    # 出た目の数をコンソールに表示する
    print(str(dice_num) + "の目が出ました。")

    # 出た目を返す
    return dice_num

def go_forward(cells):
    """
    前に進む

    Parameters
    ----------
    cells : int
        進むマス目の数

    Returns
    -------
    なし
    """
    # 現在位置をグローバル参照する
    global cur_pos

    # 引数のマス目だけ進む
    cur_pos += cells

    # 現在位置を表示
    print("現在位置は" + str(cur_pos) + "です。")

# 以下メイン処理
# 開始メッセージを表示
print("すごろくゲーム、Start!!")

# ゴールに到達するまでサイコロを投げて進む行為を繰り返す
while cur_pos < goal_pos:
    # サイコロを振る
    dice_num = shake_dice()

    # 出た目の分だけ進む
    go_forward(dice_num)

# ゴール到達のメッセージを表示
print("ゴールしました。おめでとうございます!")
