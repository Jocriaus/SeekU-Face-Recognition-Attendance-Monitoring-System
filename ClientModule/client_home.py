import tkinter as tk
import client_cam as cC

class HomeApp:
    def __init__(self):
        # build ui
        self.home_app = tk.Toplevel()
        self.home_app.configure(background="#0072bc", height=200, width=200)
        self.home_app.geometry("500x500")
        self.home_app.resizable(False, False)
        self.home_app.title("SeekU - Home")
        self.home_app.iconbitmap(".\SeekU\SeekU.ico")
        self.home_app_frame2 = tk.Frame(self.home_app)
        self.home_app_frame2.configure(
            background="#0072bc", height=200, width=200)
        self.attendance_button = tk.Button(self.home_app_frame2)
        self.attendance_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 24 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Attendance',
            width=10)
        self.attendance_button.place(
            anchor="center",
            height=75,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=300,
            x=250,
            y=230)
        self.attendance_button.bind(
            "<ButtonPress>", self.attendance_press, add="")
        self.add_visitor = tk.Button(self.home_app_frame2)
        self.add_visitor.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 24 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Add Visitors',
            width=10)
        self.add_visitor.place(
            anchor="center",
            height=75,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=300,
            x=250,
            y=350)
        self.add_visitor.bind("<ButtonPress>", self.add_visitors_press, add="")
        self.sign_out_button = tk.Button(self.home_app_frame2)
        self.sign_out_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial} 12 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='Sign out',
            width=10)
        self.sign_out_button.place(
            anchor="center",
            height=35,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=100,
            x=75,
            y=465)
        self.sign_out_button.bind("<ButtonPress>", self.signout_press, add="")
        self.home_app_frame2.place(
            anchor="center",
            height=500,
            width=500,
            x=250,
            y=250)

        self.home_app_frame = tk.Frame(self.home_app)
        self.home_app_frame.configure(
            background="#F7FAE9", height=200, width=200)

        self.seeku_logo = tk.Label(self.home_app_frame)
        self.img_SeekU2 = tk.PhotoImage(file=".\SeekU\SeekU1.png")
        self.seeku_logo.configure(
            background="#F7FAE9",
            image=self.img_SeekU2)
        self.seeku_logo.place(anchor="center", x=145, y=80)
        self.app_name_label = tk.Label(self.home_app_frame)
        self.app_name_label.configure(
            background="#F7FAE9",
            font="{arial black} 40 {}",
            foreground="#0072bc",
            relief="flat",
            text='SEEK')
        self.app_name_label.place(
            anchor="center", relx=0.0, rely=0.0, x=280, y=80)
        self.app_name_label2 = tk.Label(self.home_app_frame)
        self.app_name_label2.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial black} 40 {}",
            foreground="#fff200",
            relief="flat",
            text='U')
        self.app_name_label2.place(
            anchor="center", relx=0.0, rely=0.0, x=385, y=80)
        self.home_app_frame.place(
            anchor="center",
            height=150,
            width=500,
            x=250,
            y=75)

        # Main widget
        # self.mainwindow = self.home_app

    # def run(self):
    #     self.mainwindow.mainloop()

    def attendance_press(self, event=None):
        cC.ClientCameraApp()

    def add_visitors_press(self, event=None):
        pass

    def signout_press(self, event=None):
        pass

"""
if __name__ == "__main__":
    app = HomeApp()
    app.run()
"""