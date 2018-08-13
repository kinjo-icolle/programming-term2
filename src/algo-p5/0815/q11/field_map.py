import random

# 変数定義部
goal_pos = 100  # ゴールの位置

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
    # サイコロを振るため、Enterキーを入力待ちにする
    input("サイコロを振ります。Enterキーを押してください。")

    # 1〜6の任意の数字を取得する
    dice_num = random.randint(1, 6)

    # 出た目の数をコンソールに表示する
    print(str(dice_num) + "の目が出ました。")

    # 出た目を返す
    return dice_num

def get_event(target_cell):
    """
    止まったセルのイベントを取得する

    Parameters
    ----------
    target_cell : int
        止まったセル

    Returns
    -------
    str
        イベントの名称
    """
    # TODO:target_cellを10で割って3余ったら"GoMoreForward"を返してください。

    # TODO:上記以外で、target_cellを20で割って17余ったら"GoBack"を返してください。

    # TODO:上記以外でtarget_cellを100で割って49余ったら"GoBackToStart"を返してください。

    # TODO:上記に当てはまらない場合、""を返してください。
    return ""

# 以下メイン処理
if __name__ == '__main__':
    # TODO:get_eventの引数に1を渡して、結果を表示してください。

    # TODO:get_eventの引数に13を渡して、結果を表示してください。

    # TODO:get_eventの引数に37を渡して、結果を表示してください。

    # TODO:get_eventの引数に49を渡して、結果を表示してください。
