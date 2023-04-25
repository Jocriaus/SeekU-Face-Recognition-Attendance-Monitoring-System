#!/usr/bin/python3
import tkinter as tk
import tkinter.messagebox as messbx
import query_mod as qry


class CreateUserApp:
    def __init__(self, admin_hom, refresh):

        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.admin_home_window = admin_hom
        self.sql_query = qry.dbQueries()
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # build ui
        self.register_user_app = tk.Toplevel()
        self.register_user_app.configure(background="#F7FAE9", height=200, width=200)
        self.register_user_app.geometry("600x600")
        self.register_user_app.resizable(False, False)
        self.register_user_app.title("SeekU - Register User")
        self.register_user_app.iconbitmap("./SeekU/SeekU.ico")
        self.refresh_func = refresh
        # Contains-the-edit-label-and-entry-widgets---------------------------------------------------------------------------------------------------------
        self.register_user_frame2 = tk.Frame(self.register_user_app)
        self.register_user_frame2.configure(background="#F7FAE9", height=200, width=200)
        self.register_user_button = tk.Button(self.register_user_frame2)
        self.register_user_button.configure(
            background="#0072bc",
            font="{arial black} 20 {}",
            foreground="#F7FAE9",
            text="Register",
        )
        self.register_user_button.place(
            anchor="center", relheight=0.1, relwidth=0.27, relx=0.5, rely=0.9
        )
        self.register_user_button.bind("<ButtonPress>", self.register_user, add="")
        self.register_user_label = tk.Label(self.register_user_frame2)
        self.register_user_label.configure(
            background="#F7FAE9", font="{arial} 24 {bold}", text="Register User"
        )
        self.register_user_label.place(anchor="center", relx=0.5, rely=0.05, x=0, y=0)
        self.username_label = tk.Label(self.register_user_frame2)
        self.username_label.configure(
            background="#F7FAE9", font="{arial} 16 {bold}", text="Username"
        )
        self.username_label.place(anchor="center", relx=0.385, rely=0.15, x=0, y=0)
        self.username_entry = tk.Entry(self.register_user_frame2)
        self.username_entry.configure(font="{arial} 14 {}")
        self.username_entry.place(
            anchor="center", relwidth=0.4, relx=0.5, rely=0.21, x=0, y=0
        )
        self.password_label = tk.Label(self.register_user_frame2)
        self.password_label.configure(
            background="#F7FAE9", font="{arial} 16 {bold}", text="Password"
        )
        self.password_label.place(anchor="center", relx=0.385, rely=0.28, x=0, y=0)
        self.password_entry = tk.Entry(self.register_user_frame2)
        self.password_entry.configure(font="{arial} 14 {}", show="•")
        self.password_entry.place(
            anchor="center", relwidth=0.4, relx=0.5, rely=0.34, x=0, y=0
        )
        self.first_name_label = tk.Label(self.register_user_frame2)
        self.first_name_label.configure(
            background="#F7FAE9", font="{arial} 16 {bold}", text="First Name"
        )
        self.first_name_label.place(anchor="center", relx=0.39, rely=0.41, x=0, y=0)
        self.first_name_entry = tk.Entry(self.register_user_frame2)
        self.first_name_entry.configure(font="{arial} 14 {}")
        self.first_name_entry.place(
            anchor="center", relwidth=0.4, relx=0.5, rely=0.47, x=0, y=0
        )
        self.last_name_label = tk.Label(self.register_user_frame2)
        self.last_name_label.configure(
            background="#F7FAE9", font="{arial} 16 {bold}", text="Last Name"
        )
        self.last_name_label.place(anchor="center", relx=0.39, rely=0.54, x=0, y=0)
        self.last_name_entry = tk.Entry(self.register_user_frame2)
        self.last_name_entry.configure(font="{arial} 14 {}")
        self.last_name_entry.place(
            anchor="center", relwidth=0.4, relx=0.5, rely=0.6, x=0, y=0
        )
        self.user_role_entry = tk.StringVar(value="Choose User Type")
        __values = ["Security Guard", "High Admin", "Low Admin"]
        self.user_role_optionmenu = tk.OptionMenu(
            self.register_user_frame2, self.user_role_entry, *__values, command=None
        )
        self.user_role_optionmenu.place(
            anchor="center", relwidth=0.4, relx=0.5, rely=0.76, x=0, y=0
        )
        self.user_role_optionmenu.configure(font="{arial} 16", justify="left")
        self.user_role_options = self.register_user_app.nametowidget(
            self.user_role_optionmenu.menuname
        )
        self.user_role_options.config(font="{arial} 16")
        self.user_role_label = tk.Label(self.register_user_frame2)
        self.user_role_label.configure(
            background="#F7FAE9", font="{arial} 16 {bold}", text="User Role"
        )
        self.user_role_label.place(anchor="center", relx=0.38, rely=0.67, x=0, y=0)
        self.register_user_frame2.place(
            anchor="center", relheight=0.82, relwidth=1.0, relx=0.5, rely=0.59
        )
        # Contains-the-edit-label-and-entry-widgets---------------------------------------------------------------------------------------------------------
        # Contains-the-logo-and-logotype---------------------------------------------------------------------------------------------------------

        self.register_user_frame1 = tk.Frame(self.register_user_app)
        self.register_user_frame1.configure(background="#fff000", height=200, width=200)
        self.school_logo_label = tk.Label(self.register_user_frame1)
        self.img_STICollegeBalagtasLogomedium = tk.PhotoImage(
            file="./SeekU/STI College Balagtas Logo medium.png"
        )
        self.school_logo_label.configure(
            background="#fff000",
            image=self.img_STICollegeBalagtasLogomedium,
            text="label1",
        )
        self.school_logo_label.place(anchor="center", relx=0.25, rely=0.5)
        self.register_user_frame1.place(
            anchor="center", relheight=0.17, relwidth=1.0, relx=0.5, rely=0.09
        )
        # Contains-the-logo-and-logotype---------------------------------------------------------------------------------------------------------

        # Main widget
        self.mainwindow = self.register_user_app
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.destroy_this_window)

    def destroy_this_window(self):
        self.admin_home_window.deiconify()
        self.refresh_func("IsActive")
        self.register_user_app.destroy() 

    def register_user_function(self):
        self.register = True
        username_var = self.username_entry.get()
        self.username_check(username_var)
        password_var = self.password_entry.get()
        self.password_check(password_var)
        first_name_var = self.first_name_entry.get()
        last_name_var = self.last_name_entry.get()
        user_role_var = self.user_role_entry.get()

        if ( len(username_var) != 0 and
            len(password_var) != 0 and
            len(first_name_var) != 0 and
            len(last_name_var) != 0 and
            len(user_role_var) != 0
            ) :
            if self.register == True:
                self.sql_query.register_user(
                    username_var,
                    password_var,
                    first_name_var,
                    last_name_var,
                    user_role_var,
                )
        else:
            messbx.showwarning("Warning", "Kindly ensure all fields are filled by entering a value.")

    def password_check(self,password):
        limit = self.sql_query.get_password_length()
        if len(password) < limit :
            messbx.showwarning("Warning", "The password should have " + str(limit) + " characters." )
            self.register = False
        else:
            self.register = True

    def username_check(self,username):
        if (self.sql_query.check_username(username)):
            messbx.showwarning("Warning", "The username \"" +username+"\" is already in use. ")
            self.register = False
        else:
            self.register = True

    def register_user(self, event=None):
        self.register_user_function()
