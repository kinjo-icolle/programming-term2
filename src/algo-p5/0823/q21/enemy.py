# TODO:randomモジュールをimportしてください。


class Enemy:
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
        self.hp = 10
        self.min_damage = 2
        self.max_damage = 4
        self.freq = 30

    def attack(self, player):
        """
        敵を攻撃する

        Parameters
        ----------
        player : Player
            プレイヤーのオブジェクト

        Returns
        -------
        bool
            True:プレイヤーがまだ生きている、False:プレイヤーが死んでしまった
        """
        # TODO:相手に与えるダメージをself.min_damageからself.max_damageの範囲でランダムに選ぶように修正してください。
        # NOTE:random.randintは第1引数に最小値、第2引数に最大値を取ります。


        is_critical = False # 「つうこんのいちげき」かどうか。初期値はFalse(「つうこんのいちげき」でない)
        # TODO:1からself.freqの範囲から、数字をランダムに取得し、変数rand_numに代入してください。

        # TODO:rand_numをself.freqで割った余りが0の場合、is_criticalをTrueに更新してください。


        # 敵のターンのメッセージ表示
        print(self.name + "のこうげき!")

        # TODO:is_criticalがTrueの場合、「つうこんのいちげき!!」を表示した後、damageを2倍にしてください。


        # プレイヤーにダメージを与える
        player.hp -= damage

        if player.hp > 0:
            print(player.name + "は" + str(damage) + "のダメージを受けた!" + player.name + "のHPは" + str(player.hp) + "です。")
            return True
        else:
            print(player.name + "は" + str(damage) + "のダメージを受けた!" + player.name + "のHPは0です。")
            return False
