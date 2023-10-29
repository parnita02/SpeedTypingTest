import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import random

passage = {
    'English':[
    """The quick brown fox jumps over the lazy dog. This is a longer passage for testing your typing speed.""",
    """Please type this passage as accurately and quickly as you can. Don't worry about making mistakes, just do your best.""",
    """Typing is a valuable skill and practice makes perfect. Keep typing and improve your speed and accuracy."""
],
 'Spanish': [
        """El zorro rápido salta sobre el perro perezoso. Este es un pasaje más largo para probar tu velocidad de escritura.""",
        """Escribe este pasaje con precisión y rapidez. No te preocupes por cometer errores, simplemente haz lo mejor que puedas.""",
        """La escritura es una habilidad valiosa y la práctica la perfecciona. Sigue escribiendo y mejora tu velocidad y precisión."""
    ]
}

current_passage = ""
current_language = "English"

start_time = 0

def start_typing_test():
    global start_time, current_passage
    start_time = time.time()
    current_passage = random.choice(passage[current_language])
    passage_label.config(text=current_passage)
    entry.config(state='normal')
    entry.focus_set()


def end_typing_test():
    global start_time
    end_time = time.time()
    user_input_content = entry.get().strip()
    if not user_input_content:
        messagebox.showerror("Error", "You haven't typed anything yet!")
        return
    elapsed_time = end_time - start_time
    words = current_passage.split()
    wpm = len(words) / (elapsed_time / 60)
    correct_chars = sum([1 for i, j in zip(user_input_content, current_passage) if i == j])
    accuracy = (correct_chars / len(current_passage)) * 100
    result_text = "Time: {:.2f} seconds\nYour typing speed: {:.2f} WPM\nAccuracy: {:.2f}%".format(elapsed_time, wpm, accuracy)
    messagebox.showinfo("Typing Test Result", result_text)
    start_button.config(state='normal')


def refresh_typing_test():
    passage_label.config(text="")
    entry.delete(0, 'end')
    entry.config(state='normal')
    start_button.config(state='active')
    entry.focus()

def change_language(language):
    global current_language
    current_language = language
    refresh_typing_test()  

root = tk.Tk()
root.title("Speed Typing Test")

root.geometry("1600x1000") 

bg_image = Image.open("background1.jpg")  
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)


root.configure(bg="black")
bg_frame = tk.Frame(root)


heading_label = tk.Label(root, text="Speed Typing Test", font=("Times New Roman", 40, "bold"), fg="black", bg='powder blue')
heading_label.pack(pady=50)

language_label = tk.Label(root, text="Select Language:", font=("Times New Roman",18), fg="black")
language_label.pack()
languages = list(passage.keys())
language_var = tk.StringVar()
language_var.set(current_language) 
language_menu = tk.OptionMenu(root, language_var, *languages, command=lambda _: change_language(language_var.get()))
language_menu.config(font=("Times New Roman", 15))
language_menu.pack(pady=10)

passage_label = tk.Label(root, text="", font=("Times New Roman", 17))
passage_label.pack(pady=20)


entry = tk.Entry(root, font=("Times New Roman", 17), state='disabled',width=110, borderwidth=2, relief="solid")
entry.pack(pady=10)


# Create a styled button
style = ttk.Style()
style.configure("BlackBorder.TButton", font=("Times New Roman", 15), bg="#333333", foreground="black", background="black", relief="solid",  bordercolor="black", padding=10, width=15)


style.map("BlackBorder.TButton",
          foreground=[('active', 'blue')],
          background=[('active', 'blue')])


start_button = ttk.Button(root, text="Start Typing Test", command=start_typing_test, style="BlackBorder.TButton")
start_button.pack(pady=10)

end_button = ttk.Button(root, text="End Typing Test", command=end_typing_test, style="BlackBorder.TButton")
end_button.pack(pady=10)

refresh_button = ttk.Button(root, text="Refresh", command=refresh_typing_test, style="BlackBorder.TButton")
refresh_button.pack(pady=10)

root.mainloop()