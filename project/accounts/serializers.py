from .models import CustomUser
from rest_framework.serializers import ValidationError, ModelSerializer

from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate_email(self, value):
        if '@' not in value:
            raise ValidationError("이메일에 '@'가 포함되어야 합니다.")
        return value
    
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("패스워드는 8글자 이상이어야 합니다.")
        return value

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate_email(self, value):
        if '@' not in value:
            raise serializers.ValidationError("이메일에 '@'가 포함되어야 합니다.")
        return value
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("패스워드는 8글자 이상이어야 합니다.")
        return value
    # DB에 해당 값이 있는지 조회
    def validate(self, data):
        email = data.get('email')
        #print(email)
        password = data.get('password')
        #print(password)
        try:
            user = CustomUser.objects.get(email=email, password=password)
            if not user:
                raise serializers.ValidationError("유효한 사용자가 아닙니다.")
            # TODO: 해시함수로 비밀번호 저장하기로 다시 구현해야함.   
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("유효한 사용자가 아닙니다.")

        data['user'] = user
        return data
            
    
        