from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to My Site'
        message = f'''
        {instance.username}
        سلام علیکم
        به وبسایت من خوش آمدید
        ایمیل خوشامدگویی نثارتان نمودم جهت شادی روح امام
        اللهم صل علی محمد و ال محمد و عجل فرج محمد آل محمد'''
        send_from = settings.DEFAULT_FROM_EMAIL
        send_to = [instance.email]
        send_mail(subject, message, send_from, send_to)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()