from django.db import models
from custom_user.models import  User
from custom_user.models import User

# Create your models here.


class Message(models.Model):
    """
    klasa za slanje poruka između korisnika eg. admin salje obavijest
    """
    # body poruke
    message_body = models.CharField(max_length=200)
    # od koga je poruka poslana
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # kome se salje
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # da li je user procito poruku
    is_read = models.BooleanField()

    def __str__(self):
        return "message from:" + self.from_user + " to: " + self.to_user + ". Message:" +self.message_body


