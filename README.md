# 🎮 Number Guessing Game (Dual Mode)

A fun and interactive Python game with two modes:

- **Mode 1 – You guess:** The computer picks a number and you try to guess it.
- **Mode 2 – Computer guesses:** You think of a number and the computer tries to guess it using smart logic (binary search).

---

## 🧠 Features

- 🔀 Choose who should guess: **You** or the **Computer**
- 🧩 Difficulty levels when you guess (easy / medium / hard)
- 📉 Limited attempts in user mode for more challenge
- 📈 Smart algorithm (binary search) when computer guesses
- 🔢 Custom range selection in computer-guess mode
- 🛡️ Input validation for better user experience

---

## 🕹️ How to Play

### 🎮 Mode 1 – You Guess

1. Choose difficulty level:
   - `easy` → 1-10 (5 attempts)
   - `medium` → 1-100 (7 attempts)
   - `hard` → 1-1000 (10 attempts)
2. Try to guess the secret number.
3. You’ll get feedback: Too high / Too low / Correct.

### 🧠 Mode 2 – Computer Guesses

1. You define a number range (e.g. 1 to 1000).
2. Think of a number in that range.
3. The computer will try to guess it.
4. Give feedback: Too high (`h`), too low (`l`), or correct (`c`).

---

## ▶️ How to Run

Make sure you have **Python 3.x** installed.

Save the file as `guess_game.py`, then run it from terminal:

```bash
python guess_game.py
```
