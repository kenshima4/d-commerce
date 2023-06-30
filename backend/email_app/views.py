from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.template.loader import render_to_string
from rest_framework.response import Response
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
                subject = 'd-commerce Password Reset'
                link = str(settings.BASE_URL) + '/change_password'

                #get context to pass to templates
                context = { 'username': user, 'link':link}
               
                msg_plain = render_to_string('email_app/email.txt',context)
                msg_html = render_to_string('email_app/email.html',context)
                
                recipient_list = [email, ]

                #send mail with both text and html
                send_mail(subject,msg_plain, html_message=msg_html,from_email=None, recipient_list=recipient_list, fail_silently=False)
                

                serializer.save(token=token, slug=token)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def change_password(request):
    if request.method == "POST":
        data = request.data

        # find the user that has that email
        user = User.objects.get(username=data['username'])
        
        password = data["password"]

        user.set_password(password)
        user.save()

        return Response("Password Changed Successfully", status=status.HTTP_200_OK)
