# Email Parser Application
---
## Overview of this application
---
This Email Parser Application is a Python-based tool designed to parse email files (.eml), extract key information, and store it in a SQLite database. It provides functionality to initialize the database, parse individual emails, and retrieve parsed email data.

## App features
---
- Initialize SQLite database with tables for emails and attachments
- Parse .eml files and extract subject, sender, receiver, body, and attachment information
- Store parsed email data in the SQLite database
- Retrieve parsed email data with attachment count
## Prerequisites
---
Python 3.7 or higher & pip

## Installation
---
### Step 1: Clone the Repository
- clone repo: 
Go to the terminal and past the following code.
```bash
git clone https://github.com/chandibhandari1/EmailParserbot.git
```
- go to the directory
```bash
cd EmailParserbot
```

### Step2 :install virtual environment and activate it
---
Create your own virtual env, if you already have one you can use the existing one by simply activating it. Here myenv1 is the name of your virtual environment

- create a virtual env named: myenv1

```bash 
python -m venv myenv1 
```

- activate virtual env

1 . For MacOS
```bash
source myenv1/bin/activate
```
    
2.  For window
```bash 
myenv1\Scripts\activate
```
(note: if you want to deactivate: type: deactive)

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

## Run
Run the Streamlit app using:
```bash
streamlit run main.py
```
alternatively
```bash
python -m streamlit run main.py
```
## Troubleshooting
. If you encounter a sqlite3.OperationalError, ensure you have write permissions in the directory.
. For ModuleNotFoundError, verify that you've activated the virtual environment and installed all dependencies.
## Future Enhancements
* Add support for multiple email formats (e.g., .msg, .eml)
* Implement email content analysis features
* Create a user interface for easier interaction with the parser



