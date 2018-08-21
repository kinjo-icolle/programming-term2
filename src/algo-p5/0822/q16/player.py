# TODO:field_mapモジュールをimportしてください(このクラス内でイベントの名称を取得したいため)


class Player:
    def __init__(self, name):
        """
        コンストラクタ

        Parameters
        ----------
        name : str
            プレイヤーの名前

        Returns
        -------
        自分自身のインスタンス
        """
        self.name = name
        # TODO:プロパティself.cur_pos(プレイヤーの現在位置)に0を代入してください。


    # TODO:game_main.pyの関数定義部のコードを以下に移動してください。但し、下記の手順を踏んでください。
    # TODO:各関数(メソッド)の第1引数にはselfを追加してください。
    # TODO:cur_posのグローバル参照をカットし、残りのcur_posをself.cur_posに変更してください。
    # TODO:同じクラス内の関数(メソッド)を呼び出す際、self.を付けて呼び出してください。
