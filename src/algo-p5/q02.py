# 変数定義部
cur_pos = 0 # 現在の位置

# 関数定義部
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
    # TODO:(2) (1)から移動したコードをこの下に貼り付け、このコメントとインデントを合わせてください。
    # dice_numはcellsに書き換えてください。


# 以下メイン処理
# サイコロで出た目をdice_numに代入
dice_num = 1

# 出たサイコロの目を表示
print(str(dice_num) + "の目が出ました。")

# TODO:(1)下記2行のコードをgo_forward関数の中に移動してください。(このコメントは削除してください)
cur_pos = 0
cur_pos += dice_num

# TODO:(3)go_forward関数を、引数にdice_numを渡して呼び出してください。


# 現在位置を表示
print("現在位置は" + str(cur_pos) + "です。")
