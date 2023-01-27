# 仮想通貨の価格データから売買ポイントを予測する
 
Historic_Cryptoのモジュールから仮想通貨の価格データを取得し、売買ポイントを予測する。

![image-min](https://user-images.githubusercontent.com/49944765/215109759-fee2651d-5ff8-49ae-b96a-ade72ba1e83a.gif)

青色のデータがビットコインの生データ(今回は高値)、オレンジ色の線が売買ポイントをプロットするためのグラフ。オレンジ色の縦破線が現在日時である。

そして、赤色の点が売りポイント、紫色の点が買いポイントである。上記のデモは2020年5月3日から2023年1月27日までのデータであるが、今回の場合は現在の日にちよりも超えた時刻に買いポイントがあるので、ビットコインの買い時が近いことを表している。このように、売買ポイントを参考に仮想通貨の売買を行うことがきる。

※仮想通貨の売買は保証できないため、生データ→予測線→売買ポイントの取得→プロット の流れのみを提供する。予測線、売買ポイントを算出するアルゴリズムの作成は各自が行うこと。
 
# Features

また24/7モニタリングすることもできる。Rasberry Piでも実行可能であることを確認しているので、低電力で実行できる。１日毎の更新時間は00:00。
 
# Requirement
 
* python3 3.8.10
* Historic_Crypto, pandas, schedule, matplotlib, numpy, scipy

# Installation

Historic_Cryptoを事前にインストールする。
```
pip install Historic-Crpto
```
また、parameter.jsonを開き"length_pred"の予測する長さを変更する。単位は日。

# Usage
 
run.pyを実行する。ただし、コマンドライン引数で"BTC"もしくは"ETH"を指定する。ビットコインとイーサリアムのみ対応。
 
```
python3 run.py BTC
もしくは、
python3 run.py ETH
```
 
# Note
 
売買ポイントを予測するポイントをプロットするグラフは、PlottedDataのモジュール, 売買ポイントを取得するモジュールはBuySellPoint、予測したグラフを生成するモジュールはPredictDataであるが、これらは非公開。script内に自作すること。
 
# Author
 
* Oka.D.
* okamotoschool2018@gmail.com
 
# License
[MIT license](https://en.wikipedia.org/wiki/MIT_License).