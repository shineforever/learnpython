#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
邮件处理模块
专门用来处理邮件发送
"""
import threading
import smtplib
from email.mime.text import MIMEText
import queue
import logging
from HomeworkCheck.conf import settings

logger = logging.getLogger(__name__)
my_queue = queue.Queue()


class SendMail(threading.Thread):
    def __init__(self, thread_name, my_queue):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.queue = my_queue
        self.start()

    def run(self):
        while True:
            if self.queue.empty():
                break
            to_list = self.queue.get()
            me = settings.EMAIL["me"]
            msg = MIMEText(content)
            msg['Subject'] = sub
            msg['From'] = me
            msg['To'] = to_list
            try:
                s = smtplib.SMTP()
                s.connect(mail_host)
                s.login(mail_user, mail_pass)
                s.sendmail(me, to_list, msg.as_string())
                s.close()
                logger.info("邮件发送成功:{}".format(to_list))
                self.queue.task_done()
            except Exception as e:
                logger.error(str(e))
                print(str(e))


def send_mail():
    pass
