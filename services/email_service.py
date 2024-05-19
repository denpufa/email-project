from smtplib import SMTP, SMTPConnectError, SMTPHeloError
from email.mime.text 
import ssl

class EmailService:

    def __init__(self, host, port, email, password):
        self.host = host
        self.port = port
        self.email = email
        self.password = password

    def _create_smtp_error_message(self, error):
        return f"smtp code: {error.smtp_code} smtp error: {error.smtp_error}"

    def send_email(self):
        context = ssl.create_default_context()
        try:
            smtp_object = SMTP(host=self.host, port=self.port)
            smtp_object.ehlo_or_helo_if_needed()
            if smtp_object.ehlo_resp:
                smtp_object.starttls(context=context)
            smtp_object.login()
        except SMTPConnectError as error:
            error_message = self._create_smtp_error_message(error)
            error_message += "\n are you sure the SMTP server is running on {host}:{port}?"
            return error_message
        except SMTPHeloError:
            error_message = self._create_smtp_error_message(error)
            error_message += "\n are you sure the SMTP server is running on {host}:{port}?"
            return error_message


        if smtp_object.ehlo_resp:
            smtp_object.starttls(context=context)

        smtp_object.sendmail()