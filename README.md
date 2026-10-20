# Codveda Python Development Internship

Projects completed during my Python Development internship at Codveda Technologies, organised by level.

**Author:** Ibrahim Hidayat ([@Ibrahim-Hidayat](https://github.com/Ibrahim-Hidayat))

## Repository structure

```
Level 1/   Beginner tasks
Level 2/   Intermediate tasks
Level 3/   Advanced tasks
```

## Level 1

| Task | File | What it does |
|------|------|--------------|
| Simple Calculator | `calculator.py` | Add, subtract, multiply and divide using separate functions, with division-by-zero and invalid-input handling |
| Number Guessing Game | `Number_guessing_game.py` | Guess a random number from 1 to 100 with "too high / too low" hints, a limited number of attempts and a replay option |
| Word Counter | `Word_counter.py` | Reads a text file and counts its words, handling a missing file |

## Level 2

| Task | File | What it does |
|------|------|--------------|
| To-Do List | `To_do.py` | Command-line app to add, view, mark as done and delete tasks, saved in a JSON file |
| Data Scraper | `scraper.py` | Uses `requests` and BeautifulSoup to scrape book titles, prices and availability from books.toscrape.com and saves them to a CSV file |
| API Integration | `weather.py` | Looks up a city and shows its current weather using the free Open-Meteo API, with error handling |

## Level 3

| Task | Files | What it does |
|------|-------|--------------|
| Django Web App with Authentication | `manage.py`, `config/`, `tasks/`, `templates/` | Task manager with registration, login, logout, password reset by email, and two roles (admin sees all tasks, regular users see only their own) |
| File Encryption/Decryption | `file_crypto.py` | Encrypts a text file to a new `.enc` file and decrypts it back using Fernet |
| N-Queens Problem | `n_queens.py` | Solves N-Queens with backtracking on a 2D array board |

## How to run

You need Python 3 installed. Open a terminal in the folder of the task you want to run.

**Level 1 and the N-Queens task** need no extra packages:

```
python calculator.py
```

**Level 2** needs two packages:

```
pip install requests beautifulsoup4
python scraper.py
```

**File encryption** needs one package:

```
pip install cryptography
python file_crypto.py
```

The first time you encrypt a file, a `secret.key` file is created. Keep it safe, because it is needed to decrypt. It is not included in this repository.

**Django web app (Level 3):**

```
cd "Level 3"
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser. Password reset emails are printed in the terminal instead of being sent.

## Skills practised

Python fundamentals, file handling, JSON and CSV, error handling, web scraping, working with APIs, Django authentication, symmetric encryption and backtracking algorithms.

#CodvedaJourney #CodvedaExperience #FutureWithCodveda