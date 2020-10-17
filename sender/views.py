from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
	if request.method == 'POST':
		message_name = request.POST['name']
		message_email = request.POST['email']
		message = request.POST['message']

		send_mail(
			'Project 1'+' : '+str(message_email),	# Subject
			message,	# Message
			message_email,	# From email
			['thereceivingemail@gmail.com'],	# To email
			fail_silently=False)

		return redirect('index')
		messages.success(request, f'Your mail has been received we would get back to you shortly')

	else:
		return render(request, 'index.html')
