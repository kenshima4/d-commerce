from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework import status

from .serializers import ResetPasswordEmail

@api_view(['POST', 'GET'])
def reset_password(request):
    if request.method == "POST":
        serializer = ResetPasswordEmail(data=request.data)
        if serializer.is_valid():

            # get the email from Front-End
            email = serializer.validated_data['email']

            # find the user that has that email
            user = User.objects.get(email=email)

            # get the token of that user
            token = Token.objects.get(user=user)

            if user:

                # pass the context of things above to send them in an email
                context = {
                    'email': email,
                    'username': user,
                    'token': token
                }

                send_mail(
                    'd-commerce Password Reset',
                    render_to_string('emails/reset_password.txt', context),
                    'D-COMMERCE and No Reply',
                    [email],
                    fail_silently=False,
                    auth_user=None, auth_password=None, connection=None, html_message=None
                )
                serializer.save(token=token, slug=token)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        return Response({}, status=status.HTTP_201_CREATED)