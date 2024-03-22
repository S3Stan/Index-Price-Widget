import tkinter as tk
import requests


def get_dxy_price():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data_packet = response.json()
        DXY_base = 50.14348112
        EUR_price =  (1/data_packet["rates"]["EUR"]); EUR_weight = -0.5760
        JPY_price =  (data_packet["rates"]["JPY"]); JPY_weight = 0.1360
        GBP_price =  (1/data_packet["rates"]["GBP"]); GBP_weight = -0.1190
        CAD_price =  (data_packet["rates"]["CAD"]); CAD_weight = 0.0910
        SEK_price =  (data_packet["rates"]["SEK"]); SEK_weight = 0.0420
        CHF_price =  (data_packet["rates"]["CHF"]); CHF_weight = 0.0360
        DXY_price = round(DXY_base * (EUR_price ** EUR_weight) * (JPY_price ** JPY_weight) * (GBP_price ** GBP_weight) * (CAD_price ** CAD_weight) * (SEK_price ** SEK_weight) * (CHF_price ** CHF_weight), 3)
        #DXY_divisor = float(50.14348112)/float(current_Euro_price)
        #DXY_price = DXY_divisor / float(current_Euro_price)
        price_label.config(text=f"DXY: {DXY_price}")
    except Exception as error:
        price_label.config(text="Unable to get price")
        
        
Widget = tk.Tk()
Widget.title("EURO Price")

price_label = tk.Label(Widget, text="Loading...")
price_label.pack()

fetch_button = tk.Button(Widget, text="Refresh", command=get_dxy_price)
fetch_button.pack()

get_dxy_price() # get price
Widget.mainloop()
