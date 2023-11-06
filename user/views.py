from django.shortcuts import render
from django_user_agents.utils import get_user_agent
import socket #Para conseguir la información del dispositivo

def archivo(request):
    return render(request, 'user/archivo.html', {})

def my_view(request):

    # Let's assume that the visitor uses an iPhone...
    request.user_agent.is_mobile # returns True
    request.user_agent.is_tablet # returns False
    request.user_agent.is_touch_capable # returns True
    request.user_agent.is_pc # returns False
    request.user_agent.is_bot # returns False

    # Accessing user agent's browser attributes
    request.user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
    request.user_agent.browser.family  # returns 'Mobile Safari'
    request.user_agent.browser.version  # returns (5, 1)
    request.user_agent.browser.version_string   # returns '5.1'

    # Operating System properties
    request.user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
    request.user_agent.os.family  # returns 'iOS'
    request.user_agent.os.version  # returns (5, 1)
    request.user_agent.os.version_string  # returns '5.1'

    # Device properties
    request.user_agent.device  # returns Device(family='iPhone')
    request.user_agent.device.family  # returns 'iPhone'


def my_view(request):

    user_agent = get_user_agent(request)    
    device_type
    is_touch_device
      

    if user_agent.is_mobile: #Si es móvil
        device_type = "Móvil"
        is_touch_device = True #Los móviles que permiten acceder a internet son todos táctiles


    elif user_agent.is_tablet: #Si es tablet
        device_type = "Tablet"
        is_touch_device = True #Todas las taclet son táctiles  


    elif user_agent.is_pc: #Si es ordenador
        device_type = "PC"
        
        
        if user_agent.is_touch_capable: #Si es táctil 
            is_touch_device = True   
        else: #No es táctil
            is_touch_device = False         
  

    else: #BOT
        device_type = "Bot"
        is_touch_device = False 


    ip_cliente = request.META.get('REMOTE_ADDR', '')
    hostname = socket.gethostname()

    return render(request, 'user/archivo.html', {'ip_cliente': ip_cliente, 'hostname': hostname})


