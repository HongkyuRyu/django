from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *
from accounts.models import CustomUser

class PostSerializer(ModelSerializer):
    user_email = serializers.SerializerMethodField('get_user_email')
    
    class Meta:
        model = Post
        fields = ['user_email', 'id', 'userid', 'title', 'contents', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data["userid"] = self.context["request"].user
        post = Post.objects.create(**validated_data)
        post.save()
        return post
    
    def get_user_email(self, obj):
        user = obj.userid
        return user.email
