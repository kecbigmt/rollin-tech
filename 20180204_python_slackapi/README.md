# PythonでSlack APIをいじってみよう

## APIとは
* なんか入れるとなんかしてくれる便利な箱
* 使い方を知っていれば好きなものを取り出したり好きなことをしてもらえる（ように設計してくれてる）
* プロセス間・端末間のデータのやり取りはたいていAPIを介して行われる（すごく広い概念）
* そのなかでも一般的には「HTTP(HTTPS)プロトコルでインターネットを介して行われる連携の仕組み」を指す

## APIを叩いてみる
* LINE notify
  * Document: https://notify-bot.line.me/doc/ja/
  * HTTPプロトコルとかでデータを送りつけることができる「curl」コマンドを使う
  * Macならデフォで使える。Git for Windows
```
curl -X POST -H 'Authorization: Bearer 8kAN26TnFEWqFIPDufduqHPvoVVHXTpJBkFItmcprpH' -F 'message=foobar' \
https://notify-api.line.me/api/notify
```

## ライブラリを使ってみる

##

#### [辞書型（dict）](https://docs.python.jp/3/tutorial/datastructures.html#dictionaries)
* キー（key）と値（value）のペアの集合
  * `{キー1: 値1, キー2: 値2,...}`という書き方で表現する
  * e.g. `d = {"John": "male", "Olivia":"female"}` →辞書dの作成
* リストから要素を取り出す時は何番目か（index）を指定したが、辞書では自由に設定した値（文字列でも整数でもなんでも）をキーとして、そのキーとペアになっている値を取り出すことができる
  * `辞書[キー]`
  * e.g. `d["John"]` →"male"が出てくる
* キーは一意（ほかに重複するものがない）でなければいけない
* 辞書の値として辞書やリストを渡すこともできる（その場合の辞書は入れ子構造を持つようになる）
* データの保存・管理に最適
##### 例
```
d = {
  "John":{
    "gender": "male",
    "height": 181,
    "age": 24,
    "isAdult": True,
    "state": "California"
  },
  "Olivia":{
    "gender": "female",
    "height": 142,
    "age": 12,
    "isAdult": False,
    "state": "Virginia"
  }
}

print("Johnの年齢は、", d["John"]["age"])
print("Oliviaの年齢は、", d["Olivia"]["age"])
```
