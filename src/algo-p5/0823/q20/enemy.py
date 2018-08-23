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

    # TODO:attackメソッドを定義します。引数はself, playerです。
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
        # TODO:相手に与えるダメージとして、変数damageに、self.min_damageを代入する
        damage = self.min_damage

        # TODO:「(self.name)のこうげき!」を表示
        print(self.name + "のこうげき!")

        # TODO:player.hpからdamageを引いてください。(引いた結果をenemy.hpに再代入してください)
        player.hp -= damage

        if player.hp > 0:
            # TODO: player.hp > 0の場合、「(player.name)は(damage)のダメージを受けた!(player.name)のHPは(enemy.hp)です。」を表示した後、Trueを返す
            print(player.name + "は" + str(damage) + "のダメージを受けた!" + player.name + "のHPは" + str(player.hp) + "です。")
            return True
        else:
            # TODO: 上記以外の場合、「(player.name)は(damage)のダメージを受けた!(enemy.name)のHPは0です。」を表示した後、Falseを返す
            print(player.name + "は" + str(damage) + "のダメージを受けた!" + player.name + "のHPは0です。")
            return False
