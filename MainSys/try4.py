#!/usr/bin/python3
import tkinter as tk


class CreateUserApp:
    def __init__(self, master=None):
        # build ui
        self.register_user_app = tk.Toplevel(master, container="false")
        self.register_user_app.configure(
            background="#F7FAE9", height=200, width=200)
        self.register_user_app.geometry("600x700")
        self.register_user_app.resizable(False, False)
        self.register_user_frame2 = tk.Frame(self.register_user_app)
        self.register_user_frame2.configure(
            background="#F7FAE9", height=200, width=200)
        self.register_user_button = tk.Button(self.register_user_frame2)
        self.register_user_button.configure(
            background="#0072bc",
            font="{arial black} 20 {}",
            foreground="#F7FAE9",
            text='Register')
        self.register_user_button.place(
            anchor="center",
            relheight=0.08,
            relwidth=0.27,
            relx=.5,
            rely=0.94)
        self.register_user_button.bind(
            "<ButtonPress>", self.take_picture, add="")
        self.register_user_label = tk.Label(self.register_user_frame2)
        self.register_user_label.configure(
            background="#F7FAE9",
            font="{arial} 24 {bold}",
            text='Register User')
        self.register_user_label.place(
            anchor="center", relx=0.5, rely=0.05, x=0, y=0)
        self.username_label = tk.Label(self.register_user_frame2)
        self.username_label.configure(
            background="#F7FAE9",
            font="{arial} 16 {bold}",
            text='Username')
        self.username_label.place(
            anchor="center", relx=0.385, rely=0.14, x=0, y=0)
        self.username_entry = tk.Entry(self.register_user_frame2)
        self.username_entry.configure(font="{arial} 14 {}")
        self.username_entry.place(
            anchor="center",
            relwidth=0.4,
            relx=0.5,
            rely=0.19,
            x=0,
            y=0)
        self.password_label = tk.Label(self.register_user_frame2)
        self.password_label.configure(
            background="#F7FAE9",
            font="{arial} 16 {bold}",
            text='Password')
        self.password_label.place(
            anchor="center", relx=0.385, rely=0.26, x=0, y=0)
        self.password_entry = tk.Entry(self.register_user_frame2)
        self.password_entry.configure(font="{arial} 14 {}")
        self.password_entry.place(
            anchor="center",
            relwidth=0.4,
            relx=0.5,
            rely=0.31,
            x=0,
            y=0)
        self.first_name_label = tk.Label(self.register_user_frame2)
        self.first_name_label.configure(
            background="#F7FAE9",
            font="{arial} 16 {bold}",
            text='First Name')
        self.first_name_label.place(
            anchor="center", relx=0.39, rely=0.39, x=0, y=0)
        self.first_name_entry = tk.Entry(self.register_user_frame2)
        self.first_name_entry.configure(font="{arial} 14 {}")
        self.first_name_entry.place(
            anchor="center",
            relwidth=0.4,
            relx=0.5,
            rely=0.44,
            x=0,
            y=0)
        self.last_name_label = tk.Label(self.register_user_frame2)
        self.last_name_label.configure(
            background="#F7FAE9",
            font="{arial} 16 {bold}",
            text='Last Name')
        self.last_name_label.place(
            anchor="center", relx=0.39, rely=0.52, x=0, y=0)
        self.last_name_entry = tk.Entry(self.register_user_frame2)
        self.last_name_entry.configure(font="{arial} 14 {}")
        self.last_name_entry.place(
            anchor="center",
            relwidth=0.4,
            relx=0.5,
            rely=0.57,
            x=0,
            y=0)
        self.user_role_label = tk.Label(self.register_user_frame2)
        self.user_role_label.configure(
            background="#F7FAE9",
            font="{arial} 16 {bold}",
            text='User Role')
        self.user_role_label.place(
            anchor="center", relx=0.38, rely=0.64, x=0, y=0)
        __values = ['Security Guard', 'HighAdmin', ' LowAdmin']
        self.user_role_optionmenu = tk.OptionMenu(
            self.register_user_frame2, __tkvar, *__values, command=None)
        self.user_role_optionmenu.place(
            anchor="center", relx=.5, rely=0.7, x=0, y=0)
        self.label7 = tk.Label(self.register_user_frame2)
        self.label7.configure(
            background="#F7FAE9",
            font="{arial} 16 {bold}",
            text='User Status')
        self.label7.place(anchor="center", relx=0.395, rely=0.76, x=0, y=0)
        self.active_radiobutton = tk.Radiobutton(self.register_user_frame2)
        self.active_radiobutton.configure(
            background="#F7FAE9",
            font="{arial} 14 {}",
            text='Active')
        self.active_radiobutton.place(
            anchor="center", relx=0.4, rely=0.82, x=0, y=0)
        self.inactive_radiobutton = tk.Radiobutton(self.register_user_frame2)
        self.inactive_radiobutton.configure(
            background="#F7FAE9",
            font="{arial} 14 {}",
            text='Inactive')
        self.inactive_radiobutton.place(
            anchor="center", relx=0.6, rely=0.82, x=0, y=0)
        self.register_user_frame2.place(
            anchor="center",
            relheight=0.82,
            relwidth=1.0,
            relx=0.5,
            rely=0.59)
        self.register_user_frame1 = tk.Frame(self.register_user_app)
        self.register_user_frame1.configure(
            background="#fff000", height=200, width=200)
        self.school_logo_label = tk.Label(self.register_user_frame1)
        self.img_STICollegeBalagtasLogomedium = tk.PhotoImage(
            file="STI College Balagtas Logo medium.png")
        self.school_logo_label.configure(
            background="#fff000",
            image=self.img_STICollegeBalagtasLogomedium,
            text='label1')
        self.school_logo_label.place(anchor="center", relx=.25, rely=0.5)
        self.register_user_frame1.place(
            anchor="center",
            relheight=0.17,
            relwidth=1.0,
            relx=0.5,
            rely=0.09)

        # Main widget
        self.mainwindow = self.register_user_app

    def run(self):
        self.mainwindow.mainloop()

    def take_picture(self, event=None):
        pass


if __name__ == "__main__":
    app = CreateUserApp()
    app.run()

