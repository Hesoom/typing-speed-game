import customtkinter
import time
import random

# GUI setup
app = customtkinter.CTk()
app.geometry("600x500")
app.title("Typing Speed")

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

start_time = None
timer = True

# --- FUNCTIONS ---

def switch_frame(hide, show):
    hide.pack_forget()
    show.pack(fill="both", expand=True)

def try_again():
    global start_time, timer, sample_text,word_labels
    # Reset word colors, entry field, and timer variables
    for lbl in word_labels:
        lbl.configure(text_color="white")
    entry.delete(0, 'end')     
    start_time = None
    timer = True

    change_sentence()
    switch_frame(result_frame, main_frame)

def change_sentence():
    global word_labels,sample_words,sample_text,sentences
    # Delete previous sentence labels
    for lbl in word_labels:
        lbl.destroy()
    sample_text = random.choice(sentences)
    sample_words = sample_text.split()
    word_labels = []
    # Separate words into individual labels for color feedback
    for word in sample_words:
        lbl = customtkinter.CTkLabel(label_frame, text=word, font=("Helvetica", 18, 'bold'))
        lbl.pack(side="left", padx=(0, 5))
        word_labels.append(lbl)
    
def main():
    global start_time, timer, result_label, sample_words
    content = entry.get()
    typed_words = content.split()
    
    for i, lbl in enumerate(word_labels):
        # Check each typed word against the sample words
        if i < len(typed_words) and i < len(sample_words):
            if typed_words[i] == sample_words[i]:
                lbl.configure(text_color="green")
            else:
                lbl.configure(text_color="white") 

    if content.strip():
        if start_time is None:
            start_time = time.time()
        if timer and content == sample_text:
            timer = False
            # Calculate the WPM
            elapsed = time.time() - start_time
            num_chars = len(content)
            words = num_chars / 5
            minutes = elapsed / 60
            wpm = int(words / minutes)
            result_label.configure(text=f"Score: {wpm} WPM")
            switch_frame(main_frame, result_frame)
    app.after(100, main)

def on_enter_press(event):
    if result_frame.winfo_ismapped():
        try_again()


# --- GUI ---

main_frame = customtkinter.CTkFrame(app, width=600, height=500)
main_frame.pack()

typing_frame = customtkinter.CTkFrame(main_frame, width=400, height=250)
typing_frame.place(relx=0.5, rely=0.5, anchor='center')

label_frame = customtkinter.CTkFrame(typing_frame)
label_frame.place(relx=0.5, rely=0.4, anchor='center')

#Sentence labels
word_labels = []
sample_words = []
change_sentence()


entry = customtkinter.CTkEntry(typing_frame, width=300, font=("Helvetica", 14, "bold"))
entry.place(relx=0.5, rely=0.55, anchor="center")

result_frame = customtkinter.CTkFrame(app, width=600, height=500)

result_label = customtkinter.CTkLabel(result_frame, text="Score: 0 Wpm!", font=("Helvetica", 22, "bold"))
result_label.place(relx=0.5, rely=0.45, anchor='center')

try_again_btn = customtkinter.CTkButton(result_frame, text="Try Again", command=try_again)
try_again_btn.place(relx=0.5, rely=0.55, anchor='center')

# Try again on Enter
app.bind("<Return>", on_enter_press)

main()

app.mainloop()
