from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactoForm

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.save()
            
            # Enviar email de notificación
            try:
                send_mail(
                    f'Nuevo mensaje de {mensaje.nombre}',
                    f"""Tipo: {mensaje.get_tipo_proyecto_display()}
Email: {mensaje.email}
Teléfono: {mensaje.telefono}
Presupuesto: {mensaje.presupuesto}

Mensaje:
{mensaje.mensaje}""",
                    mensaje.email,
                    ['raul.torrescanog@gmail.com'],  # Cambiar por tu email
                    fail_silently=True,
                )
            except:
                pass
            
            messages.success(request, '¡Mensaje enviado! Te contactaré en menos de 24 horas.')
            return redirect('contacto')
    else:
        form = ContactoForm()
    
    return render(request, 'contacto.html', {'form': form})