import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# CHANGE THESE VARIABLES BY YOURS
# IN FILE LOCATION, ON WINDOWS, REPLACE \ WITH //
sender_email = os.getenv("EMAIL")
sender_password = os.getenv("PASSWORD")
full_name = "Malek Zaag"
resume_location = "C:\\Users\\mk\\Desktop\\emails-bot-sender\\CV.pdf"
resume_filename = "CV.pdf"
data_location = "C:\\Users\\mk\\Desktop\\emails-bot-sender\\contact cdi.txt"
body_template_with_person_name = "Hello {name},\n\nI am writing to express my enthusiastic interest in joining your company as a software engineering.\n\nAllow me to introduce myself. I am Malek ZAAG, a final year studies intern at Dassault Systemes, I am looking now for a future full time job as Cloud/DevOps Engineer in your company. I attached my resume in this email so you will be able to see if there are some open spots that align with my skills.\n\nYours sincerely,\nMalek ZAAG"
body_template_without_person_name = "Dear {company} recrutement team,\n\nI am writing to express my enthusiastic interest in joining your company as a software engineering.\n\nAllow me to introduce myself. I am Malek ZAAG, a final year studies intern at Dassault Systemes, I am looking now for a future full time job as Cloud/DevOps Engineer in your company. I attached my resume in this email so you will be able to see if there are some open spots that align with my skills.\n\nYours sincerely,\nMalek ZAAG"


def send_email(to_email, body):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = full_name + " " + sender_email
    message['To'] = to_email
    message['Subject'] = "Spontaneous Application - Search for a full time opportunity"

    # Attach the body to the email
    message.attach(MIMEText(body, 'plain'))

    # Attach resume

    with open(resume_location, 'rb') as resume_file:
        resume_part = MIMEApplication(resume_file.read(), Name=resume_filename)
        resume_part['Content-Disposition'] = f'attachment; filename="{resume_filename}"'
        message.attach(resume_part)

    # Attach recommendation letter
    # with open(recommendation_letter_location, 'rb') as resume_file:
    #     resume_part = MIMEApplication(resume_file.read(), Name=recommendation_letter_filename)
    #     resume_part['Content-Disposition'] = f'attachment; filename="{recommendation_letter_filename}"'
    #     message.attach(resume_part)

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())


# Read contact emails from a file
with open(data_location, 'r') as file:
    contacts = file.read().splitlines()

# Iterate through contact emails and send emails
for contact in contacts:
    # Extract the name from the email (you may need to adapt this based on your email format)
    [email, company, name] = contact.split(';')

    # Format the subject and body with the name
    if name == company:
        body = body_template_without_person_name.format(company=company, name=name)
    else:
        body = body_template_with_person_name.format(company=company, name=name)

    # Send the email
    send_email(email, body)
print("Emails sent successfully.")
