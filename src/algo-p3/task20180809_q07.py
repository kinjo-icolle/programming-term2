# TODO:入力した値が正しいかを判定する関数validateを定義してください
# (引数にhandを取り、戻り値に判定結果(正しければTrue,不正ならFalse)を返します。)
def validate(hand):
    # TODO:handが0より小さい、または2より大きい場合Falseを返してください
    # TODO:上記以外の場合、Trueを返してください。
    
def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

# TODO:関数validateの戻り値がTrueの場合のみ、以下のif~else文が実行されるようにしてください

    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
# TODO:関数validateの戻り値がFalseの場合「正しい数値を入力してください」と出力してください
