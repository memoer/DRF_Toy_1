from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Comment


class CommentSerializer(ModelSerializer):
    ccomment = StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("deleted_at",)
