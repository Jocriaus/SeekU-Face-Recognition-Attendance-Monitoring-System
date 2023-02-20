import tkinter as tk


class AddVisitorApp:
    def __init__(self, vid_source, login_mod, sel_cam, home_mod, ):

        #assignment for passed parameters
        self.video_source = vid_source
        self.login_window = login_mod
        self.sel_cam_window = sel_cam
        self.home_window = home_mod


        # build ui
        self.add_visitor_app = tk.Toplevel()
        self.add_visitor_app.configure(
            background="#F7FAE9", height=200, width=200)
        width= self.add_visitor_app.winfo_screenwidth()               
        height= self.add_visitor_app.winfo_screenheight() 
        self.add_visitor_app.geometry("%dx%d" % (width, height))
        self.add_visitor_app.resizable(False, False)


#-----------------------------------------------------------------------------------------
        self.add_visitor_frame3 = tk.Frame(self.add_visitor_app)
        self.add_visitor_frame3.configure(
            background="#0072bc", height=200, width=200)
        self.camera_canvas = tk.Canvas(self.add_visitor_frame3)
        self.camera_canvas.configure(
            background="#0072bc",
            highlightbackground="#0072bc")
        self.camera_canvas.place(
            anchor="center",
            relheight=1.0,
            relwidth=1.0,
            relx=.5,
            rely=.5,
            x=0,
            y=0)
        self.add_visitor_frame3.place(
            anchor="center",
            relheight=0.60,
            relwidth=0.60,
            relx=0.68,
            rely=0.36)


#-----------------------------------------------------------------------------------------
        self.add_visitor_frame2 = tk.Frame(self.add_visitor_app)
        self.add_visitor_frame2.configure(
            background="#F7FAE9", height=200, width=200)
        self.app_name_labelS = tk.Label(self.add_visitor_frame2)
        self.app_name_labelS.configure(
            anchor="w",
            background="#F7FAE9",
            font="{arial black} 100 {}",
            foreground="#0072bc",
            justify="left",
            text='SEEK')
        self.app_name_labelS.place(anchor="center", relx=0.70, rely=.5)
        self.app_name_labelU = tk.Label(self.add_visitor_frame2)
        self.app_name_labelU.configure(
            anchor="w",
            background="#F7FAE9",
            font="{arial black} 100 {}",
            foreground="#FFF200",
            justify="left",
            text='U')
        self.app_name_labelU.place(anchor="center", relx=0.87, rely=0.5)
        self.app_logo_label = tk.Label(self.add_visitor_frame2)
        self.img_SeekUmedium = tk.PhotoImage(file=".\SeekU\SeekU medium.png")
        self.app_logo_label.configure(
            background="#F7FAE9",
            image=self.img_SeekUmedium,
            text='label1')
        self.app_logo_label.place(anchor="center", relx=0.47, rely=0.50)
        self.sign_out_button = tk.Button(self.add_visitor_frame2)
        self.sign_out_button.configure(
            font="{arial black} 20 {}",
            foreground="#0072bc",
            text='Sign out')
        self.sign_out_button.place(
            anchor="center",
            relheight=0.15,
            relwidth=0.1,
            relx=0.93,
            rely=0.85)
        self.sign_out_button.bind("<ButtonPress>", self.sign_out, add="")
        self.add_visitor_frame2.place(
            anchor="center",
            relheight=0.3,
            relwidth=1.0,
            relx=0.50,
            rely=0.85)




#-----------------------------------------------------------------------------------------            
        self.add_visitor_frame = tk.Frame(self.add_visitor_app)
        self.add_visitor_frame.configure(
            background="#F7FAE9", height=200, width=200)
        self.snapshot_button = tk.Button(self.add_visitor_frame)
        self.snapshot_button.configure(
            font="{arial black} 30 {}",
            foreground="#0072bc",
            text='Snapshot')
        self.snapshot_button.place(
            anchor="center",
            relheight=0.1,
            relwidth=0.50,
            relx=.5,
            rely=.90)
        self.snapshot_button.bind("<ButtonPress>", self.save_info, add="")
        self.school_logo_label = tk.Label(self.add_visitor_frame)
        self.img_STICollegeBalagtasLogo = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo.png")
        self.school_logo_label.configure(
            background="#F7FAE9",
            image=self.img_STICollegeBalagtasLogo,
            text='label1')
        self.school_logo_label.place(
            anchor="center",
            relx=.5,
            rely=0.12)
        self.last_name_label = tk.Label(self.add_visitor_frame)
        self.last_name_label.configure(
            background="#F7FAE9",
            font="{arial} 36 {}",
            text='Last Name')
        self.last_name_label.place(
            anchor="center", relx=0.34, rely=0.25, x=0, y=0)
        self.last_name_entry = tk.Entry(self.add_visitor_frame)
        self.last_name_entry.configure(
            borderwidth=2,
            font="{arial} 30 {}",
            highlightbackground="#000000",
            highlightthickness=2)
        self.last_name_entry.place(
            anchor="center", relx=0.55, rely=0.31, x=0, y=0)
        self.first_name_label = tk.Label(self.add_visitor_frame)
        self.first_name_label.configure(
            background="#F7FAE9",
            font="{arial} 36 {}",
            text='First Name')
        self.first_name_label.place(
            anchor="center", relx=0.34, rely=0.40, x=0, y=0)
        self.first_name_entry = tk.Entry(self.add_visitor_frame)
        self.first_name_entry.configure(
            borderwidth=2,
            font="{arial} 30 {}",
            highlightbackground="#000000",
            highlightthickness=2)
        self.first_name_entry.place(
            anchor="center", relx=0.55, rely=0.46, x=0, y=0)
        self.contact_no_label = tk.Label(self.add_visitor_frame)
        self.contact_no_label.configure(
            background="#F7FAE9",
            font="{arial} 36 {}",
            text='Contact No.')
        self.contact_no_label.place(
            anchor="center", relx=0.36, rely=0.55, x=0, y=0)
        self.contact_no_entry = tk.Entry(self.add_visitor_frame)
        self.contact_no_entry.configure(
            borderwidth=2,
            font="{arial} 30 {}",
            highlightbackground="#000000",
            highlightthickness=2)
        self.contact_no_entry.place(
            anchor="center", relx=0.55, rely=.61, x=0, y=0)
        self.address_label = tk.Label(self.add_visitor_frame)
        self.address_label.configure(
            background="#F7FAE9",
            font="{arial} 36 {}",
            text='Address')
        self.address_label.place(
            anchor="center", relx=0.29, rely=0.70, x=0, y=0)
        self.address_entry = tk.Entry(self.add_visitor_frame)
        self.address_entry.configure(
            borderwidth=2,
            font="{arial} 30 {}",
            highlightbackground="#000000",
            highlightthickness=2)
        self.address_entry.place(
            anchor="center", relx=0.55, rely=0.76, x=0, y=0)
        self.add_visitor_frame.place(
            anchor="center",
            relheight=1.0,
            relwidth=0.35,
            relx=0.17,
            rely=0.5)

        # Main widget
        self.mainwindow = self.add_visitor_app
        self.mainwindow.wm_attributes('-fullscreen', 'True')

#-----------------------------------------------------------------------------------------
    def show_home_window(self):
        self.home_window.deiconify()
        self.add_visitor_app.destroy()
        # add additional function for destroying camera

    def sign_out(self, event=None):
        self.show_home_window()

    def save_info(self, event=None):
        pass


if __name__ == "__main__":
    app = AddVisitorApp()
    app.run()
