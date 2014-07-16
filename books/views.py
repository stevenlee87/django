from django.http import HttpResponse 
from django.shortcuts import render_to_response
from books.models import Book

#def search_form(request):
#    return render_to_response('search_form.html')

#def search(request):
#    if 'q' in request.GET:
#        message = 'You searched for: %r' % request.GET['q']
#    else:
#        message = 'You submitted an empty form.'
#    return HttpResponse(message)

#def search(request):
#    if 'q' in request.GET and request.GET['q']:
#        print request.GET
#        q = request.GET['q']
#        books = Book.objects.filter(title__icontains=q)
#        return render_to_response('search_results.html', {'books': books, 'query': q})
#    else:
#        return HttpResponse('Please submit a search term.')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books': books, 'query': q})
    return render_to_response('search_form.html', {'error': error})
