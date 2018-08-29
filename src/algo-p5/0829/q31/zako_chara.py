# 別ファイルのクラスを継承する際、importが必要です。
from enemy import Enemy

# TODO:Enemyクラスを継承し、ZakoCharaクラスを作成します。
class ZakoChara(Enemy):
    # TODO:コンストラクタ(__init__())のみを、Enemyクラスのものをそのままコピーして貼り付けてください。attack()メソッドは不要です。
    def __init__(self, name):
        """
        コンストラクタ

        Parameters
        ----------
        name : str
            敵の名前

        Returns
        -------
        自分自身のインスタンス
        """
