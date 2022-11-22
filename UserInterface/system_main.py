#!/usr/bin/python3
import tkinter as tk


class FaceRecognitionUI:
    def __init__(self, master=None):
        # build ui
        self.system_app = tk.Tk() if master is None else tk.Toplevel(master)
        self.system_app.configure(
            background="#0072bc",
            height=200,
            relief="flat",
            takefocus=True,
            width=200)
        self.system_app.geometry("1280x720")
        self.system_app.resizable(True, True)
        self.system_app.title("SeekU - Face Recognition Attendance System")
        frame1 = tk.Frame(self.system_app)
        frame1.configure(background="#0072bc", height=200, width=200)
        self.system_name = tk.Label(frame1)
        self.system_name.configure(
            background="#0072bc",
            font="{Arial Black} 40 {}",
            foreground="#fff200",
            justify="center",
            takefocus=False,
            text='SEEK U')
        self.system_name.grid(column=1, padx=25, pady=35, row=0, sticky="nw")
        self.year_section = tk.Label(frame1)
        self.year_section.configure(
            background="#0072bc",
            cursor="arrow",
            font="{arial black} 14 {}",
            foreground="#ffffff",
            justify="center",
            takefocus=False,
            text='BSCS - 4A S.Y. 2022-2023')
        self.year_section.grid(column=1, row=0,sticky="w")
        self.client_name = tk.Label(frame1)
        self.client_name.configure(
            background="#fff200",
            font="{Arial Black} 25 {}",
            foreground="#0072bc",
            height=2,
            justify="center",
            text='Detecting...',
            width=20)
        self.client_name.grid(column=0, columnspan=2, ipadx=30, padx=5, row=1)
        self.attendance_date = tk.Label(frame1)
        self.attendance_date.configure(
            background="#fff200",
            font="{Arial Black} 13 {}",
            foreground="#0072bc",
            height=2,
            justify="center",
            relief="flat",
            text='Attendance:',
            width=35)
        self.attendance_date.grid(
            column=0,
            columnspan=2,
            ipadx=20,
            ipady=10,
            padx=5,
            row=2)
        self.next_student = tk.Button(frame1)
        self.next_student.configure(
            background="#fff200",
            font="{Arial Black} 14 {}",
            foreground="#0072bc",
            justify="left",
            takefocus=False,
            text='Next',
            width=20)
        self.next_student.grid(
            column=0,
            columnspan=2,
            ipady=1,
            padx=90,
            pady=20,
            row=4,
            sticky="w")
        self.next_student.bind("<ButtonPress>", self.next_button, add="+")
        self.sti_logo = tk.Label(frame1)
        self.img_STICollegeBalagtasLogos = tk.PhotoImage(
            file="SeekU/STI College Balagtas Logo-s.png")
        self.sti_logo.configure(
            background="#0072bc",
            image=self.img_STICollegeBalagtasLogos,
            text='label3')
        self.sti_logo.grid(
            column=0,
            padx=20,
            pady=20,
            row=0,
            rowspan=2,
            sticky="nw")
        self.reset = tk.Button(frame1)
        self.reset.configure(
            background="#fff200",
            font="{Arial Black} 14 {}",
            foreground="#0072bc",
            justify="left",
            text='Reset',
            width=10)
        self.reset.grid(
            column=0,
            columnspan=2,
            padx=90,
            pady=20,
            row=4,
            sticky="e")
        self.reset.bind("<ButtonPress>", self.reset_button, add="+")
        frame1.pack(expand="true", fill="both", side="left")
        frame1.grid_anchor("center")
        frame1.rowconfigure(0, weight=1)
        frame1.rowconfigure("all", weight=1)
        frame1.columnconfigure(0, weight=1)
        frame1.columnconfigure("all", weight=1)
        frame5 = tk.Frame(self.system_app)
        frame5.configure(background="#0072bc", height=400, width=400)
        self.add_user = tk.Button(frame5)
        self.add_user.configure(
            background="#fff200",
            font="{Arial Black} 14 {}",
            foreground="#0072bc",
            justify="left",
            text='Add',
            width=20)
        self.add_user.grid(column=0, padx=5, pady=60, row=0, sticky="s")
        self.add_user.bind("<ButtonPress>", self.add_client, add="+")
        canvas4 = tk.Canvas(frame5)
        canvas4.configure(
            background="#0072bc",
            borderwidth=0,
            height=500,
            insertborderwidth=0,
            relief="flat",
            width=500)
        canvas4.grid(column=0, padx=5, pady=50, row=0, sticky = "n")
        frame5.pack(expand="true", fill="both", side="right")
        frame5.grid_anchor("center")
        frame5.rowconfigure(0, weight=1)
        frame5.columnconfigure(0, weight=1)

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
