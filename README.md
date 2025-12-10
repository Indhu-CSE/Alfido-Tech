# Alfido-Tech# Task-1-pythonautomation.py📁 Python Automation Script

This project is a Python-based automation tool that performs file operations such as renaming, sorting, and cleaning.
It uses Python’s OS module, exception handling, and logging for safe automation.
The user interacts with the script through terminal-based inputs.


---

🚀 Features

Automatically rename multiple files

Sort files into folders based on file type

Delete empty files and folders

Uses OS module + logging + exception handling

Generates a log file for every operation

User input supported



---

🛠️ Technologies Used

Python 3

OS Module

Logging Module

Exception Handling


 How to Run

1. Install Python


2. Download the project


3. Open Command Prompt or Terminal


4. Run:



python automation.py

5. Choose your operation from the menu




---

📥 User Input Options
# Task-2-pythonAPI Integration Project (Weather / Crypto / News)

This project fetches real-time data from public APIs using Python’s requests module.
Users can search or filter the results and view clean, formatted output on the terminal.


---

🔥 Features

Fetch Weather / Crypto / News data

Uses Requests module

JSON response parsing

Search / Filter option

Error handling added

Clean output format


🧪 Requirements

Install required modules:

pip install requests

(If you create requirements.txt, add)

requests


---

🚀 How to Run

python main.py


---

🛠️ How It Works

1. User selects:

Weather

Crypto

News



2. Script sends request to the selected API


3. Parses JSON data


4. Prints neat formatted output


5. Optionally filter/search (e.g., city name, crypto name, news keyword)




---

🔍 Sample Output

✔ Weather Example

Enter city: Chennai
Temperature: 30°C
Condition: Clear
Humidity: 70%

✔ Crypto Example

Enter crypto name: bitcoin
Current Price: $41,200
Market Cap: $820B

✔ News Example

Keyword: technology
1. AI startup raises $20M…
2. New smartphone launched…
# Task-3-python

📁 Sales Data Automation Script

A simple Python automation script that reads a CSV file containing product sales data and generates useful outputs like total amount, product-wise summary, month-wise summary, and more.


---

📌 Project Overview

This project automates the processing of a CSV file with sales information.
It reads the file, performs calculations, handles errors safely, and displays the output clearly.

Your Sample CSV File (sales.csv):

Date,Product,Quantity,UnitPrice,Amount
2025-01-05,Soap,10,20,200
2025-01-10,Shampoo,5,100,500
2025-02-03,Soap,8,20,160
2025-03-01,Toothpaste,6,50,300
2025-01-15,Shampoo,4,100,400


---

🚀 Features

Reads sales data from a CSV file

Calculates:

✔ Total Sales Amount

✔ Product-wise totals

✔ Month-wise totals


Handles missing files and wrong inputs (Exception Handling)

Clean and readable output

Easy to modify and extend


How to Run

1. Open IDLE / VS Code / PyCharm


2. Create a file named sales.csv


3. Copy your CSV content into it


4. Create a Python file script.py


5. Run:



python script.py


---

📝 Sample Output

Total Sales: 1560
Product-wise Sales:
  Soap → 360
  Shampoo → 900
  Toothpaste → 300

Month-wise Sales:
  2025-01 → 1100
  2025-02 → 160
  2025-03 → 300


---

🛠 Requirements

Python 3+

csv module (built-in)

Your CSV file (sales.csv)






