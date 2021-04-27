from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.staticfiles import finders
from django.utils.html import strip_tags
from email.mime.image import MIMEImage
from django.shortcuts import render
from django.conf import settings

def email_embed_image(email, img_content_id, img_data):
    for i in range(len(img_content_id)):
        img = MIMEImage(img_data[i])
        img.add_header('Content-ID', '<%s>' % img_content_id[i])
        img.add_header('Content-Disposition', 'inline')
        email.attach(img)
    return email

def index(request):
    if request.method == "POST":
        img_content_id = []
        image_data = []
        img_content_id.append("background1.png")
        img_content_id.append("background2.png")
        img_content_id.append("background3.png")
        img_content_id.append("background4.png")
        img_content_id.append("background5.png")
        img_content_id.append("background6.png")
        img_content_id.append("background7.png")
        with open(finders.find('images/background1.png'), 'rb') as f:
            image_data.append(f.read())
        with open(finders.find('images/background2.png'), 'rb') as f:
            image_data.append(f.read())
        with open(finders.find('images/background3.png'), 'rb') as f:
            image_data.append(f.read())
        with open(finders.find('images/background4.png'), 'rb') as f:
            image_data.append(f.read())
        with open(finders.find('images/background5.png'), 'rb') as f:
            image_data.append(f.read())
        with open(finders.find('images/background6.png'), 'rb') as f:
            image_data.append(f.read())
        with open(finders.find('images/background7.png'), 'rb') as f:
            image_data.append(f.read())
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