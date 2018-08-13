import field_map

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
    # 現在位置をグローバル参照する
    global cur_pos

    # 引数のマス目だけ進む
    cur_pos += cells

    # 現在位置を表示
    print("現在位置は" + str(cur_pos) + "です。")

    # 止まったマス目のイベントを取得する
    event_nm = field_map.get_event(cur_pos)

    # TODO:event_nmによって下記の通り条件分岐する
    # TODO:event_nmが"GoMoreForward"の場合、以下に定義したgo_more_forward()を呼び出す。引数は2

    # TODO:event_nmが"GoBack"の場合、以下に定義したgo_back()を呼び出す。引数は3

    # TODO:event_nmが"GoBackToStart"の場合、以下に定義したgo_back_to_start()を呼び出す。引数はなし


def go_more_forward(cells):
    """
    出た目の分さらに前に進む

    Parameters
    ----------
    cells : int
        進むマス目の数

    Returns
    -------
    なし
    """
    # TODO:「イベント発生！(cells)マスさらに進みます。」を表示してください。


    # TODO:go_forwardに引数cellsを渡して呼び出す


def go_back(cells):
    """
    出た目の分後ろに戻る

    Parameters
    ----------
    cells : int
        戻るマス目の数

    Returns
    -------
    なし
    """
    # TODO:「イベント発生！(cells)マス後ろに戻ります。」を表示してください。


    # TODO:go_forwardに引数(cells * -1)を渡して呼び出す


def go_back_to_start():
    """
    出た目の分後ろに戻る

    Parameters
    ----------
    なし

    Returns
    -------
    なし
    """
    # TODO:cur_posをグローバル参照してください。


    # TODO:「イベント発生！振り出しに戻ってしまいます！」を表示してください。


    # TODO:go_forwardに引数(cur_pos * -1)を渡して呼び出す


# 以下メイン処理
if __name__ == '__main__':
    # 開始メッセージを表示
    print("すごろくゲーム、Start!!")

    # ゴールに到達するまでサイコロを投げて進む行為を繰り返す
    while cur_pos < field_map.goal_pos:
        # サイコロを振る
        dice_num = field_map.shake_dice()

        # 出た目の分だけ進む
        go_forward(dice_num)

    # ゴール到達のメッセージを表示
    print("ゴールしました。おめでとうございます!")
