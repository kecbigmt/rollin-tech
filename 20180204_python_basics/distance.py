#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 平方根の計算に必要なmathモジュールの読み込み（Sec.3）
import math

# 計算したい2点をタプルとして変数に格納（Sec.1 & Sec.5）
point1 = (5, 5)
point2 = (10, 10)

# 関数の宣言（Sec.6）
def dist(point1, point2):
  # 各点のタプルからxy座標をそれぞれ取り出して変数に保存する（Sec.1 & Sec.5）
  x1 = point1[0]
  y1 = point1[1]
  x2 = point2[0]
  y2 = point2[1]

  # 2点間の距離の公式を実装（Sec.2 & Sec.3）
  r = (x1 - x2)**2 + (y1 - y2)**2
  sq = math.sqrt(r)

  # 計算結果を文字列と結合して返り値にする（Sec.4 & Sec.6）
  return "2点の距離: " + str(sq)

# 関数の使用（Sec.6）
d = dist(point1, point2)

# ターミナル（コマンドプロンプト）上に出力
print(d)
