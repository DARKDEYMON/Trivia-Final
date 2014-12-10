from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class datos_adicionales_usuario(models.Model):
	username=models.OneToOneField(User, unique=True)
	pais=models.CharField(max_length=100, null=True)
	avatar=ImageWithThumbsField(upload_to="avatares/", sizes=((50,50),(200,200)), null=True)
	def __unicode__(self):
		return self.username.username
	class Meta:
		verbose_name = _('Datos Adicionales de usuario')
		verbose_name_plural = _('Datos Adicionales de usuarios')
class temas(models.Model):
	username=models.ForeignKey(User)
	tema=models.CharField(max_length=100, null=True)
	def __unicode__(self):
		return self.tema
	class Meta:
		verbose_name = _('Tema')
		verbose_name_plural = _('Temas')
class preguntas(models.Model):
	username=models.ForeignKey(User)
	temas=models.ManyToManyField(temas)
	pregunta=models.CharField(max_length=100, null=True, unique=True)
	lista=models.BooleanField(default=False)
	def __unicode__(self):
		return self.pregunta
	class Meta:
		verbose_name = _('Pregunta')
		verbose_name_plural = _('Preguntas')
class respuestas(models.Model):
	username=models.ForeignKey(User)
	preguntas=models.OneToOneField(preguntas, unique=True)
	respuesta_correcta=models.CharField(max_length=100, null=False)
	respuesta_opcional_1=models.CharField(max_length=100, null=False)
	respuesta_opcional_2=models.CharField(max_length=100, null=False)
	respuesta_opcional_3=models.CharField(max_length=100, null=False)
	respuesta_opcional_4=models.CharField(max_length=100, null=False)
	def __unicode__(self):
		return "Respuesta a: "+self.preguntas.pregunta
	class Meta:
		verbose_name = _('Respuestas')
		verbose_name_plural = _('Respuestas')
class rate(models.Model):
	preguntas=models.ForeignKey(preguntas)
	rates=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5))
	rate=models.IntegerField(choices=rates,default=0)
	class Meta:
		verbose_name = _('Rate')
		verbose_name_plural = _('Rate')
class partida(models.Model):
	b=((10,10),(20,20),(30,30))
	nombre_de_partida=models.CharField(max_length=100, null=False)
	max_jugadores=models.IntegerField(null=False)
	temas=models.ManyToManyField(temas, null=False)
	num_preguntas=models.IntegerField(null=False)
	tiempo_maximo=models.IntegerField(null=False, choices=b)
	acabada=models.BooleanField(default=False)
	def __unicode__(self):
		return self.nombre_de_partida
	class Meta:
		verbose_name = _('Partida')
		verbose_name_plural = _('Partidas')
class jugadores_en_partida(models.Model):
	partida=models.ForeignKey(partida)
	user=models.ForeignKey(User)