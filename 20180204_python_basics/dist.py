#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# 関数の定義
def dist(point1, point2):
  # 2点のタプルから座標を分解して変数に代入
  x1 = point1[0]
  y1 = point1[1]
  x2 = point2[0]
  y2 = point2[1]

  # 2点間の距離の公式に基づいて計算
  r = (x1 - x2)**2 + (y1 - y2)**2
  sq = math.sqrt(r)

  # 計算結果を返す
  return sq

# 2点の定義（中身を後から変更する予定はないのでタプルで宣言）
point1 = (5, 5)
point2 = (10, 10)

# 関数の使用（座標はリストの形で渡す）
d = dist(point1, point2)

# 結果をターミナル（コマンドプロンプト）上に出力
print(d)
