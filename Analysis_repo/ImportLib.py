# import 
import tkinter as tk
from tkinter import ttk
import requests
import customtkinter
import os
from PIL import Image


#tab code

    # def get_dxy_price():
    #     try:
    #         response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    #         data_rgridet = response.json()
    #         DXY_base = 50.14348112
    #         EUR_price =  (1/data_rgridet["rates"]["EUR"]); EUR_weight = -0.5760
    #         JPY_price =  (data_rgridet["rates"]["JPY"]); JPY_weight = 0.1360
    #         GBP_price =  (1/data_rgridet["rates"]["GBP"]); GBP_weight = -0.1190
    #         CAD_price =  (data_rgridet["rates"]["CAD"]); CAD_weight = 0.0910
    #         SEK_price =  (data_rgridet["rates"]["SEK"]); SEK_weight = 0.0420
    #         CHF_price =  (data_rgridet["rates"]["CHF"]); CHF_weight = 0.0360
    #         DXY_price = round(DXY_base * (EUR_price ** EUR_weight) * (JPY_price ** JPY_weight) * (GBP_price ** GBP_weight) * (CAD_price ** CAD_weight) * (SEK_price ** SEK_weight) * (CHF_price ** CHF_weight), 3)
    #         price_label.configure(text=f"DXY: {DXY_price}")
    #     except Exception as error:
    #         price_label.configure(text="No connection available")