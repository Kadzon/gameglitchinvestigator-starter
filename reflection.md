# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
-- The debuger info was present on the game screen.
-- I could not press enter to run the game, I had to click on 'submit guess'
-- The hints are misleading

- List at least two concrete bugs you noticed at the start 
-- Hints are misleading and inverted.
-- Does not have a check for negative numbers
-- Inconsistent count for the attempts

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| User enters negative number: "-5" | Error message or rejection; only positive guesses accepted | Accepts "-5" as a valid guess | No validation error |
| Secret=50, User guesses 60 | Show "Too High" with message "Go LOWER" (📉) | Shows "Too High" with message "Go HIGHER!" (📈) | 📈 Go HIGHER! (backwards emoji & message) |
| Select "Hard" difficulty in settings | Range should be larger than Normal (e.g., 1-200) | Range shows as 1-50, which is smaller than Normal (1-100) | Range: 1 to 50 displayed in sidebar |
| Start new game with Normal difficulty (8 attempts allowed) | Display shows "Attempts left: 8" before any guesses | Display shows "Attempts left: 7" before any guesses | Attempts counter initialized to 1 instead of 0 |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude Code Haiku 4.5

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - Illogical score updates for "Too High" vs "Too Low". "Too High" has special behavior for even/odd attempts. "Too Low" always penalizes equally
  - AI suggestion: Why would getting a "Too High" hint on even-numbered attempts reward you with +5 points? That makes no sense—wrong guesses should always penalize you, not sometimes reward you.
  - My verification: This inconsistency creates bizarre game dynamics. Or at least, both should have the same conditional logic (if any). The current code rewards wrong guesses, which breaks game balance.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  - It suggested a change of the inconsistent secret type where the secret could change between str and int. The check_guess() already had a check for this that converted the int a player entered to a str to pass. So not to change the logic of the already written function, I did not change the secret type but did write out a test in pytest to catch any errors.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  1. Traced the code logic
  2. I played the game and watched the behavior (e.g., entering a negative number, checking the hints, testing the attempt counter)

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  With the secret being 50 and guessing 60.
  Expected: "Too High" with message "Go LOWER" (📉)
  Actual: "Too High" with message "Go HIGHER!" (📈)
  This proved the hints are backwards.

- Did AI help you design or understand any tests? How?
  To analyze the test expectations - The AI explained that test_guess_too_high() expected just the outcome string ("Too High"), not a tuple, which revealed another bug
  Trace code execution - AI helped me trace through what happens with the attempt counter (starting at 1 vs 0) to see the off-by-one error
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  A rerun is is when the python script runs top to bottom again creating all the UI elements fresh. A session state is  a special dictionary (st.session_state) that remembers values even after the script reruns. So you can set secret = 50 once and it stays 50 through multiple button clicks and user interactions. Without session state when the user clicks "Submit", script reruns and sets the variable back to a random number and your data is lost.
  In this game, we need session state to:
  - Remember the secret number across multiple guesses
  - Track the number of attempts the player has made
  - Keep the game status (playing, won, or lost)
  Without proper session state management, the secret number would change every time the player submitted a guess—which is exactly the bug this game has! That's why understanding how to initialize session state correctly (if "secret" not in st.session_state:) is so critical.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

  - Understanding the code from the AI's perspective, the logic and functions. Also using Haiku/Sonnet to save on tokens.
- What is one thing you would do differently next time you work with AI on a coding task?
  - Generate a logic flow diagram, something like a systems design to also allow me to make decisions independently without AI and then verify it with AI.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - You don't have to let the AI do everything, it is also possible to do the edits yourself and save some tokens ;)
