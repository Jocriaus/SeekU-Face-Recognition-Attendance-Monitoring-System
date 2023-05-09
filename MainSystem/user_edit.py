#!/usr/bin/python3
import tkinter as tk
import tkinter.messagebox as messbx
import query_mod as qry
import re


class EditUserApp:
    def __init__(self, un, pw, ufn, uln, ut, us, admin_hom, refresh, this_is_archive):
        # build ui
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        self.this_is_archived = this_is_archive
        self.admin_home_window = admin_hom
        self.username = un
        self.password = pw
        self.firstname = ufn
        self.lastname = uln
        self.user_type = ut
        self.user_status = us
        self.first_stat = us
        self.sql_query = qry.dbQueries()
        self.edit_bool = True
        self.refresh_func = refresh
        self.saved = False
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------

        self.edit_user_app = tk.Toplevel()
        self.edit_user_app.configure(background="#F7FAE9", height=200, width=200)
        self.edit_user_app.geometry("600x700")
        self.edit_user_app.resizable(False, False)
        self.edit_user_app.title("SeekU - Edit User")
        self.edit_user_app.iconbitmap(".\SeekU\SeekU.ico")
        # Contains-the-edit-label-and-entry-widgets---------------------------------------------------------------------------------------------------------
        self.edit_user_frame2 = tk.Frame(self.edit_user_app)
        self.edit_user_frame2.configure(background="#F7FAE9", height=200, width=200)
        self.edit_user_label = tk.Label(self.edit_user_frame2)
        self.edit_user_label.configure(
            background="#F7FAE9", font="{arial} 24 {bold}", text="Edit User"
        )
        self.edit_user_label.place(anchor="center", relx=0.5, rely=0.05, x=0, y=0)
        self.username_label = tk.Label(self.edit_user_frame2)
        self.username_label.configure(
            background="#F7FAE9", font="{arial} 16 {bold}", text="Username"
        )
        self.username_label.place(anchor="center", relx=0.385, rely=0.14, x=0, y=0)
        self.username_entry = tk.Entry(self.edit_user_frame2)
        self.username_entry.configure(font="{arial} 14 {}")
        self.username_entry.place(
            anchor="center", relwidth=0.4, relx=0.5, rely=0.19, x=0, y=0
        )
        self.password_label = tk.Label(self.edit_user_frame2)
        self.password_label.configure(
            background="#F7FAE9", font="{arial} 16 {bold}", text="Password"
        )
        self.password_label.place(anchor="center", relx=0.385, rely=0.26, x=0, y=0)
        self.password_entry = tk.Entry(self.edit_user_frame2)
        self.password_entry.configure(font="{arial} 14 {}", show="•")
        self.password_entry.place(
            anchor="center", relwidth=0.4, relx=0.5, rely=0.31, x=0, y=0
        )
        self.first_name_label = tk.Label(self.edit_user_frame2)
        self.first_name_label.configure(
            background="#F7FAE9", font="{arial} 16 {bold}", text="First Name"
        )
        self.first_name_label.place(anchor="center", relx=0.39, rely=0.39, x=0, y=0)
        self.first_name_entry = tk.Entry(self.edit_user_frame2)
        self.first_name_entry.configure(font="{arial} 14 {}")
        self.first_name_entry.place(
            anchor="center", relwidth=0.4, relx=0.5, rely=0.44, x=0, y=0
        )
        self.last_name_label = tk.Label(self.edit_user_frame2)
        self.last_name_label.configure(
            background="#F7FAE9", font="{arial} 16 {bold}", text="Last Name"
        )
        self.last_name_label.place(anchor="center", relx=0.39, rely=0.52, x=0, y=0)
        self.last_name_entry = tk.Entry(self.edit_user_frame2)
        self.last_name_entry.configure(font="{arial} 14 {}")
        self.last_name_entry.place(
            anchor="center", relwidth=0.4, relx=0.5, rely=0.58, x=0, y=0
        )
        self.user_role_var = tk.StringVar(value="Staff")
        __values = ["Security Guard", "System Admin", "Staff"]
        self.user_role_optionmenu = tk.OptionMenu(
            self.edit_user_frame2, self.user_role_var, *__values, command=None
        )
        self.user_role_optionmenu.place(
            anchor="center", relwidth=0.4, relx=0.5, rely=0.7, x=0, y=0
        )
        self.user_role_optionmenu.configure(font="{arial} 16", justify="left")
        self.user_role_options = self.edit_user_app.nametowidget(
            self.user_role_optionmenu.menuname
        )
        self.user_role_options.config(font="{arial} 16")
        self.user_role_label = tk.Label(self.edit_user_frame2)
        self.user_role_label.configure(
            background="#F7FAE9", font="{arial} 16 {bold}", text="User Role"
        )
        self.user_role_label.place(anchor="center", relx=0.38, rely=0.64, x=0, y=0)
        self.user_status_label = tk.Label(self.edit_user_frame2)
        self.user_status_label.configure(
            background="#F7FAE9", font="{arial} 16 {bold}", text="User Status"
        )
        self.user_status_label.place(anchor="center", relx=0.395, rely=0.76, x=0, y=0)

        # variable for the radiobuttons, to connect them
        self.stat_var = tk.StringVar()
        self.stat_var.set("Active")
        self.active_radiobutton = tk.Radiobutton(self.edit_user_frame2)
        self.active_radiobutton.configure(
            background="#F7FAE9",
            font="{arial} 14 {}",
            text="Active",
            variable=self.stat_var,
            value="IsActive",
        )
        self.active_radiobutton.place(anchor="center", relx=0.4, rely=0.82, x=0, y=0)
        self.inactive_radiobutton = tk.Radiobutton(self.edit_user_frame2)
        self.inactive_radiobutton.configure(
            background="#F7FAE9",
            font="{arial} 14 {}",
            text="Archive",
            variable=self.stat_var,
            value="IsArchived",
        )
        self.inactive_radiobutton.place(anchor="center", relx=0.6, rely=0.82, x=0, y=0)

        self.edit_user_button = tk.Button(self.edit_user_frame2)
        self.edit_user_button.configure(
            background="#0072bc",
            font="{arial black} 20 {}",
            foreground="#F7FAE9",
            text="Edit",
        )
        self.edit_user_button.place(
            anchor="center", relheight=0.08, relwidth=0.27, relx=0.3, rely=0.9
        )
        self.edit_user_button.bind("<ButtonPress>", self.edit_user, add="")

        self.save_user_button = tk.Button(self.edit_user_frame2)
        self.save_user_button.configure(
            background="#0072bc",
            font="{arial black} 20 {}",
            foreground="#F7FAE9",
            text="Save",
        )
        self.save_user_button.place(
            anchor="center", relheight=0.08, relwidth=0.27, relx=0.7, rely=0.9
        )
        self.save_user_button.bind("<ButtonPress>", self.save_user, add="")
        self.edit_user_frame2.place(
            anchor="center", relheight=0.82, relwidth=1.0, relx=0.5, rely=0.59
        )
        self.edit_user_frame2.place(
            anchor="center", relheight=0.82, relwidth=1.0, relx=0.5, rely=0.59
        )

        # Contains-the-edit-label-and-entry-widgets---------------------------------------------------------------------------------------------------------
        # Contains-the-logo-and-logotype---------------------------------------------------------------------------------------------------------

        self.edit_user_frame1 = tk.Frame(self.edit_user_app)
        self.edit_user_frame1.configure(background="#FFF875", height=200, width=200)
        self.school_logo_label = tk.Label(self.edit_user_frame1)
        self.img_STICollegeBalagtasLogomedium = tk.PhotoImage(
            file="./SeekU/STI College Balagtas Logo medium.png"
        )
        self.school_logo_label.configure(
            background="#FFF875",
            image=self.img_STICollegeBalagtasLogomedium,
            text="label1",
        )
        self.school_logo_label.place(anchor="center", relx=0.25, rely=0.5)
        self.edit_user_frame1.place(
            anchor="center", relheight=0.17, relwidth=1.0, relx=0.5, rely=0.09
        )
        # Contains-the-logo-and-logotype---------------------------------------------------------------------------------------------------------
        self.selected_user()

        self.disable_entry()
        # Main widget
        self.mainwindow = self.edit_user_app
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.destroy_this_window)
        self.center(self.mainwindow)
        self.mainwindow.attributes("-topmost", True)
        self.mainwindow.attributes("-topmost", False)
        self.mainwindow.grab_set()


    def destroy_this_window(self):
        if ( str(self.username_entry.get()) == str(self.username) and
            str(self.password_entry.get()) == str(self.password) and 
            str(self.first_name_entry.get()) == str(self.firstname) and 
            str(self.last_name_entry.get()) == str(self.lastname) and 
            str(self.user_role_var.get()) == str(self.user_type) and 
            str(self.stat_var.get()) == str(self.user_status)):
            
            self.edit_user_app.grab_release()
            if self.this_is_archived:
                self.refresh_func("IsArchived")
            else:
                self.refresh_func("IsActive")
            self.edit_user_app.destroy()
        elif self.saved:
            self.edit_user_app.grab_release()
            if self.this_is_archived:
                self.refresh_func("IsArchived")
            else:
                self.refresh_func("IsActive")
            self.edit_user_app.destroy()
        else:
            result = messbx.askokcancel("Confirm Action", "Do you wish to proceed without saving?")
            if result:
                self.edit_user_app.grab_release()
                if self.this_is_archived:
                    self.refresh_func("IsArchived")
                else:
                    self.refresh_func("IsActive")
                self.edit_user_app.destroy()

    # disables entry widgets
    def disable_entry(self):
        self.username_entry.configure(state="disabled")
        self.password_entry.configure(state="disabled")
        self.last_name_entry.configure(state="disabled")
        self.first_name_entry.configure(state="disabled")
        self.user_role_optionmenu.configure(state="disabled")
        self.active_radiobutton.configure(state="disabled")
        self.inactive_radiobutton.configure(state="disabled")

    # enables entry widgets
    def enable_entry(self):
        self.password_entry.configure(state="normal")
        self.last_name_entry.configure(state="normal")
        self.first_name_entry.configure(state="normal")
        self.user_role_optionmenu.configure(state="normal")
        self.active_radiobutton.configure(state="normal")
        self.inactive_radiobutton.configure(state="normal")

    def selected_user(self):

        self.username_entry.insert(0, self.username)
        self.password_entry.insert(0, self.password)
        self.first_name_entry.insert(0, self.firstname)
        self.last_name_entry.insert(0, self.lastname)
        self.user_role_var.set(value=self.user_type)
        self.stat_var.set(value=self.user_status)

        # if status is = IsActive then stat var set to Active else Inactive

    def center(self, win):
        win.update()
        w_req, h_req = win.winfo_width(), win.winfo_height()
        w_form = win.winfo_rootx() - win.winfo_x()
        w = w_req + w_form * 2
        h = h_req + (win.winfo_rooty() - win.winfo_y()) + w_form
        x = (win.winfo_screenwidth() // 2) - (w // 2)
        y = (win.winfo_screenheight() // 2) - (h // 2)
        win.geometry("{0}x{1}+{2}+{3}".format(w_req, h_req, x, y))

    def update_user(self):
        update = True
        username_var = self.username_entry.get()
        password_var = self.password_entry.get()
        firstname_var = self.first_name_entry.get()
        lastname_var = self.last_name_entry.get()
        user_role_variable = self.user_role_var.get()
        user_status_var = self.stat_var.get()
        update = self.password_check(password_var)
        if (
            len(username_var) != 0
            and len(password_var) != 0
            and len(firstname_var) != 0
            and len(lastname_var) != 0
            and len(user_role_variable) != 0
            and len(user_status_var) != 0
        ):
            input_values = [
                username_var,
                password_var,
                firstname_var,
                lastname_var,
                user_role_variable,
                user_status_var,
            ]

            concatenated_inputs = "".join(input_values)
            pattern = re.compile("[^a-zA-Z0-9 \-@.,]")
            if not pattern.search(concatenated_inputs):
                if (firstname_var.replace(" ", "").isalpha() and
                    lastname_var.replace(" ", "").isalpha()
                    ):
                    if update:
                        result = messbx.askokcancel("Confirm Action", "Do you wish to proceed without saving?")
                        if result:
                            self.sql_query.update_user(
                                username_var,
                                password_var,
                                firstname_var,
                                lastname_var,
                                user_role_variable,
                                user_status_var,
                            )
                            self.saved = True
                            messbx.showinfo(
                                "Success",
                                "The user record has been updated successfully.",
                            )
                else:
                    messbx.showwarning(
                        "Warning",
                        "There is an invalid character in the input for the name of the user.",
                    )
            else:
                messbx.showwarning("Warning", "The input contains special characters.")
        else:
            messbx.showwarning(
                "Warning", "Kindly ensure all fields are filled by entering a value."
            )

    def password_check(self, password):
        limit = self.sql_query.get_password_length()
        if len(password) < limit:
            messbx.showwarning(
                "Warning", "The password length limit is " + str(limit) + "."
            )
            update = False
            return update
        else:
            update = True
            return update

    # enables and disables entry
    def edit_user(self, event=None):
        if self.edit_bool == True:
            self.enable_entry()
            self.edit_bool = False
        elif self.edit_bool == False:
            self.disable_entry()
            self.edit_bool = True

    def save_user(self, event=None):
        self.update_user()
