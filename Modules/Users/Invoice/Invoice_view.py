from tkinter import *
from pathlib import Path
import Modules.Main_process as Main_process

class Invoice_view:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("966x600")
        self.window.title("Invoice")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=600, width=966, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_frame_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Invoice"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon.png", "Frame")))
        self.background_img = PhotoImage(file=self.relative_to_assets("background_invoices.png", "Frame"))
        self.canvas.create_image(483.0, 300.0, image=self.background_img)

        self.entry_total = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_total.place(x=427.48, y=464.49, width=244.75, height=28.68)


        self.button_img_back = PhotoImage(file=self.relative_to_assets("button_back.png", "Frame"))
        self.button_back = Button(image=self.button_img_back, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: Main_process.Main_process.back_button(self), relief="flat")
        self.button_back.place(x=671.0, y=527.0, width=110.0, height=47.0)



    def relative_to_assets(self, path: str, assets_type: str = "Frame") -> Path:
        if assets_type == "Frame":
            return self.assets_frame_path / Path(path)


if __name__ == "__main__":
    app = Invoice_view()
    app.window.mainloop()