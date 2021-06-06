import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

addresser = '1194542196@qq.com'
passwd = 'ntubhyqxsohjjcij'
addressee = '1583966335@qq.com'

msg = MIMEText('你好', _charset='utf8')
msg['Form'] = formataddr(['古生', addresser])
msg['To'] = formataddr(['古生', addressee])
msg['subject'] = '哈哈哈'

server = smtplib.SMTP_SSL('smtp.qq.com', 465)
server.login(addresser, passwd)

server.sendmail(addresser, addressee, msg.as_string())
server.quit()
