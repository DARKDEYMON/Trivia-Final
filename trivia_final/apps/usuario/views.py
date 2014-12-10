from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse,Http404
from form import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User
from models import *
from django.contrib.sessions.backends.db import SessionStore

from django.contrib.auth.views import password_change
from django.contrib.auth.forms import PasswordChangeForm
import pdb
# Create your views here.
def permisos_quitar_view(request,id):
	if request.user.is_authenticated():
		if request.user.is_staff:
			datospre=User.objects.get(id=id)
			datospre.is_staff=False
			print datospre.is_staff
			datospre.save()
			return render_to_response("sistema/staff_quitado.html",{},context_instance=RequestContext(request))
		else:
			raise Http404("page no exist")
	else:
		return HttpResponse("no esta logeado")
def permisos_lista_view(request):
	if request.user.is_authenticated():
		if request.user.is_staff:
			aux=aux=User.objects.filter(is_superuser=0)
			if len(aux)!=0:
				return render_to_response("sistema/lista_user.html",{"usuario":aux},context_instance=RequestContext(request))
			else:
				return Http404("Vacio")
		else:
			raise Http404("page no exist")
	else:
		return HttpResponse("no esta logeado")
def permisos_view(request,id):
	if request.user.is_authenticated():
		if request.user.is_staff:
			datospre=User.objects.get(id=id)
			datospre.is_staff=True
			datospre.save()
			return render_to_response("sistema/staff.html",{},context_instance=RequestContext(request))
		else:
			raise Http404("page no exist")
	else:
		return HttpResponse("no esta logeado")
def crear_sal_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			auxform=formulario_partida(request.POST)
			if auxform.is_valid():
				h=auxform.save()
				#auxform.save_m2m()
				return render_to_response("sistema/crear_sala.html",{"form_rom":auxform,"redi":True,"sala":h.pk},context_instance=RequestContext(request))
		else:
			auxform=formulario_partida()
		return render_to_response("sistema/crear_sala.html",{"form_rom":auxform,"redi":False},context_instance=RequestContext(request))
	else:
		raise Http404("page no exist")
def password_change(request,template_name='usuario/cambio_pass.html', post_change_redirect=None, password_change_form=PasswordChangeForm,current_app=None, extra_context=None):
	if request.user.is_authenticated():
	    if request.method == "POST":
	        form = password_change_form(user=request.user, data=request.POST)
	        if form.is_valid():
	            form.save()
	            # Updating the password logs out all other sessions for the user
	            # except the current one if
	            # django.contrib.auth.middleware.SessionAuthenticationMiddleware
	            # is enabled.
	            #update_session_auth_hash(request, form.user)
	            #cookie=SessionStore(session_key=request.session["idkey"])
				#cookie["estado"]="desconectado"
	            return HttpResponseRedirect("/")
	    else:
	        form = password_change_form(user=request.user)
	    return render_to_response("usuario/cambio_pass.html",{"form":form},context_instance=RequestContext(request))
	else:
		raise Http404("page no exist")
def lista_preguntas_modificar_respuesta_view(request,id):
	if request.user.is_authenticated():
		if request.user.is_staff:
			datospre=preguntas.objects.get(id=id)
			#pdb.set_trace()
			aux=respuestas.objects.filter(preguntas=datospre)
			if len(aux)!=0:
				if request.method=="POST":
					#usuario=request.user
					aux1=respuestas.objects.get(preguntas=datospre)
					auxform=formulario_respuestas_modi(request.POST,instance=aux1)
					#pdb.set_trace()
					if auxform.is_valid():	
						post=auxform.save(commit=False)
						post.username=request.user
						post.save()
						#auxform.save_m2m()
						return HttpResponseRedirect("/")
				else:
					auxform=formulario_respuestas_modi()
				#datosadiuser=User.get(username=request.user)
				return render_to_response("sistema/modificar_respuesta.html",{"resp":aux[0],"form_modi":auxform},context_instance=RequestContext(request))
			else:
				raise Http404("page no exist")
		else:
			raise Http404("page no exist")
	else:
		return HttpResponse("no esta logeado")
def lista_preguntas_modificar_pregunta_view(request,id):
	if request.user.is_authenticated():
		if request.user.is_staff:
			aux=preguntas.objects.filter(id=id)
			if len(aux)!=0:
				if request.method=="POST":
					#usuario=request.user
					datospre=preguntas.objects.get(id=id)
					auxform=formulario_preguntas(request.POST,instance=datospre)
					#pdb.set_trace()
					if auxform.is_valid():	
						#pdb.set_trace()
						auxform.save()
						#auxform.save_m2m()
						return HttpResponseRedirect("/")
				else:
					auxform=formulario_preguntas()
				#datosadiuser=User.get(username=request.user)
				return render_to_response("sistema/modificar_pregunta.html",{"preguntas":aux[0],"form_modi":auxform},context_instance=RequestContext(request))
			else:
				raise Http404("page no exist")
		else:
				raise Http404("page no exist")
	else:
		return HttpResponse("no esta logeado")
def lista_preguntas_view(request):
	if request.user.is_authenticated():
		if request.user.is_staff:
			aux=preguntas.objects.filter()
			#pdb.set_trace()
			if len(aux)!=0:
				return render_to_response("sistema/lista_preguntas.html",{"preguntas":aux},context_instance=RequestContext(request))
			else:
				raise Http404("page no exist")
		else:
				raise Http404("page no exist")

	else:
		return HttpResponse("no esta logeado")
