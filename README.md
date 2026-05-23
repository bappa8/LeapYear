# 🗓️ Leap Year Checker

A simple, beautiful leap year checking tool available as both a **web app** and a **desktop app**. Built with a dark mode design, colorful bold fonts, and smooth animations.

![Dark Mode](https://img.shields.io/badge/Theme-Dark%20Mode-020204?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML-5-e34c26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-3-3a86ff?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-fee440?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-00f5d4?style=for-the-badge)

---

## ✨ Features

- **Dark Mode UI** — Deep dark background (`#020204`) with glassmorphism card design
- **Colorful & Bold Typography** — Poppins font with weights up to 900, animated gradient title
- **Leap Year Detection** — Enter any year and instantly check if it's a leap year
- **Animated Blobs** — Floating background blobs in blue, cyan, and yellow (web version)
- **Confetti Celebration** — Confetti animation when a leap year is detected 🎉 (web version)
- **Next Leap Year Hint** — Shows the next leap year when the entered year is not a leap year
- **Keyboard Support** — Press `Enter` to check
- **Fully Responsive** — Works on mobile, tablet, and desktop (web version)
- **Desktop Executable** — Standalone `.exe` file, no Python installation needed (desktop version)

---

## 📁 Project Structure

```
leap-year-checker/
├── index.html               # Web version — HTML, CSS & JS
├── leap_year_checker.py     # Desktop version — Python Tkinter app
├── dist/
│   └── LeapYearChecker      # Compiled executable (Linux binary)
├── README.md                # You are here
```

---

## 🌐 Web Version

### Quick Start

1. Clone or download this repository
2. Open `index.html` in any modern web browser
3. Enter a year and click **Check Now** (or press `Enter`)

```bash
git clone https://github.com/your-username/leap-year-checker.git
cd leap-year-checker
open index.html        # macOS
xdg-open index.html    # Linux
start index.html       # Windows
```

### Tech Stack

| Technology   | Purpose              |
|--------------|----------------------|
| HTML5        | Page structure       |
| CSS3         | Styling & animations |
| JavaScript   | Leap year logic      |
| Google Fonts | Poppins font family  |

---

## 🖥️ Desktop Version (Python + Tkinter)

### Run from Source

Make sure you have **Python 3.13+** installed, then:

```bash
python leap_year_checker.py
```

> No external Python packages required — uses only the built-in `tkinter` module.

### Build `.exe` (Windows)

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "LeapYearChecker" leap_year_checker.py
```

The executable will be generated at:

```
dist/LeapYearChecker.exe
```

> `--onefile` bundles everything into a single file  
> `--windowed` hides the console window

### Build for Linux / macOS

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "LeapYearChecker" leap_year_checker.py
```

The binary will be at `dist/LeapYearChecker`.

---

## 🎨 Color Palette

| Role           | Color       | Hex       | Preview                                                             |
|----------------|-------------|-----------|---------------------------------------------------------------------|
| Background     | Deep Black  | `#020204` | ![#020204](https://via.placeholder.com/20/020204/020204)            |
| Blue Blob      | Blue        | `#3a86ff` | ![#3a86ff](https://via.placeholder.com/20/3a86ff/3a86ff)            |
| Leap Year      | Green/Cyan  | `#00f5d4` | ![#00f5d4](https://via.placeholder.com/20/00f5d4/00f5d4)            |
| Accent         | Yellow      | `#fee440` | ![#fee440](https://via.placeholder.com/20/fee440/fee440)            |
| Not Leap Year  | Purple      | `#8338ec` | ![#8338ec](https://via.placeholder.com/20/8338ec/8338ec)            |

---

## 🧠 How It Works

The leap year logic follows the standard **Gregorian calendar** rules:

```javascript
function isLeapYear(year) {
  return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}
```

> A year is a **leap year** if:
> - It is divisible by **4** AND **not** divisible by **100**
> - OR it is divisible by **400**

### Examples

| Year | Leap Year? | Result Color |
|------|------------|--------------|
| 2024 | ✅ Yes      | Green (Cyan) |
| 2023 | ❌ No       | Purple       |
| 2000 | ✅ Yes      | Green (Cyan) |
| 1900 | ❌ No       | Purple       |
| 2028 | ✅ Yes      | Green (Cyan) |

---

## 📸 Screenshots

### Web Version (`index.html`)
- Enter a year → Green text = leap year, Purple text = not a leap year
- Animated gradient title, floating blobs, confetti on success

### Desktop Version (`leap_year_checker.py`)
- Same dark theme and color coding in a native desktop window
- Button hover effect (green → yellow)
- Lightweight — no browser needed

---

## 📄 License

© **Bappa Ghosh**. All rights reserved.

---

<p align="center">
  Built with ❤️ by <strong>Bappa Ghosh</strong>
</p>
