# main.py (Backend Email Parser)
import sqlite3
import mailparser

def init_db():
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS emails
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  subject TEXT,
                  sender TEXT,
                  receiver TEXT,
                  body TEXT,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS attachments
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  email_id INTEGER,
                  filename TEXT,
                  content_type TEXT,
                  FOREIGN KEY(email_id) REFERENCES emails(id))''')
    conn.commit()
    conn.close()

def parse_email(file_path):
    mail = mailparser.parse_from_file(file_path)
    
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    
    c.execute('''INSERT INTO emails (subject, sender, receiver, body)
                 VALUES (?, ?, ?, ?)''',
              (mail.subject, mail.from_, mail.to, mail.body))
    
    email_id = c.lastrowid
    
    for attachment in mail.attachments:
        c.execute('''INSERT INTO attachments (email_id, filename, content_type)
                     VALUES (?, ?, ?)''',
                  (email_id, attachment['filename'], attachment['content_type']))
    
    conn.commit()
    conn.close()
    return email_id

def get_parsed_emails():
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    c.execute('''SELECT e.id, e.subject, e.sender, e.receiver, 
                        e.timestamp, COUNT(a.id) as attachments
                 FROM emails e
                 LEFT JOIN attachments a ON e.id = a.email_id
                 GROUP BY e.id''')
    results = c.fetchall()
    conn.close()
    return results
