from telnetlib import STATUS
from tokenize import Token
from django.shortcuts import redirect, render
from rest_framework import generics
from .models import Persona 
from .serializers import personaSerializer
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from  rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
def _redirect(request):
    return redirect("/admin/")

class personaList(generics.ListCreateAPIView):
    queryset=Persona.objects.all()
    serializer_class=personaSerializer    #estas son palabras estaticas ya de django  serializer_class 
    permission_classes=(IsAuthenticated,)#estas son palabras estaticas ya de django  serializer_class
    authentication_class =(TokenAuthentication,)#estas son palabras estaticas ya de django  serializer_class
class Login(FormView):
    template_name="login.html"
    form_class=AuthenticationForm
    success_url=reverse_lazy("apii:persona_list")
    

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
 
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, **kwargs)# video 33:43

    def form_valid(self,form):
        user= authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
        token,_= Token.objects.get_or_create(user=user)

        if token: # validamos que exista el token 

            login(self.request,form.get_user())
            return super(Login,self).form_valid(form)#valido el formulario
    
class Logout(APIView):
    def get(self,request,format=None):
        request.user.auth_token.delete()#con esto lo elimino mi token
        logout(request)#con esto cierro mi login 
        return Response(status= status.HTTP_200_OK )

    

