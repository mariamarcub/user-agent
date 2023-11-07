from django.shortcuts import render
from django_user_agents.utils import get_user_agent
import socket #Para conseguir la información del dispositivo

def index(request):
    return render(request, 'user/index.html', {})


def visitar(request):

    user_agent = get_user_agent(request)            

    if user_agent.is_mobile: #Si es móvil
        device_type = 'Móvil'
        is_touch_device = 'Si es táctil' #Los móviles que permiten acceder a internet son todos táctiles


    elif user_agent.is_tablet: #Si es tablet
        device_type = 'Tablet'
        is_touch_device = 'Si es táctil' #Todas las taclet son táctiles  


    elif user_agent.is_pc: #Si es ordenador
        device_type = 'PC'
        
        
        if user_agent.is_touch_capable: #Si es táctil 
            is_touch_device = 'Si es táctil'   
        else: #No es táctil
            is_touch_device = 'No es táctil'
  

    else: #BOT
        device_type = 'Bot'
        is_touch_device = 'No es táctil'

    
    hostname = socket.gethostname() #obtener el nombre
    ip_cliente = socket.gethostbyname(hostname) #obtener la IP

    return render(request, 'user/visitar.html', {'device_type': device_type, 'is_touch_device': is_touch_device, 'ip_cliente': ip_cliente, 'hostname': hostname})


def info(request):
    user_agent = request.META.get('HTTP_USER_AGENT', None)
    return render(request, 'user/info.html', {'user_agent': user_agent})


