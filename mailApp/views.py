from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.staticfiles import finders
from django.utils.html import strip_tags
from email.mime.image import MIMEImage
from django.shortcuts import render
from django.conf import settings

def email_embed_image(email, img_content_id, img_data):
    img = MIMEImage(img_data)
    img.add_header('Content-ID', '<%s>' % img_content_id)
    img.add_header('Content-Disposition', 'inline')
    email.attach(img)
    return email

def index(request):
    if request.method == "POST":
        img_content_id = "background1.jpg"
        with open(finders.find('images/background1.jpg'), 'rb') as f:
            image_data = f.read()
        toEmailsraw = request.POST.get("toaddress")
        toEmailsraw = toEmailsraw.strip().split(',')
        toEmail = []
        for i in toEmailsraw:
            toEmail.append(i.strip())
        html_content = render_to_string('mailApp/email_template.html')
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives("Prestige Gifting Delights",text_content,settings.EMAIL_HOST_USER,toEmail)
        email.attach_alternative(html_content,'text/html')
        email = email_embed_image(email,img_content_id,image_data)
        email.send()
        return render(request,'mailApp/index.html')
    else:
        return render(request,'mailApp/index.html')