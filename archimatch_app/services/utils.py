from archimatch_project import settings
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
import os

def send_email_with_template(to_email, subject, body, images):
    """Global function to send email with HTML template."""
    from_email = settings.DEFAULT_FROM_EMAIL
    email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
    email_message.attach_alternative(body, "text/html")
    attach_email_icons(email_message, images)
    email_message.send()


def attach_email_icons(msg, images):
    """method to attach icons to email template"""
    msg.mixed_subtype = "related"
    for image in images:
        
        file_path = os.path.join(image[0], image[1])
        print(file_path)
        with open(file_path, "rb") as f:
            img = MIMEImage(f.read(),_subtype="image/svg+xml")
            
            img.add_header("Content-ID", "<{name}>".format(name=image[1]))
            img.add_header("Content-Disposition", "inline", filename=image[1])
        msg.attach(img)




