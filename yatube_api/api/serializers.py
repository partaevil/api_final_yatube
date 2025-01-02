from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.contrib.auth import get_user_model
from posts.models import Comment, Group, Post, Follow

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        fields = "__all__"
        model = Post
        read_only_fields = ["author", "created_at"]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    post = serializers.ReadOnlyField(source="post.id")

    class Meta:
        model = Comment
        fields = ["id", "author", "post", "text", "created"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "title", "slug", "description"]


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    following = serializers.CharField()

    def validate_following(self, value):
        try:
            User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                f"User with username {value} does not exist."
            )
        return value

    class Meta:
        model = Follow
        fields = ["user", "following"]
