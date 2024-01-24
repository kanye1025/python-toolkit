import os.path
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header, make_header
from email.utils import formataddr
import email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage



class EmailSender:
    def __init__(self,mail_host  , mail_port ,mail_user  ,mail_pass , ):
        self.mail_host = mail_host
        self.nail_port = mail_port
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.mail_port = mail_port

    def send(self, to,title='',text='',cc = [],bcc = [],files = [],replyto =''):
        # 设置email信息
        # 邮件内容设置
        to = ','.join(to)  # 收件人
        cc = ','.join(cc)  # 抄送
        bcc = ','.join(bcc)  # 密送
        rcptto = [to, cc, bcc]  # 完整的收件对象



        message = MIMEMultipart('alternative')

        #part['From'] = formataddr([sender_name,sender])
        message['From'] =  Header(self.mail_user, 'utf-8')
        message['Reply-to'] =  Header(replyto,'utf-8')
        message['TO'] = Header(to,'utf-8')
        message['Cc'] =  Header(cc,'utf-8')
        message['Bcc'] = Header(bcc,'utf-8')
        message['Message-id'] = email.utils.make_msgid()
        message['Date'] = email.utils.formatdate()
        message['Subject'] = Header(title, 'utf-8')
        message.attach(MIMEText(text, 'plain', 'utf-8'))

        for file_path in files:
            with open(file_path, 'rb') as f:
                content = f.read()
                part = MIMEText(content, 'base64', 'utf-8')
                _,file_name = os.path.split(file_path)
                part['Content-Type'] = 'application/octet-stream'
                part.add_header("Content-Disposition", "attachment",filename=file_name)
                message.attach(part)
        try:
            client = smtplib.SMTP_SSL(self.mail_host, self.mail_port)
            #client.ehlo()
            #client.starttls()
            print('smtp_ssl----连接服务器成功，现在开始检查帐号密码')

        except Exception as e2:
            print('连接服务超时')
            return False
        try:
            client.login(self.mail_user,self.mail_pass)
            print('帐密验证成功')
        except:
            print('抱歉，帐密验证失败')
            return False

        '''~~~发送邮件并结束任务~~~'''
        send_to = (','.join(rcptto)).split(',')
        msg = message.as_string()
        client.sendmail(self.mail_user,send_to , message.as_string())
        client.quit()
        return True


if __name__ == "__main__":

    sender = EmailSender("smtp.qiye.aliyun.com",465,"bi@bybon.cn","aNSZR7EmH9qjhY0")
    sender.send(to=['ye.kan@bybon.cn'],title='test',text='test')
