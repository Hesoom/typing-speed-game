import customtkinter
import time
import random

app = customtkinter.CTk()
app.geometry("600x500")
app.title("CTk example")

sentences = [
    "Chase dreams not people",
    "Silence is better than nonsense",
    "Move in silence code like thunder",
    "Stay sharp the world is blurry",
    "Vibes speak louder than words",
    "Hustle in private shine in public",
    "Break rules not keyboards"
]

sample_text = random.choice(sentences)

# --- Switch Function ---
def switch_frame(hide, show):
    hide.pack_forget()
    show.pack(fill="both", expand=True)

# --- Try Again ---
def try_again():
    global start_time, timer, sample_text
    for lbl in word_labels:
        lbl.configure(text_color="white")
    entry.delete(0, 'end')     
    switch_frame(resault_frame, main_frame)
    start_time = None
    timer = True
    main()
    

# --- Main Loop ---

start_time = None
timer = True
def main():
    global start_time, timer, resault_label, sample_words
    content = entry.get()
    typed_words = content.split()
    for i, lbl in enumerate(word_labels):
        if i < len(typed_words):
            if typed_words[i] == sample_words[i]:
                lbl.configure(text_color="green")
    if content.strip():
        if start_time is None:
            start_time = time.time()
    
        if timer and content == sample_text:
            timer = False
            elapsed = time.time() - start_time
            num_chars = len(content)
            words = num_chars / 5
            minutes = elapsed / 60
            wpm = int(words / minutes)
            resault_label.configure(text=f"Score: {wpm} WPM")
            switch_frame(main_frame, resault_frame)
    app.after(100, main)

# --- Main Frame ---
main_frame = customtkinter.CTkFrame(app, width=600, height=500)
main_frame.pack()

typing_frame = customtkinter.CTkFrame(main_frame, width=400, height=250)
typing_frame.place(relx=0.5, rely=0.5, anchor='center')

label_frame = customtkinter.CTkFrame(typing_frame)
label_frame.place(relx=0.5, rely=0.4, anchor='center')

sample_words = sample_text.split()
word_labels = []
for word in sample_words:
    lbl = customtkinter.CTkLabel(label_frame, text=word, font=("Helvetica", 18, 'bold'))
    lbl.pack(side="left", padx=(0, 5))
    word_labels.append(lbl)

entry = customtkinter.CTkEntry(typing_frame, width=300, font=("Helvetica", 14, "bold"))
entry.place(relx=0.5, rely=0.55, anchor="center")

# --- Resault Frame ---
resault_frame = customtkinter.CTkFrame(app, width=600, height=500)

resault_label = customtkinter.CTkLabel(resault_frame, text="Score: 0 Wpm!", font=("Helvetica", 22, "bold"))
resault_label.place(relx=0.5, rely=0.45, anchor='center')

try_again_btn = customtkinter.CTkButton(resault_frame, text="Try Again", command=try_again)
try_again_btn.place(relx=0.5, rely=0.55, anchor='center')


main()

app.mainloop()
