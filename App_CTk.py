from customtkinter import *
from tkinter import filedialog

class App():
    def __init__(self):
        self.app = CTk()

        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()

        window_width = 1480
        window_height = 750

        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        self.app.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        self.min_frame_width = 1280 / 5

        self.frame = CTkFrame(self.app, width=self.min_frame_width, height=window_height, fg_color="gray")
        self.frame.place(relx=1.0, rely=0.0, anchor='ne', relheight=1.0)

        self.file_label = CTkLabel(self.frame, text="", anchor='w')
        self.file_label.place(relx=0.5, rely=0.55, anchor='center')

        self.open_file_button = CTkButton(self.frame, text="Open File", command=self.open_file)
        self.open_file_button.place(relx=0.5, rely=0.6, anchor='center')

        self.submit_button = CTkButton(self.frame, text="Submit", command=self.submit)
        self.submit_button.place(relx=0.5, rely=0.85, anchor='center')

        self.app.bind("<Configure>", self.on_resize)

        self.app.mainloop()

    def open_file(self):
        file_path = filedialog.askopenfilename()

        self.file_label.configure(text=f"Selected file: {file_path}")

    def submit(self):
        print("Submit button clicked!")

    def on_resize(self, event):
        new_frame_width = max(int(self.app.winfo_width() / 5), self.min_frame_width)
        frame_height = self.app.winfo_height()
        self.frame.configure(width=new_frame_width, height=frame_height)

        label_width = int(new_frame_width * 0.8)
        self.file_label.configure(width=label_width)

if __name__ == '__main__':
    App()
