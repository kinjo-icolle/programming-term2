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
    # TODO:(2) (1)から移動したコードをそのまま貼り付けてください。


    # TODO:(3)dice_numを返してください


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
    # TODO:(1)下記2行のコードをshake_dice関数内に移動してください。移動したらこのコメントは行ごと削除してください。
    dice_num = 1
    print(str(dice_num) + "の目が出ました。")

    # TODO:(4)shake_dice()関数を呼び出した戻り値を、変数dice_numに代入してください。


    # 出た目の分だけ進む
    go_forward(dice_num)

# ゴール到達のメッセージを表示
print("ゴールしました。おめでとうございます!")
