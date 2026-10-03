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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
