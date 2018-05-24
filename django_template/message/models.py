from django.db import models
from custom_user.models import  User

# Create your models here.


class Message(models.Model):
    """
    klasa za slanje poruka između korisnika eg. admin salje obavijest
    """
    # body poruke
    message_body = models.CharField(max_length=200)
    # od koga je poruka poslana
    message_from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_from_user")
    # kome se salje
    message_to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_to_user")
    # da li je user procito poruku
    is_read = models.BooleanField()

    def __str__(self):
        return "message from:" + str(self.message_from_user.id) + " to: " \
               + str(self.message_to_user.id) + ". Message:" +self.message_body + " is read: " +str(self.is_read)


