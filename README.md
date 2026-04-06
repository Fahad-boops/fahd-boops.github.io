# Python Financial Toolkit

Welcome to my Python Financial Toolkit! I am building these projects to apply what I am learning about programming and information systems to real-world financial tracking. 

This repository holds my progress as a developer, showcasing how I am learning to write cleaner, more resilient code over time.

## Version 1.0.1: The Investment Simulator
**File:** `v1.0.1_Investment_Simulator.py` 

This was my first major script. It is a text-based simulator that allows users to calculate the future value of an investment, figure out how many months it takes to reach a savings goal, and find out the exact monthly contribution needed to get there.

**What I learned:** Core Python math logic, `while` loops, and managing user inputs. 
**The Limitation:** It was a great foundation, but it was fragile. If a user accidentally typed a letter instead of a number, the program would crash. It also did not save any data after the program closed.

## Version 1.0.2: The Budget & Paycheck Dashboard
**File:** `v1.0.2_Budget_Dashboard.py` 

For my next iteration, I built a tool focused on daily budgeting and estimating weekly/monthly paychecks based on tax rates. I took the limitations from v1.0.1 and applied some major software architecture upgrades.

**New Concepts Applied:**
* **Persistent Memory:** I implemented the `json` and `os` libraries so the dashboard automatically saves all income and expenses to a local file. No more data loss on exit!
* **Bulletproof Error Handling:** I wrote custom functions using `while True` loops and `try/except` blocks to handle user inputs. Now, invalid entries simply prompt the user to try again instead of breaking the script.
* **Object-Oriented Programming (OOP):** I built a `Budget` class to cleanly manage transaction states and calculate balances, moving away from unstructured, loose variables.

## 🛠️ How to Run
1. Download the Python file you want to use.
2. Open your terminal or command prompt.
3. Run the script (e.g., `python v1.0.2_Budget_Dashboard.py`).
4. Follow the on-screen menu options to start tracking!
