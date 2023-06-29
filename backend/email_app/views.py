from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework import status
from django.middleware.csrf import get_token

from django.views.decorators.csrf import csrf_protect
from rest_framework import status
from rest_framework.decorators import api_view

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
                
                subject = 'd-commerce Password Reset'
                
                message = create_message(user)
                
                email_from = settings.EMAIL_HOST_USER
                # email_from = "test@example.com"
                recipient_list = [user.email, ]
                send_mail( subject=subject,message= message, from_email=email_from, recipient_list=recipient_list)

                serializer.save(token=token, slug=token)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def create_message(username):
    password_reset_link = settings.BASE_URL + '/change_password'
    
    message = """
    Hi {0}, 

    you've requested to reset your password. Please follow this link to reset your password: {1}"
    
    Best regards
    d-commerce team
    """.format(username, password_reset_link)
  
    return message

  
  
