from tkinter import *
from pathlib import Path


class CartCustomerDetails:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("966x600")
        self.window.title("Cart and Customer Details")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=600, width=966, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Cart_and_Customer"
        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon_cart.png")))

        self.background_img = PhotoImage(file=self.relative_to_assets("background_cart_and_customer.png"))
        self.canvas.create_image(484.0, 300.0, image=self.background_img)


        self.entry_name = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_name.place(x=648.89, y=198.07, width=232.0, height=26.6667)

        self.entry_phone = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_phone.place(x=648.89, y=250.42, width=232.0, height=26.6667)

        self.entry_cccd = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_cccd.place(x=648.89, y=300.1, width=232.0, height=26.6667)

        self.entry_dayin = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_dayin.place(x=224.08, y=392, width=151.39, height=23.33)

        self.entry_dayout = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_dayout.place(x=224.08, y=428.67, width=151.39, height=23.33)

        self.btn_img_booking = PhotoImage(file=self.relative_to_assets("button_booking.png"))
        self.button_booking = Button(image=self.btn_img_booking, borderwidth=0, highlightthickness=0,activebackground="#6C9587", command=lambda: print("Booking button clicked"),relief="flat")
        self.button_booking.place(x=42.9998, y=523.0, width=125.0, height=49.0)

        self.btn_img_cart = PhotoImage(file=self.relative_to_assets("button_cart.png"))
        self.button_cart = Button(image=self.btn_img_cart, borderwidth=0, highlightthickness=0,activebackground="#6C9587", command=lambda: print("Cart button clicked"), relief="flat")
        self.button_cart.place(x=183.0, y=524.0, width=98.0, height=48.0)

        self.btn_img_invoice = PhotoImage(file=self.relative_to_assets("button_invoice.png"))
        self.button_invoice = Button(image=self.btn_img_invoice, borderwidth=0, highlightthickness=0,activebackground="#6C9587", command=lambda: print("Invoice button clicked"),relief="flat")
        self.button_invoice.place(x=791.0, y=524.0, width=124.0, height=48.0)

        self.btn_img_back = PhotoImage(file=self.relative_to_assets("button_back.png"))
        self.button_back = Button(image=self.btn_img_back, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Back button clicked"),relief="flat")
        self.button_back.place(x=668.0, y=523.0, width=110.0, height=49.0)

        self.btn_img_confirm = PhotoImage(file=self.relative_to_assets("button_confirm.png"))
        self.button_confirm = Button(image=self.btn_img_confirm, borderwidth=0, highlightthickness=0,activebackground="#6C9587", command=lambda: print("Confirm button clicked"),relief="flat")
        self.button_confirm.place(x=670.0, y=407.0, width=104.0, height=42.0)

        self.btn_img_add = PhotoImage(file=self.relative_to_assets("button_add.png"))
        self.button_add = Button(image=self.btn_img_add, borderwidth=0, highlightthickness=0,activebackground="#6C9587", command=lambda: print("add button clicked"),relief="flat")
        self.button_add.place(x=234.75, y=470.67, width=52.68, height=23.67)

        self.btn_img_remove = PhotoImage(file=self.relative_to_assets("button_remove.png"))
        self.button_remove = Button(image=self.btn_img_remove, borderwidth=0, highlightthickness=0,activebackground="#6C9587", command=lambda: print("remove button clicked"),relief="flat")
        self.button_remove.place(x=299.44, y=470.67, width=76.03, height=23.33)

        #self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)


if __name__ == "__main__":
    CartCustomerDetails()