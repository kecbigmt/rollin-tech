#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 平方根を計算するためのパッケージを読み込む
import math

# 関数の定義
def dist(point1, point2):
  # 2点のリストから座標を分解して変数に代入
  x1 = point1[0]
  y1 = point1[1]
  x2 = point2[0]
  y2 = point2[1]

  # 2点間の距離の公式に基づいて計算
  r = (x1 - x2)**2 + (y1 - y2)**2
  sq = math.sqrt(r)

  # 計算結果を返す
  return sq

# 関数の使用（座標はリストの形で渡す）
d = dist([1, 1], [10, 10])

# 結果をターミナル（コマンドプロンプト）上に出力
print(d)
