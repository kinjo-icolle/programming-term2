#!/usr/bin/env python3

import cgi
import cgitb
import os.path
import html

# ブラウザでのデバッグを有効にする
cgitb.enable()

# 全体の設定
FILE_LOG = "test-record.txt"

# HTMLを画面に出力する
def print_html(body, total, avg):
    # ヘッダを出力
    print("Content-Type: text/html; charset=utf-8")
    print("")
    # HTMLを出力
    print("""
<html>
<head>
<meta charset="utf-8">
<title>成績一覧</title>
</head>
<body>
<h1>成績一覧</h1>
<div><form>
名前: <input type="text" name="name" size="8">
点数: <input type="text" name="score" size="8">
<input type="submit" value="追加">
<input type="hidden" name="mode" value="write">
</form></div><hr>
<p>合計点：{0}</p>
<p>平均点：{1}</p>
<table>
<tr>
  <th>名前</th><th>点数</th><th>差</th>
</tr>
{2}
</table>
</body></html>
    """.format(total, avg, body))

# 画面に成績一覧を表示する
def mode_read(form):
    # 成績一覧を元に取得した辞書
    results = {}
    # 合計点
    total = 0

    # テキストから成績一覧を読み取る
    if os.path.exists(FILE_LOG):
        with open(FILE_LOG, "r", encoding='utf-8') as f:
            for line in f:
                separated = line.split(",")
                results[separated[0]] = int(separated[1])
                total += int(separated[1])

    # 平均点を求める
    if len(results) > 0:
        avg = round(total / len(results), 1)
    else:
        avg = 0

    # 結果を一覧表示する
    content = ""
    for name, v in sorted(results.items()):
        # 平均点との差を求める
        diff_v = v - avg
        # HTMLの形式で書き出す
        content += "<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>".format(name, v, diff_v)

    print_html(content, total, avg)

# 任意のURLにジャンプする
def jump(url):
    # ヘッダを出力
    print("Status: 301 Moved Permanently")
    print("Location: " + url)
    print("")
    # HTMLを出力(ヘッダがうまく動かなかった時の対策)
    print('<html><head>')
    print('<meta http-equiv="refresh" content="0;'+url+'">')
    print('</head><body>')
    print('<a href="'+url+'">jump</a></body></html>')

# 成績データの書き込み
def mode_write(form):
    # パラメータを取得
    name = form.getvalue("name", "no name")
    score = form.getvalue("score", "")
    # ファイルに保存 --- (*6a)
    with open(FILE_LOG, "a+", encoding='utf-8') as f:
        f.write("{0},{1}\n".format(name,score))
    # 書き込み後にリダイレクトする
    jump('task20180823.py')

# メイン処理
def main():
    # フォームの値を取得
    form = cgi.FieldStorage()
    # modeパラメータを取得
    mode = form.getvalue("mode", "read")
    # modeの値によって処理を変更
    if mode == "read": mode_read(form)
    elif mode == "write": mode_write(form)
    else: mode_read(form)

if __name__ == "__main__":
    main()
