from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from contact.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                'imepisode1@126.com',
                [cd.get('email')],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
			initial={'subject': 'I love your site!'}
		)
    return render_to_response('contact_form.html', {'form': form})
