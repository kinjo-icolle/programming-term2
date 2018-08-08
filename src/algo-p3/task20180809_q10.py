def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

# TODO:関数judgeを定義してください
# (引数にplayer(プレイヤーの出した手(0,1,2))とcomputer(コンピュータの出した手)を取り、
#  戻り値として、「勝ち」「負け」「引き分け」の文字列で結果を返します。)
def judge(player, computer):
    # TODO:playerとcomputerが等しければ「引き分け」を返してください

    # TODO:上記に当てはまらず、(playerが0かつcomputerが1)または(playerが1かつcomputerが2)
    # または(playerが2かつcomputerが0)の場合、「勝ち」を返してください
    # ※elifを1回で上記を表現することが難しければ、elifを3回書いても構いません。

    # TODO:上記どちらにも当てはまらない場合は、「負け」を返してください。

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if validate(player_hand):
    computer_hand = 1
   
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
    
    print_hand(computer_hand, 'コンピューター')
    
    # TODO:変数resultに関数judgeの戻り値を代入してください
    

    # TODO:変数resultを、「結果は(result)でした」の形式で出力してください

else:
    print('正しい数値を入力してください')