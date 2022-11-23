#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image 


class FaceRecognitionUI:
    def __init__(self, master=None):
        # build ui
        self.system_app = tk.Tk() if master is None else tk.Toplevel(master)
        #self.bg_image = ImageTk.PhotoImage(Image.open("SeekU/Background.png"))
        self.system_app.configure(
            background="#0072bc",
            height=200,
            relief="flat",
            takefocus=True,
            width=200)
        self.system_app.geometry("1280x720")
        self.system_app.resizable(True, True)
        self.system_app.title("SeekU - Face Recognition Attendance System")
        frame2 = ttk.Frame(self.system_app)
        frame2.configure(height=200, width=200)
        frame3 = tk.Frame(frame2)
        frame3.configure(background="#0072bc", height=200, width=200)
        self.label1 = tk.Label(frame3)
        self.label1.configure(
            background="#0072bc",
            font="{Arial Black} 40 {}",
            foreground="#fff200",
            justify="center",
            takefocus=False,
            text='SEEK U')
        self.label1.grid(column=1, padx=10, pady=35, row=0, sticky="n")
        self.label2 = tk.Label(frame3)
        self.label2.configure(
            background="#0072bc",
            cursor="arrow",
            font="{arial black} 14 {}",
            foreground="#ffffff",
            justify="center",
            takefocus=False,
            text='BSCS - 4A S.Y. 2022-2023')
        self.label2.grid(column=1, padx=10, row=0)
        self.label3 = tk.Label(frame3)
        self.label3.configure(
            background="#fff200",
            font="{Arial Black} 25 {}",
            foreground="#0072bc",
            height=2,
            justify="center",
            text='Detecting...',
            width=20)
        self.label3.grid(column=0, columnspan=2, ipadx=30, padx=5, row=1)
        self.label4 = tk.Label(frame3)
        self.label4.configure(
            background="#fff200",
            font="{Arial Black} 13 {}",
            foreground="#0072bc",
            height=2,
            justify="center",
            relief="flat",
            text='Attendance:',
            width=35)
        self.label4.grid(
            column=0,
            columnspan=2,
            ipadx=20,
            ipady=10,
            padx=5,
            row=2)
        self.button1 = tk.Button(frame3)
        self.button1.configure(
            background="#fff200",
            font="{Arial Black} 14 {}",
            foreground="#0072bc",
            justify="left",
            takefocus=False,
            text='Next',
            width=20)
        self.button1.grid(
            column=0,
            columnspan=2,
            ipady=1,
            padx=90,
            pady=20,
            row=4,
            sticky="w")
        self.button1.bind("<ButtonPress>", self.next_button, add="+")
        self.label5 = tk.Label(frame3)
        self.img_STICollegeBalagtasLogos = tk.PhotoImage(
            file="SeekU/STI College Balagtas Logo-s.png")
        self.label5.configure(
            background="#0072bc",
            image=self.img_STICollegeBalagtasLogos,
            text='label3')
        self.label5.grid(
            column=0,
            padx=20,
            pady=20,
            row=0,
            rowspan=2,
            sticky="nw")
        self.button2 = tk.Button(frame3)
        self.button2.configure(
            background="#fff200",
            font="{Arial Black} 14 {}",
            foreground="#0072bc",
            justify="left",
            text='Reset',
            width=10)
        self.button2.grid(
            column=0,
            columnspan=2,
            padx=90,
            pady=20,
            row=4,
            sticky="e")
        self.button2.bind("<ButtonPress>", self.next_button, add="+")
        frame3.pack(expand="true", fill="both", side="left")
        frame3.grid_anchor("center")
        frame3.rowconfigure(0, weight=1)
        frame3.rowconfigure("all", weight=1)
        frame3.columnconfigure(0, weight=1)
        frame3.columnconfigure("all", weight=1)
        frame4 = tk.Frame(frame2)
        frame4.configure(background="#0072bc", height=400, width=400)
        self.button3 = tk.Button(frame4)
        self.button3.configure(
            background="#fff200",
            font="{Arial Black} 14 {}",
            foreground="#0072bc",
            justify="left",
            text='Add',
            width=20)
        self.button3.grid(column=0, padx=5, pady=60, row=0, sticky="s")
        self.button3.bind("<ButtonPress>", self.add_client, add="+")
        canvas1 = tk.Canvas(frame4)
        canvas1.configure(
            background="#0072bc",
            borderwidth=0,
            height=500,
            insertborderwidth=0,
            relief="flat",
            width=500)
        canvas1.grid(column=0, padx=5, pady=10, row=0)
        frame4.pack(expand="true", fill="both", side="right")
        frame4.grid_anchor("center")
        frame4.rowconfigure(0, weight=1)
        frame4.columnconfigure(0, weight=1)
        frame2.pack(anchor="center", expand="true", fill="both", side="top")
        #self.bg_label = tk.Label(frame2, image=self.bg_image)
        #self.bg_label.place(x=0,y=0)
        #self.bg_label.lower()
        # Main widget
        self.mainwindow = self.system_app


    #the run of the UI
    def run(self):
        self.mainwindow.mainloop()

    #the Functions of the button
    def next_button(self, event=None):
        pass

    def reset_button(self, event=None):
        pass

    def add_client(self, event=None):
        pass


if __name__ == "__main__":
    app = FaceRecognitionUI()
    app.run()
