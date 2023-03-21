import tkinter as tk
import tkinter.ttk as ttk
import Treeview_table as tv


class Mainsys:
    def __init__(self, master=None):
        self.treeview = tv.TreeviewGUI()
        self.root = tk.Tk()
        self.frame = self.treeview.student_report_treeview(self.root)

    def run(self):
        self.treeview.student_report_treeview_root.mainloop()


if __name__ == "__main__":
    app = Mainsys()
    app.run()
