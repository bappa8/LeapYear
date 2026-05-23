import tkinter as tk
from tkinter import ttk


class LeapYearChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Leap Year Checker")
        self.root.geometry("500x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#020204")

        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.root.winfo_screenheight() // 2) - (520 // 2)
        self.root.geometry(f"500x520+{x}+{y}")

        # ── Colors ──
        self.BG = "#020204"
        self.CARD_BG = "#0a0a12"
        self.GREEN = "#00f5d4"
        self.PURPLE = "#8338ec"
        self.YELLOW = "#fee440"
        self.BLUE = "#3a86ff"
        self.WHITE = "#ffffff"
        self.DIM_WHITE = "#808080"

        self._build_ui()

    def _build_ui(self):
        # ── Title ──
        title_frame = tk.Frame(self.root, bg=self.BG)
        title_frame.pack(pady=(35, 0))

        title = tk.Label(
            title_frame,
            text="Leap Year Checker",
            font=("Poppins", 28, "bold"),
            fg=self.BLUE,
            bg=self.BG,
        )
        title.pack()

        # ── Subtitle ──
        subtitle = tk.Label(
            self.root,
            text="Enter a year to find out if it's a leap year",
            font=("Poppins", 10),
            fg=self.DIM_WHITE,
            bg=self.BG,
        )
        subtitle.pack(pady=(5, 30))

        # ── Input Frame ──
        input_frame = tk.Frame(self.root, bg=self.BG)
        input_frame.pack()

        self.year_var = tk.StringVar()

        self.entry = tk.Entry(
            input_frame,
            textvariable=self.year_var,
            font=("Poppins", 20, "bold"),
            fg=self.WHITE,
            bg="#0d0d1a",
            insertbackground=self.WHITE,
            relief="flat",
            justify="center",
            width=16,
            highlightthickness=2,
            highlightcolor=self.GREEN,
            highlightbackground="#1a1a2e",
        )
        self.entry.pack(ipady=10, padx=40, fill="x")
        self.entry.focus()

        # ── Button ──
        self.check_btn = tk.Button(
            self.root,
            text="✔  CHECK NOW",
            font=("Poppins", 14, "bold"),
            fg=self.BG,
            bg=self.GREEN,
            activebackground=self.YELLOW,
            activeforeground=self.BG,
            relief="flat",
            cursor="hand2",
            command=self.check_leap_year,
        )
        self.check_btn.pack(pady=(25, 0), ipady=10, padx=40, fill="x")

        # Hover effects
        self.check_btn.bind("<Enter>", lambda e: self.check_btn.configure(bg=self.YELLOW))
        self.check_btn.bind("<Leave>", lambda e: self.check_btn.configure(bg=self.GREEN))

        # ── Result Frame ──
        self.result_frame = tk.Frame(self.root, bg=self.BG)
        self.result_frame.pack(pady=(30, 0))

        self.icon_label = tk.Label(
            self.result_frame, text="", font=("Segoe UI Emoji", 36), bg=self.BG
        )
        self.icon_label.pack()

        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=("Poppins", 16, "bold"),
            bg=self.BG,
            wraplength=420,
        )
        self.result_label.pack(pady=(5, 0))

        self.detail_label = tk.Label(
            self.result_frame,
            text="",
            font=("Poppins", 10),
            fg=self.DIM_WHITE,
            bg=self.BG,
        )
        self.detail_label.pack(pady=(5, 0))

        # ── Footer ──
        footer = tk.Label(
            self.root,
            text="© Bappa Ghosh. All rights reserved.",
            font=("Poppins", 8),
            fg="#333333",
            bg=self.BG,
        )
        footer.pack(side="bottom", pady=15)

        # ── Enter key binding ──
        self.root.bind("<Return>", lambda e: self.check_leap_year())

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def find_next_leap(self, year):
        y = year + 1
        while not self.is_leap_year(y):
            y += 1
        return y

    def check_leap_year(self):
        val = self.year_var.get().strip()

        if not val:
            self._clear_result()
            return

        try:
            year = int(val)
        except ValueError:
            self._clear_result()
            return

        if year < 1:
            self._clear_result()
            return

        if self.is_leap_year(year):
            self.icon_label.configure(text="🎉")
            self.result_label.configure(
                text=f"{year} is a Leap Year! 🗓️",
                fg=self.GREEN,
            )
            self.detail_label.configure(text="February has 29 days this year!")
        else:
            self.icon_label.configure(text="✖️")
            self.result_label.configure(
                text=f"{year} is not a Leap Year",
                fg=self.PURPLE,
            )
            next_leap = self.find_next_leap(year)
            self.detail_label.configure(text=f"Next leap year: {next_leap}")

    def _clear_result(self):
        self.icon_label.configure(text="")
        self.result_label.configure(text="")
        self.detail_label.configure(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = LeapYearChecker(root)
    root.mainloop()
