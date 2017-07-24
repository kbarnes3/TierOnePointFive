from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class EmailHelper:
    def __init__(self, config):
        self._config = config

    def _send_email(self, tick_list):
        email_config = self._config.email_settings

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['From'] = email_config.from_name
        msg['To'] = email_config.to_names
        msg['Subject'] = '[Tier 1.5] Network Event Report'

        self._prepare_email_body(msg, tick_list)

        # Send the message via local SMTP server.
        s = smtplib.SMTP_SSL(email_config.server_address, email_config.server_port)
        s.login(email_config.login, email_config.password)
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        s.sendmail(email_config.from_name, email_config.to_names, msg.as_string())
        s.quit()

    def _prepare_email_body(self, msg, tick_list):
        opening = "Tier 1.5 detected a network event. The details and actions performed are below."

        text = '{0}\n\n'.format(opening)

        html = """\
<html>
    <head></head>
    <body>
        <p>{0}</p>
        <ul>
""".format(opening)

        reverse_tick_list = tick_list[:]
        reverse_tick_list.reverse()
        for tick in reverse_tick_list:
            text += "    {0}\n".format(str(tick))
            html += "            <li>{0}</li>\n".format(str(tick))

        text += "Sincerely,\n-Tier 1.5"
        html += """\
        </ul>
        <p>Sincerely,<br />
        -Tier 1.5</p>
    </body>
</html>"""

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

