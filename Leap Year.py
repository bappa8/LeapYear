import customtkinter as ctk

# Appearance settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# App window
app = ctk.CTk()
app.title("Leap Year Checker (Bappa)")
app.geometry("420x320")
app.resizable(False, False)

# Function
def check_leap_year():
    year = entry.get().strip()

    if not year.isdigit():
        result_label.configure(text="⚠️ Enter a valid number", text_color="#ff6b6b")
        return

    year = int(year)

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        animate_result(f"✅ {year} is a Leap Year", "#2ecc71")
    else:
        animate_result(f"❌ {year} is NOT a Leap Year", "#e74c3c")


# Simple animation (fade effect)
def animate_result(text, color):
    result_label.configure(text="")
    
    def fade(i=0):
        if i <= len(text):
            result_label.configure(text=text[:i], text_color=color)
            app.after(25, fade, i + 1)

    fade()


# Title
title = ctk.CTkLabel(
    app,
    text="Leap Year Checker",
    font=ctk.CTkFont(size=24, weight="bold")
)
title.pack(pady=(25, 10))

# Subtitle
subtitle = ctk.CTkLabel(
    app,
    text="Enter a year to check",
    font=ctk.CTkFont(size=13),
    text_color="gray"
)
subtitle.pack(pady=(0, 15))

# Entry
entry = ctk.CTkEntry(
    app,
    width=220,
    height=40,
    corner_radius=12,
    font=ctk.CTkFont(size=14),
    justify="center"
)
entry.pack(pady=10)

# Button
button = ctk.CTkButton(
    app,
    text="Check Year",
    width=180,
    height=40,
    corner_radius=20,
    font=ctk.CTkFont(size=14, weight="bold"),
    command=check_leap_year
)
button.pack(pady=15)

# Result
result_label = ctk.CTkLabel(
    app,
    text="",
    font=ctk.CTkFont(size=16, weight="bold")
)
result_label.pack(pady=20)

# Enter key support
app.bind("<Return>", lambda event: check_leap_year())

# Run
app.mainloop()
