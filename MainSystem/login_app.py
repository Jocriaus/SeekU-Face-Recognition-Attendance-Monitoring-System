import tkinter as tk
import tkinter.messagebox as messbx
import query_mod as qry
import client_cam as cC
import time
import sys


class LoginApp:
    def __init__(self, master=None):
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.sql_query = qry.dbQueries()
        self.sql_query.default_settings_if_not_exist()
        self.sql_query.default_user_if_not_exist()
        self.user = "None"
        self.locked = False
        # will be used for account locked
        self.init_time = 0
        self.current_time = 0
        self.passed_time = 0
        self.time_locked = 15.0
        self.timer = 0.0
        self.tries = self.sql_query.get_login_attempts()
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # build ui
        self.log_in_app = tk.Tk() if master is None else tk.Toplevel(master)
        self.log_in_app.configure(background="#0072bc", height=200, width=200)
        self.log_in_app.geometry("500x500")
        self.log_in_app.resizable(False, False)
        self.log_in_app.title("SeekU - Login")
        self.log_in_app.iconbitmap(".\SeekU\SeekU.ico")
        # Contains-the-entry-and-button---------------------------------------------------------------------------------------------------------
        self.log_in_frame2 = tk.Frame(self.log_in_app)
        self.log_in_frame2.configure(background="#0072bc", height=200, width=200)
        self.un_label = tk.Label(self.log_in_frame2)
        self.un_label.configure(
            background="#0072bc",
            font="{arial} 20 {}",
            foreground="#F7FAE9",
            text="Username",
        )
        self.un_label.place(anchor="center", relx=0.0, rely=0.0, x=150, y=190)
        self.un_entry = tk.Entry(self.log_in_frame2)
        self.un_entry.configure(
            background="#F7FAE9", font="{arial} 18 {}", foreground="#010303"
        )
        self.un_entry.place(
            anchor="center", height=40, relx=0.0, rely=0.0, width=320, x=250, y=225
        )
        self.pw_label = tk.Label(self.log_in_frame2)
        self.pw_label.configure(
            background="#0072bc",
            font="{arial} 20 {}",
            foreground="#F7FAE9",
            justify="left",
            text="Password",
        )
        self.pw_label.place(anchor="center", relx=0.0, rely=0.0, x=150, y=285)
        self.pw_entry = tk.Entry(self.log_in_frame2)
        self.pw_entry.configure(
            background="#F7FAE9", font="{arial} 18 {}", foreground="#010303", show="•"
        )
        self.pw_entry.place(
            anchor="center", height=40, relx=0.0, rely=0.0, width=320, x=250, y=320
        )
        self.login_button = tk.Button(self.log_in_frame2)
        self.login_button.configure(
            background="#F7FAE9",
            default="active",
            font="{arial Black} 20 {}",
            foreground="#0072bc",
            justify="center",
            relief="ridge",
            text="Login",
            width=10,
        )
        self.login_button.place(
            anchor="center",
            height=50,
            relheight=0.0,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=200,
            x=250,
            y=425,
        )
        self.login_button.bind("<ButtonPress>", self.login_press, add="")
        self.log_in_frame2.place(anchor="center", height=500, width=500, x=250, y=250)
        # Contains-the-entry-and-button---------------------------------------------------------------------------------------------------------
        # Contains-the-logo-and-logotype---------------------------------------------------------------------------------------------------------

        self.log_in_frame = tk.Frame(self.log_in_app)
        self.log_in_frame.configure(background="#F7FAE9", height=200, width=200)
        self.sti_logo = tk.Label(self.log_in_frame)
        self.img_SeekU = tk.PhotoImage(file=".\SeekU\SeekU small.png")
        self.sti_logo.configure(background="#F7FAE9", image=self.img_SeekU)
        self.sti_logo.place(anchor="center", relx=0.0, rely=0.0, x=150, y=80)
        self.app_name_logo = tk.Label(self.log_in_frame)
        self.img_SeekULogotypemicro = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype micro.png"
        )
        self.app_name_logo.configure(
            background="#F7FAE9",
            foreground="#0072bc",
            image=self.img_SeekULogotypemicro,
            relief="flat",
            text="SEEK",
        )
        self.app_name_logo.place(anchor="center", relx=0.052, rely=0.04, x=290, y=80)
        self.log_in_frame.place(anchor="center", height=150, width=500, x=250, y=75)
        # Contains-the-logo-and-logotype---------------------------------------------------------------------------------------------------------
        # this protocol will do a function after pressing the close button.
        self.log_in_app.protocol("WM_DELETE_WINDOW", self.exit_program)

        # Main widget
        self.mainwindow = self.log_in_app

        # refer to the function's comments
        self.center(self.mainwindow)

    # -----------------------------------------------------------------------------------------

    # this function will run the main window/the app.
    def run(self):
        self.mainwindow.mainloop()

    # this function will destroy the window and closes the system/program.
    def exit_program(self):
        sys.exit()

    # this function will hide the window after logging in.
    def hide_this_window(self):
        self.log_in_app.withdraw()

    # this function will clear the contents of the entry after logging in.
    def clear_entry(self):
        self.un_entry.delete(0, "end")
        self.pw_entry.delete(0, "end")

    # this function will enable the user to enter to the system
    def login_logic(self):
        if not self.locked:
            self.username_var = self.un_entry.get()
            self.password_var = self.pw_entry.get()
            if (len(self.username_var) != 0) and (len(self.password_var) != 0):
                if self.sql_query.login_entry(self.username_var, self.password_var):

                    # test for admin = jus    jus123
                    # test for security guard = jc   123

                    print(
                        self.sql_query.check_user_type(self.username_var, self.password_var)
                    )
                    if (
                        self.sql_query.check_user_type(self.username_var, self.password_var)
                        == "Security Guard"
                    ):
                        print("login")
                        # add message box
                        self.hide_this_window()
                        self.clear_entry()
                        self.user = "Security Guard"
                        cC.ClientCameraSelectApp(self.user, self.log_in_app)
                    elif (
                        self.sql_query.check_user_type(self.username_var, self.password_var)
                        == "High Admin"
                        or self.sql_query.check_user_type(
                            self.username_var, self.password_var
                        )
                        == "Low Admin"
                    ):
                        print("login")
                        # add message box
                        self.hide_this_window()
                        self.clear_entry()
                        self.user = self.sql_query.check_user_type(
                            self.username_var, self.password_var
                        )
                        cC.ClientCameraSelectApp(self.user, self.log_in_app)

                elif (self.sql_query.login_entry(self.username_var, self.password_var) == False):
                    self.tries = self.tries-1
                    if self.tries == 1:
                        if self.init_time == 0:
                            self.init_time = time.time()
                        self.locked = True
                        messbx.showwarning(
                            "Warning", "The username and password entered do not match. You have remaining {} tries".format(self.tries))
                        self.time_passing()
                    else:
                        
                        messbx.showwarning(
                            "Warning", "The username and password entered do not match. You have remaining {} tries".format(self.tries))
                        

            else:
                messbx.showwarning(
                    "Warning ", "Kindly ensure all fields are filled by entering a value."
                )

        else:
            messbx.showwarning(
                    "Warning", "Your account is curretly locked. Please try after {:.0f} seconds".format(self.timer)
                ) 

    def time_passing(self):
        self.time_locked = 15.0
        self.current_time = time.time()
        self.passed_time = self.current_time - self.init_time
        self.timer = self.time_locked - self.passed_time
        if self.timer > 0:
            self.log_in_app.after(15, self.time_passing)
        else:
            self.init_time = 0
            self.locked = False
            self.tries = self.sql_query.get_login_attempts()

    # this function will center the window
    def center(self, win):
        win.update()
        w_req, h_req = win.winfo_width(), win.winfo_height()
        w_form = win.winfo_rootx() - win.winfo_x()
        w = w_req + w_form * 2
        h = h_req + (win.winfo_rooty() - win.winfo_y()) + w_form
        x = (win.winfo_screenwidth() // 2) - (w // 2)
        y = (win.winfo_screenheight() // 2) - (h // 2)
        win.geometry("{0}x{1}+{2}+{3}".format(w_req, h_req, x, y))

    # this command function is associated with the login button
    def login_press(self, event=None):
        self.login_logic()


if __name__ == "__main__":
    app = LoginApp()
    app.center(app.mainwindow)
    app.run()
