from django.template.loader import get_template
from django.template import Context
import datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("Hello world")

#def current_datetime(request):
#    now = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now
#    return HttpResponse(html)

def current_datetime(request):
    #now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
    #return render_to_response('current_datetime.html', {'current_date': now})

    current_date = datetime.datetime.now() 
    return render_to_response('current_datetime.html', locals() )

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    #dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    #return HttpResponse(html)
#extend templates
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def current_url_view_good(request):
	return HttpResponse("Welcome to the page at %s" % request.path)

def display_meta(request):
	values = request.META.items()
	values.sort()
	#html = []
#	for k, v in values:
#		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
#		print "HTMLLLLLLLLLLLLLLLLLLLLL IS: %s" % html
#	return HttpResponse('<table>%s</table>' % '\n'.join(html))
	return render_to_response('display_meta.html', {'values': values })


