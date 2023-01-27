from Historic_Crypto import HistoricalData
import pandas as pd
import schedule
import time
import datetime
import json
import matplotlib.pyplot as plt
from script import PredictData, BuySellPoint, PlottedData
import numpy as np
import subprocess
import sys
import warnings
warnings.simplefilter("ignore")

def get_data(symbol, start_date, end_date, fpath):
    """
    仮想通貨の価格データを取得する
    get cryptocurrency data.

    Attributes:
        symbol: BTC-USD or ETH-USD
        period: period to get data.
        fpath: file path to save data.
    """
    granularity = 86400
    data = HistoricalData(symbol, granularity, start_date, end_date).retrieve_data()
    data.to_csv(fpath)
    return 0


def Simulation_Animation(raw_data, save_fpath, symbol):
    """
    アニメーションの作成
    Generate animation.
    """
    parameter = json.load(open("./parameter.json"))
    length_pred = parameter["length_pred"]
    ylabel_name = symbol + "-USD"

    N = len(raw_data)
    if N >= length_pred:
        """predict data"""
        x = np.linspace(0, len(raw_data)-1, len(raw_data))
        plotted_data = np.array(PlottedData.get_plotted_data(raw_data))
        x_pred, y_pred = PredictData.predict_algorithm(x, plotted_data)
        x_np_pred, y_np_pred = np.array(x_pred), np.array(y_pred)
        buy_points, sell_points = BuySellPoint.get_buy_points(y_pred), BuySellPoint.get_sell_points(y_pred)
        """plot"""
        plt.figure(figsize=(16,9), dpi=120)
        plt.rcParams["font.size"] = 18
        plt.xlabel("day")
        plt.ylabel(ylabel_name)
        plt.plot(x, raw_data, label="data")
        plt.plot(x_pred, y_pred, label="predict")
        plt.vlines(x[-1], min(raw_data), max(raw_data), color="orange", linestyle="dashed", label="now")
        plt.plot(x_np_pred[sell_points], y_np_pred[sell_points], "ro")
        plt.plot(x_np_pred[buy_points], y_np_pred[buy_points], "mo")
        number = str(len(raw_data))
        save_img_fpath = save_fpath + "graph_" + number + "_" + symbol + ".png"
        plt.savefig(save_img_fpath, facecolor="gray")
        plt.legend()
        print("Number: {}".format(number))
        plt.clf()
    else:
        pass
    return save_img_fpath


def job():
    delay = 120
    sleep_time = 24 * 60 * 60 - delay
    extract_row = "high"
    start_date = "2017-01-01-00-00"
    dt_now = datetime.datetime.now()
    end_date = str(dt_now.year) + "-" + str(dt_now.month) + "-" + str(dt_now.day) + "-00-00"
    symbol = sys.argv[1]
    print(symbol)
    if symbol == "btc" or symbol == "BTC":
        """btc"""
        symbol_btc = "BTC-USD"
        fpath_btc = "data/btc_day.csv"
        get_data(symbol_btc, start_date, end_date, fpath_btc)
        save_fpath = "./Graph_btc/"
        df = pd.read_csv(fpath_btc)
        raw_data = df[extract_row].interpolate()
        btc_save_fpath = Simulation_Animation(raw_data, save_fpath, symbol) #BTC
        cmd = ["xli", btc_save_fpath]
        btc_p = subprocess.Popen(cmd)
        """画像ウインドウを閉じる"""
        time.sleep(sleep_time)
        btc_p.terminate()
    elif symbol == "eth" or symbol == "ETH":
        """eth"""
        symbol_eth = "ETH-USD"
        save_fpath = "./Graph_eth/"
        fpath_eth = "data/eth_day.csv"
        get_data(symbol_eth, start_date, end_date, fpath_eth)
        df = pd.read_csv(fpath_eth)
        raw_data = df[extract_row].interpolate()
        eth_save_fpath = Simulation_Animation(raw_data, save_fpath, symbol) #ETH
        cmd = ["xli", eth_save_fpath]
        eth_p = subprocess.Popen(cmd)
        """画像ウインドウを閉じる"""
        time.sleep(sleep_time)
        eth_p.terminate()
    else:
        print("Error: symbol string is wrong.")
        sys.exit()
    return 0


def main():
    job()
    #schedule.every().day.at("00:00").do(job)

    #while True:
    #    schedule.run_pending()
    #    time.sleep(60)
    return 0

if __name__=="__main__":
    main()