"""
    Reuseable validate
"""
from re import match

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

#################################################################################
# START USER MODULE


def email_exist(email):
    """
        If email already exist
    """
    return User.objects.filter(email=email).first()


def username_exist(username):
    """
        If username already exist
    """
    return User.objects.filter(username=username).first()

def phone_validate(value):
    pattern = r'^([\d]+){9,12}$'
    if value:
        if not match(pattern, value):
            raise ValidationError('Vui lòng nhập đúng số điện thoại')

# END USER MODULE
#################################################################################
