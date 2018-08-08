def print_hand(hand, name='ゲスト'):
    # TODO:変数handsに、'グー','チョキ','パー'を要素に持つリストを代入してください


    # TODO:リストhandsを用いて、選択した手が出力されるように、(◯◯)の部分を書き換えましょう
    print(name + 'は(◯◯)を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
# TODO:「何を出しますか？（0: グー, 1: チョキ, 2: パー）」と出力してください


# TODO:inputを用いて「数字入力してください：」をコンソールに表示後、入力を受け取り、数値に型変換してから変数player_handに代入するよう変更してください
player_hand = int(input('数字で入力してください：'))

if player_name == '':
    # TODO:第1引数を変数player_handに書き換えてください
    print_hand('グー')
else:
    # TODO:第1引数を変数player_handに書き換えてください
    print_hand('グー', player_name)
