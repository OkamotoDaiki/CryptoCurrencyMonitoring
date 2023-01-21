# 仮想通貨の価格データを24/7でモニタリングする
 
Historic_Cryptoのモジュールから仮想通貨の価格データを取得し、24時間体制でモニタリングできる。1日毎に更新する。
 
# Features
 
Rasberry Piでも実行可能なので、低電力で実行できる。１日毎の更新時間は00:00。
 
# Requirement
 
* python3 3.8.10
* Historic_Crypto, pandas, schedule, matplotlib, numpy, scipy

# Installation

現在のディレクトリにGraph_btcもしくはGraph_ethを追加して、Usageを実行する。

# Usage
 
run.pyを実行する。ただし、コマンドライン引数で"btc"もしくは"eth"を指定する。ビットコインとイーサリアムのみ対応。
 
```
python3 run.py btc
もしくは、
python3 run.py eth
```
 
# Note
 
scirpt内のCryptoCurrencyLPF, GradientDescent, predictは非公開です。ご自身で作成ください。
 
# Author
 
* Oka.D.
* okamotoschool2018@gmail.com
 
# License
[MIT license](https://en.wikipedia.org/wiki/MIT_License).