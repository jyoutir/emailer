import smtplib 
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

# Entering email and password
my_email='YOUR EMAIL'
password_key='YOUR PASSWORD KEY'


# SMTP Server and port no for GMAIL.com
gmail_server= "smtp.gmail.com"
gmail_port= 587


# Starting connection
my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()
    

# Login with your email and password
my_server.login(my_email, password_key)


# Creation and setting the subject
message = MIMEMultipart("alternative")
message['Subject'] = f"Order confirmation"


# Attatching file (Purchase receipt) to the email 
file_name = "Directory to your file"
from email.mime.application import MIMEApplication

with open(file_name, 'rb') as f:
    file = MIMEApplication(
        f.read(),
        name=os.path.basename(file_name)
    )
    file['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_name)}"'
    message.attach(file)


# Importing the CSV file to personalise emails and setting the email content. 
with open("Client_list.csv") as csv_file:
    clients = csv.reader(csv_file)
    next(clients)  # Skip header row

    for client_name,client_email,address,payment_method,order_number in clients:

        html = f"""
<html>

your content. 

</html>

"""
        
        part2 = MIMEText(html, 'html')   
        message.attach(part2)    

        my_server.sendmail(
            from_addr= my_email,
            to_addrs=client_email,
            msg=message.as_string()
        )



my_server.quit()

print("\033[92mEmails sent successfully.\033[0m")