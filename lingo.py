import random
import tkinter as tk
from tkinter import messagebox

# Load words from CSV with normalization
words_list = [
    "انار", "آب", "دوست", "کتاب", "خورشيد", "گل", "ماشين", "خانه", "سفر", "ياد",
    "درخت", "شجاعت", "آسمان", "سلام", "نقره", "برف", "دريا", "پروانه", "خوراکي", "قلم",
    "سيب", "عشق", "موز", "زنبور", "فرشته", "پرنده", "شهر", "مدرسه", "دانشگاه", "خواب",
    "چراغ", "فنجان", "باد", "ستاره", "زمين", "کتابخانه", "هواپيما", "قهوه", "شير", "دستگاه",
    "يخ", "دوچرخه", "عيد", "لباس", "شيريني", "سبز", "شادي", "کوه", "درياچه", "آبشار",
    "خانه", "سايه", "ميز", "دست", "پنجره", "ورزش", "ساينا", "صدا", "غذا", "طبيعت",
    "شطرنج", "کاميون", "دستکش", "موزيک", "صندلي", "درختچه", "درب", "لبخند", "گلابي", "چاي",
    "تابستان", "پايز", "بهار", "زمستان", "سفره", "آبجو", "حيوان", "کاسه", "کفش", "چشمه",
    "کف", "کنسرت", "ورزشگاه", "توفان", "کيک", "درياچه", "شاتل", "موزه", "کارد", "فيل",
    "آرام", "ابري", "گلخانه", "يخچال", "حيوانات", "تاريک", "پالتو", "آينه", "اسکيت", "دوستدار",
    "چادر", "همه", "دوست", "چاي", "رنگ", "در", "پنکه", "دست", "مقدس", "آبمعدني", "درختان",
    "نکته", "کوسه", "سوسک", "سياره", "پرچم", "سورتمه", "کره", "درختان", "فصل", "گلاب",
    "لبخند", "مجله", "بازي", "کتابخواني", "ايران", "پارک", "کارت", "حافظ", "بيمارستان", "پسر",
    "کاشي", "صحراء", "دشمن", "سالن", "فراش", "آوردن", "پيشنهاد", "زيبا", "گلابي", "کيسه",
    "نوشته", "تفسير", "سينما", "پرچم", "زندگي", "ستاره‌شناسي", "بنياد", "هديه", "رياضيات", "سرمايه",
    "دستور", "صفحه", "کتابخانه", "تاريخ", "فرياد", "ساعت", "رودخانه", "حکايت", "اتاق", "برنده",
    "غروب", "شفق", "چمن", "آبشار", "ادبيات", "غذاهاي", "افسانه", "صابون", "قهرمان", "مصلحت",
    "آتش", "برف", "چراغ", "حفاظت", "گلاب", "خاطره", "تولد", "پزشکي", "فرهنگ", "کشاورزي",
    "مغز", "کيک", "چراغ", "کوهستان", "چراغ", "دسته", "آشپزخانه", "شرکت", "کارد", "بانک",
    "آداب", "سنگ", "حياط", "مرد", "ساکت", "کتاب", "خاطره", "سفر", "محافظ", "موسيقي",
    "زندگي", "جنگل", "دريا", "موزه", "سفر", "ماه", "خورشيد", "ستاره", "حريم", "جهان",
    "برگ", "چشمه", "خواب", "صفحه", "سقوط", "کوه", "درخت", "ميدان", "درختان", "دستگاه",
    "دوربين", "ميز", "هوشمند", "مغازه", "چراغ", "ادبيات", "شهرستان", "ساده", "خريدار", "مهمان",
    "کارت", "تلفن", "شماره", "صندلي", "حيوانات", "موجودات", "آواي", "ويلا", "پاسخ", "پرچم",
    "رنگارنگ", "سياه", "سفيد", "خاکي", "آبي", "طلا", "نقره", "سفيد", "مدرن", "سفرهاي",
    "نمک", "گوشت", "پيش‌بيني", "تکامل", "زنبور", "شکوفه", "جنگ", "رودخانه", "خانه", "کودک",
    "پدر", "مادر", "پسر", "دختر", "همه", "خانواده", "سلامت", "خوشمزه", "شيريني", "دوستي",
    "بازي", "پوشش", "آشپزي", "غذا", "آداب", "فرياد", "گفتار", "حس", "هنر", "سورتمه",
    "راهپيماي", "امتحان", "کتابخانه", "درخت", "نقد", "دانش", "مقاله", "دولت", "شهرداري", "کتابي",
    "آثار", "کامپيوتر", "سخت", "راه", "پوشش", "نيک", "نهال", "ساخت", "نياز", "آبادي",
    "طبيعت", "نبرد", "يادداشت", "گواهي", "استعداد", "جمع‌آوري", "طراحي", "مدير", "مراجعه", "بررسي",
    "کاشي", "سکوت", "آرامش", "تجزيه", "خوشبو", "تفريح", "سينما", "مطالعه", "حساب", "رياضي",
    "موسيقي", "دوره", "آگاه", "ارزش", "هوش", "کتابخانه", "آزادي", "فضا", "رودخانه", "صحنه",
    "پست", "موسيقي", "کتابخوان", "لباس", "چاي", "خوردن", "موزيک", "آرايش", "تصوير", "کاغذ",
    "ظرف", "پيشرفت", "شعر", "آبجو", "هوشمند", "گلاب", "پايز", "آسيا", "يادگيري", "کنسرت",
    "ساعت", "کامياب", "رنگارنگ", "مرکز", "چراغ"
]

