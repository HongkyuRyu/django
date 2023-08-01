from .models import CustomUser
from rest_framework.serializers import ValidationError, ModelSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate

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

class UserLoginSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
    
    def validate_email(self, value):
        if '@' not in value:
            raise ValidationError("이메일에 '@'가 포함되어야 합니다.")
        return value
    
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("패스워드는 8글자 이상이어야 합니다.")
        return value
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user = authenticate(username=email, password=password)
            if user:
                if not user.is_active:
                    raise ValidationError("계정이 비활성화 상태입니다.")
            else:
                raise ValidationError("올바른 이메일과 비밀번호를 입력해주세요.")
        else:
            raise ValidationError("이메일과 비밀번호를 입력해주세요.")
        
        data['user'] = user
        return data
            
    
        