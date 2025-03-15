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
``` bash
git clone https://github.com/chandibhandari1/EmailParserbot.git
cd EmailParserbot
```

Step1 :install virtual env
---
(python -m venv myenv1 (name of your venv))

step 2: activate virtual env

if in MacOS
(source myenv1/bin/activate)
if in window
(myenv1\Scripts\activate)
(note: if you want to deactivate: type: deactive)


