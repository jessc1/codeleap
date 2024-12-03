from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class UserManager(BaseUserManager):
    def get_object_by_id(self, user_id):
        try:
            instance = self.get(user_id=self.user.id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return 404

    def create_user(self, username, password=None, **kwargs):
        """ Create a user with username and password """
        if username is None:
            raise TypeError("Expected  username")
        if password is None:
            raise TypeError('Expected password')
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **kwargs):
        """ Create a superuser with admin permissions"""
        if password is None:
            raise TypeError('Expected password')
        if username is None:
            raise TypeError('Expected username')
        user = self.create_user(username, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    created = models.DateTimeField(auto_now=True)
    title = models.TextField()
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    

    objects = UserManager()

    def __str__(self):
        return f"self.username"



        


