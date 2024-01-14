from django.shortcuts import render,redirect
from. import serializer
from rest_framework import viewsets
from. import models
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives,EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token


# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset=models.Patient.objects.all()
    serializer_class=serializer.PatientSerializer

class PatientRegistrationApiView(APIView):
    serializer_class=serializer.RegistrationSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token=default_token_generator.make_token(user)
            print('token:', token)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            print('uid:', uid)
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            email_subject="Confirm Yout Email"
            email_body=render_to_string('confirm_mail.html',{'confirm_link':confirm_link})

            email=EmailMultiAlternatives(email_subject,"",to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response('Check your email for confirm')
        return Response(serializer.errors)
    
def Activate(request, uid64, token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect('register')
    else:
        return redirect('register')


                                
class UserLoginApiView(APIView):
    serializer_class = serializer.UserLoginSerializer  # class attribute

    def post(self, request):
        login_serializer = self.serializer_class(data=request.data)  # renamed variable
        if login_serializer.is_valid():
            username = login_serializer.validated_data['username']
            password = login_serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'Invalid Credentials'})
        return Response(login_serializer.errors)

class UserLogoutApiView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')