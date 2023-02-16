import tkinter as tk


class ClientCameraApp:
    def __init__(self):
        # build ui
        self.camera_app = tk.Toplevel()
        self.camera_app.configure(background="#0072bc", height=200, width=200)
        self.camera_app.geometry("500x600")
        self.camera_app.resizable(False, False)
        self.camera_app.title("SeekU - Camera")
        self.camera_app.iconbitmap(".\SeekU\SeekU.ico")
        self.camera_frame = tk.Frame(self.camera_app)
        self.camera_frame.configure(
            background="#0072bc", height=200, width=200)
        self.ip_cam_entry = tk.Entry(self.camera_frame)
        self.ip_cam_entry.configure(
            background="#F7FAE9",
            font="{arial} 18 {}",
            foreground="#010303",
            show="•")
        self.ip_cam_entry.place(
            anchor="center",
            height=40,
            relx=0.0,
            rely=0.0,
            width=350,
            x=250,
            y=400)
        self.builtin_radiobutton = tk.Radiobutton(self.camera_frame)
        self.builtin_radiobutton.configure(
            background="#0072bc",
            font="{arial} 24 {}",
            foreground="#F7FAE9",
            text='Built in Webcam')
        self.builtin_radiobutton.place(anchor="center", x=210, y=250)
        self.third_party_radiobutton = tk.Radiobutton(self.camera_frame)
        self.third_party_radiobutton.configure(
            background="#0072bc",
            font="{arial} 24 {}",
            foreground="#F7FAE9",
            text='Third Party Webcam')
        self.third_party_radiobutton.place(anchor="center", x=240, y=300)
        self.ip_cam_radiobutton = tk.Radiobutton(self.camera_frame)
        self.ip_cam_radiobutton.configure(
            background="#0072bc",
            font="{arial} 24 {}",
            foreground="#F7FAE9",
            text='IP Camera')
        self.ip_cam_radiobutton.place(anchor="center", x=170, y=350)
        self.ip_cam_radiobutton.bind("<1>", self.callback, add="")
        self.login_button = tk.Button(self.camera_frame)
        self.login_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 20 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text='START',
            width=10)
        self.login_button.place(
            anchor="center",
            height=50,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=200,
            x=250,
            y=550)
        self.login_button.bind("<ButtonPress>", self.login_press, add="")
        self.camera_frame.place(
            anchor="center",
            height=600,
            width=500,
            x=250,
            y=300)
        self.camera_frame2 = tk.Frame(self.camera_app)
        self.camera_frame2.configure(
            background="#F7FAE9", height=200, width=200)
        self.seeku_logo = tk.Label(self.camera_frame2)
        self.img_SeekU2 = tk.PhotoImage(file=".\SeekU\SeekU1.png")
        self.seeku_logo.configure(
            background="#F7FAE9",
            image=self.img_SeekU2)
        self.seeku_logo.place(anchor="center", relx=0.0, rely=0.0, x=150, y=80)
        self.app_name_label = tk.Label(self.camera_frame2)
        self.app_name_label.configure(
            background="#F7FAE9",
            font="{arial black} 40 {}",
            foreground="#0072bc",
            relief="flat",
            text='SEEK')
        self.app_name_label.place(
            anchor="center", relx=0.0, rely=0.0, x=290, y=80)
        self.app_name_label2 = tk.Label(self.camera_frame2)
        self.app_name_label2.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial black} 40 {}",
            foreground="#fff200",
            relief="flat",
            text='U')
        self.app_name_label2.place(
            anchor="center", relx=0.0, rely=0.0, x=395, y=80)
        self.camera_frame2.place(
            anchor="center",
            height=150,
            width=500,
            x=250,
            y=75)

        # Main widget
        self.mainwindow = self.camera_app

    def run(self):
        self.mainwindow.mainloop()

    def callback(self, event=None):
        pass

    def login_press(self, event=None):
        pass


if __name__ == "__main__":
    app = ClientCameraApp()
    app.run()
