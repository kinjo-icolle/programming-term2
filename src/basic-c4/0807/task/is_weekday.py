from datetime import datetime, timedelta

def process(target_date):
    """
    メインロジックを実行する

    Parameters
    ----------
    target_date : datetime
        処理対象の日付

    Returns
    -------
    list
        表示されるメッセージを要素に含むリスト
    """

    res_list = []   # 結果として返すリスト

    # TODO:書式%wでdatetimeオブジェクトの曜日を取得し、条件分岐してください。
    # TODO:土曜の場合は「(日付) は (曜日) です。平日ではありません。」をres_listに格納し、
    # 更に2日後の日付を取得した上で、「次の平日は(翌月曜日)です」をres_listに格納します。

    # TODO:日曜の場合は「(日付) は (曜日) です。平日ではありません。」をres_listに格納し、
    # 更に1日後の日付を取得した上で、「次の平日は(翌月曜日)です」をres_listに格納します。

    # TODO:その他の場合は「(日付) は (曜日) です。平日です。」をres_listに格納します。

    return res_list

def display(msgs):
    """
    結果を表示する

    Parameters
    ----------
    msgs: list
        表示するメッセージが格納されたリスト

    Returns
    -------
    なし
    """
    print(*msgs, sep="\n")

# メイン処理
if __name__ == '__main__':
    while True:
        try:
            input_date = input('日付を入力してください。')
            target_date = datetime.strptime(input_date, '%Y/%m/%d')

            display(process(target_date))
            break
        except:
            print('入力された日付が不正です。再入力してください。')
