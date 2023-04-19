#!/usr/bin/python3
import tkinter as tk
import tkcalendar as tkc
import datetime

class SavePrintReportApp:
    def __init__(self, master=None):
    #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.today = datetime.date.today()
        self.today_day = self.today.day
        self.today_month = self.today.month
        self.today_year = self.today.year
        # self.mindate =  min date is set as when the first attendance
        self.maxdate = datetime.datetime.now() # max date is today
    #PRE-LOAD-ASSIGNMENT------------------------------------------------------------------------------------------- 
        self.generate_report_app = tk.Tk() if master is None else tk.Toplevel(master)
        self.generate_report_app.configure(background="#0072bc", height=200, width=200)
        self.generate_report_app.geometry("640x600")
        self.generate_report_app.resizable(False, False)
        self.generate_report_app.title("SeekU-Save & Print-Report")
        self.generate_report_app.iconbitmap(".\SeekU\SeekU.ico")
        self.gen_report_frame2 = tk.Frame(self.generate_report_app)
        self.gen_report_frame2.configure(
            background="#0072bc", height=200, width=200)
        self.from_label = tk.Label(self.gen_report_frame2)
        self.from_label.configure(
            background="#0072bc",
            font="{arial} 20 {}",
            foreground="#F7FAE9",
            text='From')
        self.from_label.place(anchor="center", relx=0.20, rely=0.25)

        self.calendar1 = tkc.Calendar(self.gen_report_frame2, selectmode = 'day', maxdate= self.maxdate,
               year = self.today_year, month = self.today_month,
               day = self.today_day, )
        self.calendar1.place(anchor="center", relx=0.25, rely=0.45)

        self.calendar2 = tkc.Calendar(self.gen_report_frame2, selectmode = 'day', maxdate= self.maxdate,
               year = self.today_year, month = self.today_month,
               day = self.today_day)
        self.calendar2.place(anchor="center", relx=0.75, rely=0.45)

        self.to_label = tk.Label(self.gen_report_frame2)
        self.to_label.configure(
            background="#0072bc",
            font="{arial} 20 {}",
            foreground="#F7FAE9",
            justify="left",
            text='To')
        self.to_label.place(anchor="center", relx=0.65, rely=0.25)
        self.save_button = tk.Button(self.gen_report_frame2)
        self.save_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 20 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Save',
            width=10)
        self.save_button.place(
            anchor="center",
            relheight=0.1,
            relwidth=0.3,
            relx=0.30,
            rely=0.9)
        self.save_button.bind("<ButtonPress>", self.save_press, add="")
        self.print_button = tk.Button(self.gen_report_frame2)
        self.print_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 20 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Print',
            width=10)
        self.print_button.place(
            anchor="center",
            relheight=0.1,
            relwidth=0.3,
            relx=0.70,
            rely=0.9)
        self.print_button.bind("<ButtonPress>", self.print_press, add="")
        self.pdf_radiobutton = tk.Radiobutton(self.gen_report_frame2)
        self.file_type_var = tk.StringVar(value='Pdf')
        self.pdf_radiobutton.configure(
            background="#0072bc",
            font="{arial} 24 {}",
            foreground="#F7FAE9",
            text='Pdf',
            selectcolor='black',
            value="Pdf", variable=self.file_type_var)
        self.pdf_radiobutton.place(anchor="center", relx=0.485, rely=0.64, relheight=0.05)
        self.docx_radiobutton = tk.Radiobutton(self.gen_report_frame2)
        self.docx_radiobutton.configure(
            background="#0072bc",
            font="{arial} 24 {}",
            foreground="#F7FAE9",
            selectcolor='black',
            text='Docx', value="Docx", variable=self.file_type_var)
        self.docx_radiobutton.place(anchor="center", relx=0.5, rely=0.72, relheight=0.05)
        self.excel_radiobutton = tk.Radiobutton(self.gen_report_frame2)
        self.excel_radiobutton.configure(
            background="#0072bc",
            font="{arial} 24 {}",
            foreground="#F7FAE9",
            selectcolor='black',
            text='Excel', value="Excel", variable=self.file_type_var)
        self.excel_radiobutton.place(anchor="center", relx=0.505, rely=0.80, relheight=0.05)
        self.gen_report_frame2.place(
            anchor="center",
            relheight=1.0,
            relwidth=1.0,
            relx=0.5,
            rely=0.5)
        self.gen_report_frame = tk.Frame(self.generate_report_app)
        self.gen_report_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.sti_logo = tk.Label(self.gen_report_frame)
        self.img_SeekUsmall = tk.PhotoImage(file=".\SeekU\SeekU small.png")
        self.sti_logo.configure(
            background="#F7FAE9",
            font="TkDefaultFont",
            image=self.img_SeekUsmall)
        self.sti_logo.place(anchor="center", relx=0.30, rely=.5)
        self.app_name_logo = tk.Label(self.gen_report_frame)
        self.img_SeekULogotypemicro = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype micro.png")
        self.app_name_logo.configure(
            background="#F7FAE9",
            foreground="#0072bc",
            image=self.img_SeekULogotypemicro,
            relief="flat",
            text='SEEK')
        self.app_name_logo.place(anchor="center", relx=0.65, rely=0.5)
        self.gen_report_frame.place(
            anchor="center",
            relheight=.2,
            relwidth=1,
            relx=.5,
            rely=0.1)

        # Main widget
        self.mainwindow = self.generate_report_app

    def run(self):
        self.mainwindow.mainloop()

    def save_press (self, event=None):
        pass

    def print_press (self, event=None):
        pass

if __name__ == "__main__":
    app = SavePrintReportApp()
    app.run()