class WordGuessGame:
    def __init__(self, master):
        self.master = master
        self.master.title("بازی حدس کلمه")

        # Set the window size to 1920x1080
        self.master.geometry("1920x1080")
        # Optional: Disable window resizing
        # self.master.resizable(False, False)
        # Optional: Set window to fullscreen
        # self.master.attributes('-fullscreen', True)

        self.words_list = words_list[:]  # Make a copy to modify
        self.current_word = ""

        self.attempts = 5
        self.word_length = 0
        self.current_row = 0

        # Timer variables
        self.time_left = 10
        self.guess_made = False
        self.timer_job = None  # To keep track of the scheduled timer callback

        # Frames
        self.board_frame = tk.Frame(self.master, padx=10, pady=10)
        self.board_frame.pack()

        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack(pady=20)  # Increased padding for better spacing

        # Entry and submit button
        self.guess_entry = tk.Entry(self.input_frame, font=("Helvetica", 24), justify='center')  # Changed justify to center
        self.guess_entry.pack(side=tk.LEFT, padx=10, pady=10)  # Increased padding
        self.guess_entry.bind("<Return>", self.submit_guess)

        self.submit_btn = tk.Button(self.input_frame, text="تایید", font=("Helvetica", 18), command=self.submit_guess)  # Increased font size
        self.submit_btn.pack(side=tk.LEFT, padx=10, pady=10)  # Increased padding

        # Status and informational labels
        self.status_label = tk.Label(self.master, text="", font=("Helvetica", 18))  # Increased font size
        self.status_label.pack(pady=10)

        self.correct_word_label = tk.Label(self.master, text="", font=("Helvetica", 20), fg="red")  # Increased font size
        self.correct_word_label.pack(pady=10)

        # Timer label
        self.timer_label = tk.Label(self.master, text="", font=("Helvetica", 20), fg="blue")  # Increased font size
        self.timer_label.pack(pady=10)

        self.rows = []

        self.start_new_game()

    def start_new_game(self):
        # Cancel any existing timer to prevent multiple timers
        if self.timer_job is not None:
            self.master.after_cancel(self.timer_job)
            self.timer_job = None

        # Clear previous board and related variables
        for row in self.rows:
            for cell in row:
                cell.destroy()
        self.rows.clear()
        self.current_row = 0

        # Check if we have words left
        if not self.words_list:
            messagebox.showinfo("پایان بازی", "تمام کلمات استفاده شده‌اند. بازی تمام شد.")
            self.master.destroy()
            return

        self.current_word = random.choice(self.words_list)
        self.words_list.remove(self.current_word)  # Remove the chosen word from the list

        self.word_length = len(self.current_word)

        self.correct_word_label.config(text="")

        # Create board (5 rows)
        for i in range(self.attempts):
            row_cells = []
            for j in range(self.word_length):
                label = tk.Label(
                    self.board_frame,
                    text="",
                    font=("Helvetica", 24),        # Increased font size for better visibility
                    width=4,                        # Adjusted width
                    height=2,                       # Adjusted height
                    bd=2,                           # Increased border width for distinction
                    relief="solid",
                    bg="lightgray",
                    anchor='center',                # Changed from 'e' to 'center' to center the text
                    justify='center'                # Ensures multi-line text (if any) is centered
                )
                label.grid(row=i, column=j, padx=10, pady=10)  # Increased padding for spacing
                row_cells.append(label)
            self.rows.append(row_cells)

        # Show the first letter of the word in green in the rightmost cell of each row
        for i in range(self.attempts):
            first_block = self.rows[i][self.word_length - 1]
            first_block.config(text=self.current_word[0].upper(), bg="green", fg="white")

        self.guess_entry.config(state='normal')
        self.submit_btn.config(state='normal')
        self.guess_entry.delete(0, tk.END)
        self.status_label.config(text=f"شما {self.attempts} فرصت دارید. حدس خود را وارد کنید:")

        # Reset and start the timer for this guess
        self.time_left = 10
        self.guess_made = False
        self.update_timer()

    def update_timer(self):
        if self.guess_made:
            # User has guessed before time ran out, do nothing
            return
        if self.time_left > 0:
            self.timer_label.config(text=f"زمان باقی‌مانده: {self.time_left} ثانیه")
            self.time_left -= 1
            # Schedule the next timer update and keep track of the job
            self.timer_job = self.master.after(1000, self.update_timer)
        else:
            # Time is up
            self.time_up()

    def time_up(self):
        # User didn't guess in time
        self.correct_word_label.config(text=f"وقت تمام شد! کلمه درست: {self.current_word.upper()}")
        self.guess_entry.config(state='disabled')
        self.submit_btn.config(state='disabled')
        # Cancel any existing timer
        if self.timer_job is not None:
            self.master.after_cancel(self.timer_job)
            self.timer_job = None
        # After 5 seconds, go to next word
        self.master.after(5000, self.enable_and_new_word)

    def enable_and_new_word(self):
        # Start a new game after showing correct word for 5 seconds
        self.start_new_game()

    def submit_guess(self, event=None):
        guess = self.guess_entry.get().strip().lower()
        if len(guess) != self.word_length:
            messagebox.showerror("خطا", f"حدس شما باید {self.word_length} حرف باشد.")
            return

        # Optionally, validate the guessed word against a dictionary here

        # The user made a guess before time ran out
        self.guess_made = True

        # Cancel the timer since the user has made a guess
        if self.timer_job is not None:
            self.master.after_cancel(self.timer_job)
            self.timer_job = None

        self.check_guess(guess)

    def check_guess(self, guess):
        display = ["_"] * self.word_length
        letter_count = {}

        for letter in self.current_word:
            letter_count[letter] = letter_count.get(letter, 0) + 1

        # First pass for correct (green)
        for i in range(self.word_length):
            if guess[i] == self.current_word[i]:
                display[i] = "G"
                letter_count[guess[i]] -= 1

        # Second pass for present (yellow)
        for i in range(self.word_length):
            if display[i] == "_":
                if guess[i] in letter_count and letter_count[guess[i]] > 0:
                    display[i] = "Y"
                    letter_count[guess[i]] -= 1
                else:
                    display[i] = "X"  # Not in word

        # Update the board
        for i in range(self.word_length):
            cell = self.rows[self.current_row][self.word_length - i - 1]

            # If it's the first letter cell (i == 0), keep it as is (the correct first letter in green)
            if i == 0:
                cell.config(text=self.current_word[0].upper(), bg="green", fg="white")
            else:
                cell.config(text=guess[i].upper())
                if display[i] == "G":
                    cell.config(bg="green", fg="white")
                elif display[i] == "Y":
                    cell.config(bg="yellow", fg="black")
                else:
                    cell.config(bg="gray", fg="white")

        # Check if user guessed correctly
        if all(d == "G" for d in display):
            messagebox.showinfo("تبریک", "شما کلمه را حدس زدید!")
            # Move on to the next word automatically
            self.start_new_game()
        else:
            # Move to next row if attempts left
            self.current_row += 1
            if self.current_row >= self.attempts:
                # Show correct word and wait 5 seconds
                self.correct_word_label.config(
                    text=f"متاسفانه تمام فرصت‌ها تمام شد. کلمه درست: {self.current_word.upper()}")
                self.guess_entry.config(state='disabled')
                self.submit_btn.config(state='disabled')
                # Cancel any existing timer
                if self.timer_job is not None:
                    self.master.after_cancel(self.timer_job)
                    self.timer_job = None
                self.master.after(5000, self.enable_and_new_word)
            else:
                # Another attempt: reset guess entry and timer
                self.guess_entry.delete(0, tk.END)
                remaining = self.attempts - self.current_row
                self.status_label.config(
                    text=f"دوباره امتحان کنید. شما {remaining} فرصت دیگر دارید.")

                # Reset timer and guess_made for the next attempt
                self.time_left = 10
                self.guess_made = False
                self.update_timer()

def main():
    root = tk.Tk()
    game = WordGuessGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
