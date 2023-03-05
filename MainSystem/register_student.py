#!/usr/bin/python3
import tkinter as tk


class RegisterStudentApp:
    def __init__(self, master=None):
        #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------

        
        #PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # build ui
        self.register_student_app = tk.Tk() if master is None else tk.Toplevel(master)
        self.register_student_app.configure(
            background="#F7FAE9", height=200, width=200)
        width= self.register_student_app.winfo_screenwidth()               
        height= self.register_student_app.winfo_screenheight()               
        self.register_student_app.geometry("%dx%d" % (width, height))
        self.register_student_app.resizable(False, False)
        #Contains-the-camera-canvas--------------------------------------------------------------------------------------------------------- 
        self.register_stud_frame4 = tk.Frame(self.register_student_app)
        self.register_stud_frame4.configure(
            background="#0072bc", height=200, width=200)
        self.camera_canvas = tk.Canvas(self.register_stud_frame4)
        self.camera_canvas.configure(
            background="#0072bc",
            highlightbackground="#0072bc")
        self.camera_canvas.place(
            anchor="center",
            relheight=1.0,
            relwidth=1.0,
            relx=0.5,
            rely=0.5,
            x=0,
            y=0)
        self.register_stud_frame4.place(
            anchor="center",
            relheight=0.50,
            relwidth=0.50,
            relx=0.65,
            rely=0.47)
        #Contains-the-camera-canvas--------------------------------------------------------------------------------------------------------- 
        #Contains-return-button-the-app-name-logotype-and-app-logo--------------------------------------------------------------------------------------------------------- 
        self.register_stud_frame3 = tk.Frame(self.register_student_app)
        self.register_stud_frame3.configure(
            background="#F7FAE9", height=200, width=200)
        self.app_name_logo = tk.Label(self.register_stud_frame3)
        self.img_SeekULogotypesmall = tk.PhotoImage(
            file=".\SeekU\SeekU Logotype small.png")
        self.app_name_logo.configure(
            anchor="w",
            background="#F7FAE9",
            font="{arial black} 100 {}",
            foreground="#0072bc",
            image=self.img_SeekULogotypesmall,
            justify="left",
            text='SEEK')
        self.app_name_logo.place(anchor="center", relx=0.60, rely=.5)
        self.app_logo_label = tk.Label(self.register_stud_frame3)
        self.img_SeekUlarge = tk.PhotoImage(file=".\SeekU\SeekU large.png")
        self.app_logo_label.configure(
            background="#F7FAE9",
            image=self.img_SeekUlarge,
            text='label1')
        self.app_logo_label.place(anchor="center", relx=0.32, rely=0.5)
        self.return_button = tk.Button(self.register_stud_frame3)
        self.return_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text='Return')
        self.return_button.place(anchor="center", relx=0.935, rely=0.85, x=0, y=0)
        self.return_button.bind("<1>", self.return_func, add="")
        self.register_stud_frame3.place(
            anchor="center",
            relheight=0.25,
            relwidth=0.61,
            relx=0.65,
            rely=0.85)
        #Contains-return-button-the-app-name-logotype-and-app-logo--------------------------------------------------------------------------------------------------------- 
        #Contains-register-button-the-entry-widgets--------------------------------------------------------------------------------------------------------- 
        self.register_stud_frame2 = tk.Frame(self.register_student_app)
        self.register_stud_frame2.configure(
            background="#F7FAE9", height=200, width=200)
        self.register_stud_label = tk.Label(self.register_stud_frame2)
        self.register_stud_label.configure(
            background="#F7FAE9",
            font="{arial} 28 {bold}",
            text='Register Student')
        self.register_stud_label.place(
            anchor="center", relx=0.5, rely=0.05, x=0, y=0)
        self.student_num_label = tk.Label(self.register_stud_frame2)
        self.student_num_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text='Student No.')
        self.student_num_label.place(
            anchor="center", relx=0.33, rely=0.125, x=0, y=0)
        self.student_num_entry = tk.Entry(self.register_stud_frame2)
        self.student_num_entry.configure(font="{arial} 20 {}")
        self.student_num_entry.place(
            anchor="center",
            relwidth=0.62,
            relx=0.5,
            rely=0.165,
            x=0,
            y=0)
        self.first_name_label = tk.Label(self.register_stud_frame2)
        self.first_name_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text='First Name')
        self.first_name_label.place(
            anchor="center", relx=0.32, rely=0.22, x=0, y=0)
        self.first_name_entry = tk.Entry(self.register_stud_frame2)
        self.first_name_entry.configure(font="{arial} 20 {}")
        self.first_name_entry.place(
            anchor="center",
            relwidth=0.62,
            relx=0.5,
            rely=0.26,
            x=0,
            y=0)
        self.mid_name_label = tk.Label(self.register_stud_frame2)
        self.mid_name_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text='Middle Name')
        self.mid_name_label.place(
            anchor="center", relx=0.345, rely=0.315, x=0, y=0)
        self.mid_name_entry = tk.Entry(self.register_stud_frame2)
        self.mid_name_entry.configure(font="{arial} 20 {}")
        self.mid_name_entry.place(
            anchor="center",
            relwidth=0.62,
            relx=0.5,
            rely=0.355,
            x=0,
            y=0)
        self.last_name_label = tk.Label(self.register_stud_frame2)
        self.last_name_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text='Last Name')
        self.last_name_label.place(
            anchor="center", relx=0.32, rely=0.41, x=0, y=0)
        self.last_name_entry = tk.Entry(self.register_stud_frame2)
        self.last_name_entry.configure(font="{arial} 20 {}")
        self.last_name_entry.place(
            anchor="center",
            relwidth=0.62,
            relx=0.5,
            rely=0.45,
            x=0,
            y=0)
        self.program_label = tk.Label(self.register_stud_frame2)
        self.program_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text='Program')
        self.program_label.place(
            anchor="center", relx=0.295, rely=0.505, x=0, y=0)
        self.program_entry = tk.Entry(self.register_stud_frame2)
        self.program_entry.configure(font="{arial} 20 {}")
        self.program_entry.place(
            anchor="center",
            relwidth=0.62,
            relx=0.5,
            rely=0.545,
            x=0,
            y=0)
        self.section_label = tk.Label(self.register_stud_frame2)
        self.section_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text='Section')
        self.section_label.place(
            anchor="center", relx=0.28, rely=0.6, x=0, y=0)
        self.section_entry = tk.Entry(self.register_stud_frame2)
        self.section_entry.configure(font="{arial} 20 {}")
        self.section_entry.place(
            anchor="center",
            relwidth=0.62,
            relx=0.5,
            rely=0.64,
            x=0,
            y=0)
        self.contact_num_label = tk.Label(self.register_stud_frame2)
        self.contact_num_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text='Contact No.')
        self.contact_num_label.place(
            anchor="center", relx=0.33, rely=0.695, x=0, y=0)
        self.contact_num_entry = tk.Entry(self.register_stud_frame2)
        self.contact_num_entry.configure(font="{arial} 20 {}")
        self.contact_num_entry.place(
            anchor="center",
            relwidth=0.62,
            relx=0.5,
            rely=0.735,
            x=0,
            y=0)
        self.address_label = tk.Label(self.register_stud_frame2)
        self.address_label.configure(
            background="#F7FAE9",
            cursor="arrow",
            font="{arial} 20 {bold}",
            text='Address')
        self.address_label.place(
            anchor="center", relx=0.295, rely=0.79, x=0, y=0)
        self.address_entry = tk.Entry(self.register_stud_frame2)
        self.address_entry.configure(font="{arial} 20 {}")
        self.address_entry.place(
            anchor="center",
            relwidth=0.62,
            relx=0.5,
            rely=0.83,
            x=0,
            y=0)
        self.register_button = tk.Button(self.register_stud_frame2)
        self.register_button.configure(
            background="#0072bc",
            font="{arial} 20 {bold}",
            foreground="#ffffff",
            text='Register')
        self.register_button.place(anchor="center", relx=0.5, rely=0.92, x=0, y=0)
        self.register_button.bind("<1>", self.register_student, add="")
        self.register_stud_frame2.place(
            anchor="center",
            relheight=0.86,
            relwidth=0.35,
            relx=0.18,
            rely=0.565)
        #Contains-register-button-the-entry-widgets--------------------------------------------------------------------------------------------------------- 
        #Contains-school-logo-------------------------------------------------------------------------------------------------------------------------------------
        self.register_stud_frame1 = tk.Frame(self.register_student_app)
        self.register_stud_frame1.configure(
            background="#fff000", height=200, width=200)
        self.school_logo_label = tk.Label(self.register_stud_frame1)
        self.img_STICollegeBalagtasLogomedium = tk.PhotoImage(
            file=".\SeekU\STI College Balagtas Logo medium.png")
        self.school_logo_label.configure(
            background="#fff000",
            image=self.img_STICollegeBalagtasLogomedium,
            text='label1')
        self.school_logo_label.place(anchor="center", relx=.25, rely=0.5)
        self.register_stud_frame1.place(
            anchor="center",
            relheight=0.13,
            relwidth=1.0,
            relx=0.5,
            rely=0.065)
        #Contains-school-logo-------------------------------------------------------------------------------------------------------------------------------------

        # Main widget
        self.mainwindow = self.register_student_app
        self.mainwindow.wm_attributes('-fullscreen', 'True')

    def run(self):
        self.mainwindow.mainloop()

    def register_student(self, event=None):
        # save infos
        pass
    def return_func(self, event=None):
        # return to admin module
        pass


if __name__ == "__main__":
    app = RegisterStudentApp()
    app.run()
