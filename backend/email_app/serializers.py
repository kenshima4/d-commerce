from rest_framework import serializers

from .models import ResetPassword

class ResetPasswordEmail(serializers.ModelSerializer):
    class Meta:
        model = ResetPassword
        fields = (
            'email',
        )