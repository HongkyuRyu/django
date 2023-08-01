from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("이메일은 필수로 입력해야합니다.")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
    
class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    