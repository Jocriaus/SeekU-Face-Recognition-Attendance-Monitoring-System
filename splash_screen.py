import tkinter as tk
import face_recog_mod as mf
import client_face_recog as cFG

class SplashScreenWin:
    def __init__(self,vid_source, login_mod, sel_cam, home_mod,detection,tolerance, file_path):
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------
        # Color ------------
        self.sub_complimentary_color = "#808080" #gray
        self.main_color = "#0072bc" #Blue
        self.sub_color = "#FFF875" #light Yellow
        self.complimentary_color_1 = "#E7E7E7" #light  gray
        self.complimentary_color_2 = "#F7FAE9" #Cream Color
        self.hover_color = "#FFF200" #pure Yellow
        # Color ------------
        # PRE-LOAD-ASSIGNMENT-------------------------------------------------------------------------------------------

        self.vid_source = vid_source
        self.file_path = file_path
        self.login_mod = login_mod
        self.sel_cam = sel_cam
        self.home_mod = home_mod
        self.detection_time = detection
        self.tolerance = tolerance
        self.splashscreen_app = tk.Toplevel()
        self.splashscreen_app.configure(background=self.main_color,height=200, width=200)
        self.splashscreen_app.geometry("1000x700")
        self.splashscreen_app.resizable(False, False)
        self.splashscreen_app.overrideredirect(True)
        self.splashscreen = tk.Label(self.splashscreen_app)
        self.img_splashscreen = tk.PhotoImage(file=".\SeekU\SeekU Splash Screen.png")
        self.splashscreen.configure(
            background=self.complimentary_color_2, image=self.img_splashscreen, text="label1"
        )
        self.splashscreen.place(
            anchor="center", relheight=1, relwidth=1, relx=0.50, rely=0.5
        )
        self.mainwindow = self.splashscreen_app
        self.message = tk.Label(self.splashscreen_app)
        self.message.configure(
            anchor="center",
            background=self.complimentary_color_2,
            font="{lucida} 10 {}",
            foreground="#000000",
            justify="left",
            text="Image processing may take up to a few minutes. Please wait patiently."
        )
        self.message.place(
            anchor="center", relx=0.5, rely=0.975
        )
        self.center(self.mainwindow)

        self.splashscreen_app.after(1000, self.callmf)
        

    def callmf(self):
        self.fr_vid = mf.FaceRecognition(self.vid_source,self.tolerance,self.detection_time, self.file_path, 1280, 720)
        cFG.ClientFaceRecogApp(self.login_mod,self.sel_cam,self.home_mod,self.splashend,self.fr_vid)

    def splashend(self):
        self.splashscreen_app.destroy()

    def center(self, win):
        win.update()
        w_req, h_req = win.winfo_width(), win.winfo_height()
        w_form = win.winfo_rootx() - win.winfo_x()
        w = w_req + w_form * 2
        h = h_req + (win.winfo_rooty() - win.winfo_y()) + w_form
        x = (win.winfo_screenwidth() // 2) - (w // 2)
        y = (win.winfo_screenheight() // 2) - (h // 2)
        win.geometry("{0}x{1}+{2}+{3}".format(w_req, h_req, x, y))