from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Reply


@receiver(post_save, sender=Reply)
def reply_created(instance, created, **kwargs):
    if not created:
        return

    reply = Reply.objects.get(id=instance.pk)
    send_mail(
        subject='New reply',
        message=f'{reply.author.username} responded to the post - "{reply.post.title}"!',
        from_email=None,
        recipient_list=[reply.post.author.email],
    )
