# import library
import Analysis_repo
from Analysis_repo import ImportLib as importLibrary

# System variables
importLibrary.customtkinter.set_appearance_mode("System")
importLibrary.customtkinter.set_default_color_theme("green")

class App(importLibrary.customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Pricewatch")
        self.geometry(f"{500}x{300}")
        
        #images
        image_path = importLibrary.os.path.join(importLibrary.os.path.dirname(importLibrary.os.path.realpath(__file__)), "Analysis_repo/test_images")
        self.price_watch_logo = importLibrary.customtkinter.CTkImage(importLibrary.Image.open(importLibrary.os.path.join(image_path, "pricewatch_logo.png")), size=(26, 26))
        self.logo_image = importLibrary.customtkinter.CTkImage(importLibrary.Image.open(importLibrary.os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))

        # APP FUNCTIONS Start -----------------------------------------------------------------------------------------------------------------------------
        
        def change_app_theme_event(self, new_theme: str):
            importLibrary.customtkinter.set_appearance_mode(new_theme)
        
        
        # APP FUNCTIONS End -----------------------------------------------------------------------------------------------------------------------------
        
        # NAVIGATION Start -----------------------------------------------------------------------------------------------------------------------------
        self.navigation_frame = importLibrary.customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)


        self.navigation_frame_label = importLibrary.customtkinter.CTkLabel(self.navigation_frame, text="PriceWatch", image=self.price_watch_logo, compound="left", font=importLibrary.customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        #Navbar items
        self.home_button = importLibrary.customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home", image=self.price_watch_logo, fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w")
        self.home_button.grid(row=1, column=0, sticky="ew")
        
        self.create_button = importLibrary.customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Create Entry", image=self.price_watch_logo, fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w")
        self.create_button.grid(row=2, column=0, sticky="ew")
        
        self.strategy_button = importLibrary.customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Strategy", image=self.price_watch_logo, fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w")
        self.strategy_button.grid(row=3, column=0, sticky="ew")
        
        # System setting
        # self.appearance_mode_optionemenu = importLibrary.customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"], command=self.change_app_theme_event)
        # self.appearance_mode_optionemenu.grid(row=1, column=0, sticky="ew")
           
        # NAVIGATION End -----------------------------------------------------------------------------------------------------------------------------
            
        # TABS SECTION Start -----------------------------------------------------------------------------------------------------------------------------
        # HOME SECTION Start -----------------------------------------------------------------------------------------------------------------------------
        
        self.home_frame = importLibrary.customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        
        # self.textbox = importLibrary.customtkinter.CTkTextbox(self, width=150)
        # self.textbox.grid(row=0, column=1, padx=(10,0), pady=(10,0), sticky="nsew")
        # self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        
        
        
        
            # current prices tab;
        # ENTRY Tab Start -----------------------------------------------------------------------------------------------------------------------------
            # create a new journal entry;
        # STRATEGY Tab Start -----------------------------------------------------------------------------------------------------------------------------
            # create strategy tab;
        
        # TABS SECTION End -----------------------------------------------------------------------------------------------------------------------------
        
        
        # self.sidebar_frame = importLibrary.customtkinter.CTkFrame(self, width=140, corner_radius=0)
        # self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        # self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # self.logo_label = importLibrary.customtkinter.CTkLabel(self.sidebar_frame,  image=self.price_watch_logo,font=importLibrary.customtkinter.CTkFont(size=20, weight="bold"))
        # self.navigation_frame_label = importLibrary.customtkinter.CTkLabel(self.navigation_frame, text="PriceWatch", image=self.price_watch_logo,
        #                                                     compound="left", font=importLibrary.customtkinter.CTkFont(size=15, weight="bold"))
        # self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
if __name__ == "__main__":
    app = App()
    app.mainloop()