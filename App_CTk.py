from customtkinter import *
from tkinter import filedialog
import os
from back import start


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

        # Create a CTkTabview on the right side
        self.tab_view = CTkTabview(self.app, width=self.min_frame_width, height=window_height)
        self.tab_view.place(relx=1.0, rely=0.0, anchor='ne')

        # Create two tabs
        self.tab1 = self.tab_view.add("Train")
        self.tab2 = self.tab_view.add("Predict")

        self.setup_tab1()
        self.setup_tab2()

        self.app.mainloop()

        

    def setup_tab1(self):
        self.file_label1 = CTkLabel(self.tab1, text="Selected file:", anchor='w')
        self.file_label1.place(relx=0.5, rely=0.14, anchor='center')

        self.open_file_button1 = CTkButton(self.tab1, text="Open File", command=self.open_file)
        self.open_file_button1.place(relx=0.5, rely=0.18, anchor='center')

        label0 = CTkLabel(self.tab1, text="Method", anchor='w')
        label0.place(relx=0.5, rely=0.26, anchor='center')

        self.combo_box1 = CTkComboBox(self.tab1, values=["RF", "DT"])
        self.combo_box1.place(relx=0.5, rely=0.30, anchor='center')

        label1 = CTkLabel(self.tab1, text="Target 1 - 3:", anchor='w')
        label1.place(relx=0.5, rely=0.38, anchor='center')

        self.int_entry1 = CTkEntry(self.tab1)
        self.int_entry1.place(relx=0.5, rely=0.42, anchor='center')

        label2 = CTkLabel(self.tab1, text="Ratio 0 - 1:", anchor='w')
        label2.place(relx=0.5, rely=0.50, anchor='center')

        self.int_entry2 = CTkEntry(self.tab1)
        self.int_entry2.place(relx=0.5, rely=0.54, anchor='center')

        label3 = CTkLabel(self.tab1, text="max:", anchor='w')
        label3.place(relx=0.5, rely=0.62, anchor='center')

        self.int_entry3 = CTkEntry(self.tab1)
        self.int_entry3.place(relx=0.5, rely=0.66, anchor='center')

        self.submit_button1 = CTkButton(self.tab1, text="Submit", command=self.submit)
        self.submit_button1.place(relx=0.5, rely=0.85, anchor='center')

    def setup_tab2(self):
        self.file_label2 = CTkLabel(self.tab2, text="Selected file:", anchor='w')
        self.file_label2.place(relx=0.5, rely=0.14, anchor='center')

        self.open_file_button2 = CTkButton(self.tab2, text="Open File", command=self.open_file)
        self.open_file_button2.place(relx=0.5, rely=0.18, anchor='center')

        label4 = CTkLabel(self.tab2, text="Method", anchor='w')
        label4.place(relx=0.5, rely=0.26, anchor='center')

        self.combo_box2 = CTkComboBox(self.tab2, values=["RF", "DT"])
        self.combo_box2.place(relx=0.5, rely=0.30, anchor='center')

        label5 = CTkLabel(self.tab2, text="Target 1 - 3:", anchor='w')
        label5.place(relx=0.5, rely=0.38, anchor='center')

        self.int_entry4 = CTkEntry(self.tab2)
        self.int_entry4.place(relx=0.5, rely=0.42, anchor='center')

        label6 = CTkLabel(self.tab2, text="Ratio 0 - 1:", anchor='w')
        label6.place(relx=0.5, rely=0.50, anchor='center')

        self.int_entry5 = CTkEntry(self.tab2)
        self.int_entry5.place(relx=0.5, rely=0.54, anchor='center')

        label7 = CTkLabel(self.tab2, text="max:", anchor='w')
        label7.place(relx=0.5, rely=0.62, anchor='center')

        self.int_entry6 = CTkEntry(self.tab2)
        self.int_entry6.place(relx=0.5, rely=0.66, anchor='center')

        self.submit_button2 = CTkButton(self.tab2, text="Submit", command=self.submit)
        self.submit_button2.place(relx=0.5, rely=0.85, anchor='center')

    def open_file(self):
        file_path = filedialog.askopenfilename()
        file_name = os.path.basename(file_path)
        current_tab = self.tab_view.get()
        if current_tab == "Train":
            self.file_label1.configure(text=f"Selected file: {file_name}")
        elif current_tab == "Predict":
            self.file_label2.configure(text=f"Selected file: {file_name}")

    def submit(self):
        current_tab = self.tab_view.get()
        if current_tab == "Train":
            file_label_text = self.file_label1.cget("text")
            target = self.int_entry1.get()
            ratio = self.int_entry2.get()
            max = self.int_entry3.get()
            combo_box_text = self.combo_box1.get()

            if file_label_text.startswith("Selected file: "):
                file_name = file_label_text[len("Selected file: "):]
            else:
                print("No file selected.")
                return
            # Check if all fields are filled
            if not all([target, ratio, max,combo_box_text]):
                print("Please fill all integer fields.")
                return
    
            # Convert values to appropriate types if needed
            try:
                target = int(target)
                ratio = float(ratio)
                max = float(max)
            except ValueError:
                print("Invalid input for integer or float fields.")
                return
    
        elif current_tab == "Predict":
            file_label_text = self.file_label2.cget("text")
            target = self.int_entry4.get()
            ratio = self.int_entry5.get()
            max = self.int_entry6.get()
            combo_box_text = self.combo_box2.get()

            if file_label_text.startswith("Selected file: "):
                file_name = file_label_text[len("Selected file: "):]
            else:
                print("No file selected.")
                return
    
            # Check if all fields are filled
            if not all([target, ratio, max, combo_box_text]):
                print("Please fill all fields.")
                return
    
            # Convert values to appropriate types if needed
            try:
                target = int(target)
                ratio = float(ratio)
                max = float(max)
            except ValueError:
                print("Invalid input for integer or float fields.")
                return
    
        
        print(file_name,current_tab,target,ratio,max,combo_box_text)
        #start(file_name,current_tab,target,ratio,max,combo_box_text)

if __name__ == '__main__':
    App()
