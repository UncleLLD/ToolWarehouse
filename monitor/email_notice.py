import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, message, to_email):
    # 配置发件人邮箱信息
    from_email = "yourSend@gmail.com"
    password = "yourPassword"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # 创建邮件
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # 添加邮件正文
    msg.attach(MIMEText(message, "plain"))

    # 连接到 SMTP 服务器并发送邮件
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()


# 使用示例
# subject = "重大问题通知"
# message = "应用程序出现重大问题，请立即处理。"
# to_email = "yourReceive@gmail.com
# send_email(subject, message, to_email)
