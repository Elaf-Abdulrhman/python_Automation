import smtplib

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    with open('password.txt', 'r') as x:
        password = x.read()
    server.login('elafabdualrhman00@gmail.com', password)

    subject = "Good morning from elaf"
    with open('body.txt', 'r') as n:
        body = n.read()

    msg = f"subject:{subject} \n\n\n {body}"
    server.sendmail(
        'elafabdualrhman00@gmail.com',
        'ela45f@gmail.com',
        msg
        )
    print('Sent Successfully')

if __name__ == "__main__":
    send_mail()
