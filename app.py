import customtkinter
import time

app = customtkinter.CTk()
app.geometry("600x500")
app.title("CTk example")

sample_text = "This is a sample text"

# --- Main Frame ---
main_frame = customtkinter.CTkFrame(app, width=600, height=500)
main_frame.pack()

typing_frame = customtkinter.CTkFrame(main_frame, width=400, height=250)
typing_frame.place(relx=0.5, rely=0.5, anchor='center')

sentence_label = customtkinter.CTkLabel(typing_frame, text=sample_text, font=("Helvetica", 16, "bold"))
sentence_label.place(relx=0.5, rely=0.4, anchor='center')

entry = customtkinter.CTkEntry(typing_frame, width=200, font=("Helvetica", 14, "bold"))
entry.place(relx=0.5, rely=0.6, anchor='center')

# --- Resault Frame ---
resault_frame = customtkinter.CTkFrame(app, width=600, height=500)

resault_label = customtkinter.CTkLabel(resault_frame, text="Score: 50 Wpm!", font=("Helvetica", 22, "bold"))
resault_label.place(relx=0.5, rely=0.45, anchor='center')

play_again_btn = customtkinter.CTkButton(resault_frame, text="Play Again")
play_again_btn.place(relx=0.5, rely=0.55, anchor='center')


# --- Switch Function ---
def switch_frame(hide, show):
    hide.pack_forget()
    show.pack(fill="both", expand=True)



# --- Main Loop ---
start_time = None
timer = True
counter = 0
def main():
    global start_time, timer, counter, resault_label
    content = entry.get()

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



main()

app.mainloop()
