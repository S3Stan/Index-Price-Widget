# import library
import Analysis_repo
from Analysis_repo import ImportLib as importLibrary

# CSSing the widget
importLibrary.customtkinter.set_appearance_mode("system")
importLibrary.customtkinter.set_default_color_theme("dark-blue")
root = importLibrary.customtkinter.CTk()
root.geometry("500x300")
root.title("Pricewatch")


# Navigation frame
root.navigation_frame = importLibrary.customtkinter.CTkFrame(root, corner_radius=0)
root.navigation_frame.grid(row=0, column=0, sticky="nsew")
root.navigation_frame.grid_rowconfigure(4, weight=1)

root.navigation_frame_label = importLibrary.customtkinter.CTkLabel(root.navigation_frame, text="  Image Example", image=root.logo_image,
                                                        compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
root.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

root.home_button = importLibrary.customtkinter.CTkButton(root.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            image=root.home_image, anchor="w", command=root.home_button_event)
root.home_button.grid(row=1, column=0, sticky="ew")

root.frame_2_button = importLibrary.customtkinter.CTkButton(root.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                image=root.chat_image, anchor="w", command=root.frame_2_button_event)
root.frame_2_button.grid(row=2, column=0, sticky="ew")

root.frame_3_button = importLibrary.customtkinter.CTkButton(root.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                image=root.add_user_image, anchor="w", command=root.frame_3_button_event)
root.frame_3_button.grid(row=3, column=0, sticky="ew")

root.appearance_mode_menu = importLibrary.customtkinter.CTkOptionMenu(root.navigation_frame, values=["Light", "Dark", "System"],
                                                        command=root.change_appearance_mode_event)
root.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")



















bucky = "emp"
def get_dxy_price():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data_rgridet = response.json()
        DXY_base = 50.14348112
        EUR_price =  (1/data_rgridet["rates"]["EUR"]); EUR_weight = -0.5760
        JPY_price =  (data_rgridet["rates"]["JPY"]); JPY_weight = 0.1360
        GBP_price =  (1/data_rgridet["rates"]["GBP"]); GBP_weight = -0.1190
        CAD_price =  (data_rgridet["rates"]["CAD"]); CAD_weight = 0.0910
        SEK_price =  (data_rgridet["rates"]["SEK"]); SEK_weight = 0.0420
        CHF_price =  (data_rgridet["rates"]["CHF"]); CHF_weight = 0.0360
        DXY_price = round(DXY_base * (EUR_price ** EUR_weight) * (JPY_price ** JPY_weight) * (GBP_price ** GBP_weight) * (CAD_price ** CAD_weight) * (SEK_price ** SEK_weight) * (CHF_price ** CHF_weight), 3)
        price_label.configure(text=f"DXY: {DXY_price}")
        bucky = DXY_price
    except Exception as error:
        price_label.configure(text="No connection available")
        



    
# frame = importLibrary.customtkinter.CTkFrame(master=root)
# root.grid_columnconfigure(1, weight=1)
# root.grid_columnconfigure((2, 3), weight=0)
# root.grid_rowconfigure((2, 1, 2), weight=1)

# # Main screen contents
# price_label = importLibrary.customtkinter.CTkLabel(master=frame, text="")
# price_label.grid(pady=5)

# refreshButton = importLibrary.customtkinter.CTkButton(master=frame, text="Refresh", command=get_dxy_price)
# refreshButton.grid()

# get_dxy_price() # get price

# # Tabs section

# root.tabview = importLibrary.customtkinter.CTkTabview(root, width=400)
# root.tabview.grid(row=0, column=3, padx=(10, 0), pady=(20, 0), sticky="nsew")
# root.tabview.add("Home")
# root.tabview.add("New")
# root.tabview.add("Previous")
# root.tabview.add("Performance")
# root.tabview.tab("Home").grid_columnconfigure(0, weight=1) 
# root.tabview.tab("New").grid_columnconfigure(0, weight=1) 
# root.tabview.tab("Previous").grid_columnconfigure(0, weight=1) 
# root.tabview.tab("Performance").grid_columnconfigure(0, weight=1) 



# # Tab 1 -  Quick notes
# # Notes_tab = importLibrary.ttk.Frame(notebook)
# # notebook.add(Notes_tab, text="Quick note")



# # Tab 2 - Journal entry files
# # Tab 3 - Previous entries
# # Tab 4 - Performance



# # nt_label = importLibrary.tk.Label(Notes_tab, text="Note content here..")
# # nt_label.rgrid()

# # # Performance
# # Performance_tab = importLibrary.ttk.Frame(notebook)



# # 

 

root.mainloop()