def lista_preguntas_eliminar_view(request,id):
	if request.user.is_authenticated():
		if request.user.is_staff:
			aux=preguntas.objects.filter(id=id)
			if len(aux)!=0:
				preguntas.objects.get(id=id).delete()
				return render_to_response("sistema/eliminar_preguntas.html",{"pregunta":aux[0]},context_instance=RequestContext(request))
			else:
				raise Http404("page no exist")
		else:
				raise Http404("page no exist")
	else:
		return HttpResponse("no esta logeado")
def respuestas_view(request):
	if request.user.is_authenticated():
		usuario=request.user
		if request.method=="POST":
			auxform=formulario_respuestas(request.POST)
			if auxform.is_valid():
				post=auxform.save(commit=False)
				post.username=usuario
				post.save()
				#pdb.set_trace()
				t1=request.POST['preguntas']
				t2 = preguntas.objects.get(id=t1)
				t2.lista=True
				t2.save()
				return HttpResponseRedirect("/")
		else:
			auxform=formulario_respuestas()
		return render_to_response("sistema/respuestas.html",{"form_respuesta":auxform},context_instance=RequestContext(request))
	else:
		return HttpResponse("no esta logeado")
def preguntas_view(request):
	if request.user.is_authenticated():
		usuario=request.user
		if request.method=="POST":
			auxform=formulario_preguntas(request.POST)
			if auxform.is_valid():
				#pdb.set_trace()
				post= auxform.save(commit=False)
				post.username=usuario
				post.save()
				auxform.save_m2m()
				return HttpResponseRedirect("/")
		else:
			auxform=formulario_preguntas()
		return render_to_response("sistema/preguntas.html",{"form_pregunta":auxform},context_instance=RequestContext(request))
	else:
		return HttpResponse("no esta logeado")
def temas_view(request):
	if request.user.is_authenticated():
		usuario=request.user
		if  request.method=="POST":
			auxform=formulario_temas(request.POST)
			#datouser=User.objects.get(username=usuario)
			if auxform.is_valid():
				#pdb.set_trace()
				post = auxform.save(commit=False)
		        post.username = usuario
		        post.save()
		        return HttpResponseRedirect("/")
		else:
			auxform=formulario_temas()
		return render_to_response("sistema/temas.html",{"form_tema":auxform},context_instance=RequestContext(request))
	else:
		return HttpResponse("no esta logeado")
def registro_view(request):
	if request.method=="POST":
		auxform=formulario_usuario_registro(request.POST)
		if auxform.is_valid():
			usuario=request.POST['username']
			auxform.save()
			usuariodato=User.objects.get(username=usuario)
			#pdb.set_trace()
			perfil=datos_adicionales_usuario.objects.create(username=usuariodato)
			return HttpResponseRedirect("/")
	else:
		auxform = formulario_usuario_registro()
	return render_to_response("usuario/registro.html",{"form_regi":auxform},context_instance=RequestContext(request))

def login_view(request):
	if request.method=="POST":
		auxform=AuthenticationForm(data=request.POST)
		#pdb.set_trace()
		if request.session['con']>3:
			form_captcha=formulario_capcha(request.POST)
			if form_captcha.is_valid():
				pass
			else:
				datos={"form_login":auxform,"form_chaptcha":form_captcha}
				return render_to_response("usuario/login.html",datos,context_instance=RequestContext(request))		
		if auxform.is_valid():
			usuario=request.POST['username']
			contrasena=request.POST['password']
			acceso=authenticate(username=usuario,password=contrasena)
			#pdb.set_trace()
			if acceso is not None:
				del request.session['con']
				login(request,acceso)
				#cookie de secion inicia aca para node js
				cookie=SessionStore()
				cookie["name"]=usuario
				cookie["estado"]="conectado"
				cookie.save()
				#request.COOKIES.get('idkey', cookie.session_key)
				request.session["idkey"]=cookie.session_key
				print cookie.session_key
				return HttpResponseRedirect("/")
		else:
			request.session['con']=request.session['con']+1
			auxcon=request.session["con"]
			estado=True
			mensaje="Error en los datos "+str(auxcon)
			if auxcon>3:
				estado=False
				form_captcha=formulario_capcha()
				return render_to_response("usuario/login.html",{"form_login":auxform,"estado":estado,"mensaje":mensaje,"form_chaptcha":form_captcha},context_instance=RequestContext(request))
			else:
				return render_to_response("usuario/login.html",{"form_login":auxform,"estado":estado,"mensaje":mensaje},context_instance=RequestContext(request))
	else:
		request.session['con']=0
		auxform=AuthenticationForm()
	return render_to_response("usuario/login.html",{"form_login":auxform},context_instance=RequestContext(request))
def logout_view(request):
	cookie=SessionStore(session_key=request.session["idkey"])
	cookie["estado"]="desconectado"
	#del request.cookie["idkey"]
	cookie["name"]=""
	cookie.save()
	logout(request)
	return HttpResponseRedirect("/")
def actualisar_perfil_view(request):
	if request.user.is_authenticated():
		usuario=request.user
		if request.method=="POST":
			auxform=formulario_de_perfil(data=request.POST)
			datouser=User.objects.get_by_natural_key(username=usuario)
			datosadiuser=datos_adicionales_usuario.objects.get(username=datouser)
			auxform=formulario_de_perfil(request.POST,request.FILES,instance=datosadiuser)
			if auxform.is_valid():
				auxform.save()
				return HttpResponseRedirect("/")
			else:
				return HttpResponse("algo salio mal")
		else:
			auxform=formulario_de_perfil()
		return render_to_response("usuario/actualisar.html",{"form_actua":auxform},context_instance=RequestContext(request))
	else:
		return HttpResponse("no esta logeado")