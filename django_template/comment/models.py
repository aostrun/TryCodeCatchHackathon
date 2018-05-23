from django.db import models
from custom_user.models import User

# Create your models here.


class Comment(models.Model):
    """
    pojedini user može ostavljati komentare na aplikaciju

    """

    # tijelo komentara
    comment_body = models.CharField(max_length=200)
    # id usera koji ostavlja komentar
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_body
