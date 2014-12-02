#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import *

from captcha.fields import ReCaptchaField

class formulario_capcha(forms.Form):
	captcha = ReCaptchaField(attrs={'theme' : 'clean'})

class formulario_de_perfil(ModelForm):
	class Meta:
		model=datos_adicionales_usuario
		exclude=['username']
class formulario_temas(ModelForm):
	class Meta:
		model=temas
		exclude=['username']
class formulario_preguntas(ModelForm):
	class Meta:
		model=preguntas
		exclude=['username','lista']
class formulario_respuestas_modi(ModelForm):
	class Meta:
		model=respuestas
		exclude=['username','preguntas']
class formulario_respuestas(ModelForm):
	class Meta:
		model=respuestas
		exclude=['username']
class formulario_usuario_registro(UserCreationForm):
	username=forms.CharField(max_length=40,required=True,help_text=False,label="Nick")
	password2=forms.CharField(help_text=False,label="Contraseña de confirmación", widget=forms.PasswordInput)
	first_name=forms.CharField(max_length=50,required=True,label="Nombre")
	last_name=forms.CharField(max_length=50,required=True,label="Apellido")
	email=forms.EmailField(max_length=100,required=True,label="Email")
	class Meta:
		model=User
		fields=("username","password1","password2","first_name","last_name","email")
	def save(self, commit=True):
		user=super(formulario_usuario_registro, self).save(commit=False)
		user.first_name=self.cleaned_data.get("first_name")
		user.last_name=self.cleaned_data.get("last_name")
		user.email=self.cleaned_data.get("email")
		if commit:
			user.save()
		return user