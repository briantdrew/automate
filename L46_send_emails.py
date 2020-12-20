import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
# need to get google app specific password which i didn't get
conn.login('briantdrew@gmail.com', 'xagagad;gadpgah!')
conn.quit()