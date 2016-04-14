#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
向指定主机的使用者发送提醒关机的邮件
"""

import smtplib
import logging
from email.mime.text import MIMEText

logger = logging.getLogger(__name__)

HOST = "smtp.exmail.qq.com"  # 定义smtp主机
SUBJECT = "关机提醒"  # 主题
FROM = ""  # 定义发件人
FROMPASSWORD = ""
# 关机提醒邮件模板
SHUTDOWN_TEMPLATE = """
		<table width="800" border="0" cellspacing="0" cellpadding="4">
			<tr>
				<td bgcolor="#00BFFF" height="20" style="font-size:18px">*AIT-周末关机提醒*</td>
			</tr>
			<tr>
				<td bgcolor="#66CCFF" height="100" style="font-size: 14px">
					您好：<br>
						<br>
						&nbsp;&nbsp;&nbsp;&nbsp;下列服务器:<br><font color=red> {:50} </font> 还在运行中，请注意下班关机。<br>
						&nbsp;&nbsp;&nbsp;&nbsp;如需周末开机，请前往<a href="http://ur.ait.cn"> UR平台 >></a>填写周末开机申请。<br>
						&nbsp;&nbsp;&nbsp;&nbsp;如有疑问，请与系统组联系。谢谢合作。<br>
						<br>
						<br>
						本邮件为系统自动发送，请勿回复！<br>
				</td>
			</tr>
		</table>
		"""


def send_mail(ip_list, email_to, template=SHUTDOWN_TEMPLATE):
	email_body = template.format("".join(ip_list))

	to = "{}@ait.cn".format(email_to)

	msg = MIMEText(email_body, "html", "utf-8")
	msg["Subject"] = SUBJECT
	msg["From"] = FROM
	msg["To"] = to
	try:
		server = smtplib.SMTP()  # 创建一个SMTP()对象
		server.connect(HOST, "25")  # 连接smtp主机
		server.login(FROM, FROMPASSWORD)
		server.sendmail(FROM, to, msg.as_string())
		server.quit()
	except Exception as e:
		logger.warning("发送失败：{}".format(e))
