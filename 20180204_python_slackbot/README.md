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
