import smtplib


def email_send_function(to_,subj_,mess_,from_,pass_):
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(from_, pass_)
    msg = "Subject: {}\n\n{}".format(subj_, mess_)
    s.sendmail(from_, to_, mess_)
    x = s.ehlo()
    if x[0] == 250:
        return "s"
    else:
        return "f"

    s.close()





