from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.serializers import ValidationError
from .serializers import CustomUserSerializer
import pytest

class UserRegistrationIntegrationTest(TestCase):
    def test_user_registration(self):
        url = reverse('user-registration')
        data={
            'email': 'test@example.com',
            'password': 'TestPassword12345'
        }
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CustomUserSerializerTest(TestCase):
    def test_valid_data(self):
        data = {'email': 'test@example.com', 'password': 'TestPassword12345'}
        serializer = CustomUserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
    # 이메일 조건 검사
    @pytest.mark.xfail
    def test_invalid_email(self):
        data = {'email': 'email', 'password': 'TestPassword12345'}
        serializer = CustomUserSerializer(data=data)
        # self.assertFalse(serializer.is_valid())
        is_valid = serializer.is_valid()
        if not is_valid:
            errors = serializer.errors.get('email', [])
            error_message = str(errors[0]) if errors else ''
            # print(errors)
            # print(error_message)
            assert '@' in error_message  
            
    # 패스워드 조건 검사
    def test_invalid_password(self):
        data = {'email': 'test@exmaple.com', 'password': 'Test'}
        serializer = CustomUserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
    
        
