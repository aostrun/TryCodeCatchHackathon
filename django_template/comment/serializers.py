from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ("comment_body", "user_id")
