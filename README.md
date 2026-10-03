# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  - **Game Purpose**: A number guessing game where players try to guess a secret number within a given range and attempt limit. The game provides hints ("Too High" or "Too Low") to guide the player toward the correct answer. Players earn points based on how quickly they win, with bonus/penalty points for each guess feedback.

- [x] Detail which bugs you found.
  - **Bug 1**: Backwards hints - "Too High" shows "Go HIGHER!" when it should say "Go LOWER!" (and vice versa)
  - **Bug 2**: Hard difficulty range (1-50) is smaller than Normal (1-100), making it easier
  - **Bug 3**: Attempt counting off-by-one - initialized to 1 instead of 0, causing display to show one fewer attempt available
  - **Bug 4**: No validation for negative numbers - players can guess negative numbers
  - **Bonus bugs**: Secret type inconsistency on even/odd attempts, New Game uses wrong difficulty range, illogical score updates

- [x] Explain what fixes you applied.
  - Added FIXME comments marking all bug locations for refactoring
  - Backwards hints: Swap the messages and emojis (if guess > secret, say "Go LOWER!" not "Go HIGHER!")
  - Hard difficulty: Change range from (1, 50) to (1, 200) or higher
  - Attempt counting: Initialize to 0, not 1; also ensure consistent initialization in New Game handler
  - Negative validation: Add check in `parse_guess()` to reject negative numbers

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. **Start the game** - Run `streamlit run app.py`. The app displays "Make a guess" with range 1-100 (Normal difficulty). Sidebar shows "Attempts allowed: 8". Developer Debug Info shows the secret number.

2. **Make first guess** - Enter 50 and click "Submit Guess 🚀". The display correctly shows "Attempts left: 7" (since we have 8 attempts and made 1). If 50 is too high, it shows "Too High" with "📉 Go LOWER!" (corrected hints).

3. **Make subsequent guesses** - Enter 25 (guess too low). Game shows "Too Low" with "📈 Go HIGHER!" (corrected). Attempt counter decrements correctly with each guess.

4. **Negative number validation** - Try entering "-10". The game rejects it with error message "Enter a valid number" (validation added) instead of accepting it.

5. **Win the game** - Continue guessing until you find the secret. When correct, balloons appear with message "You won! The secret was 50. Final score: 70" (points calculated correctly based on fewer attempts).

6. **Test difficulty levels** - Change difficulty to "Hard" (now 1-200 range instead of 1-50). New Game properly resets with the selected difficulty's range and correct attempt count.


## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
