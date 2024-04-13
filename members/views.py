from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Members
from django.urls import reverse
# Create your views here.

def index(request):
    my_members = Members.objects.all().values()
    template = loader.get_template('myfirst.html')
    context = {
        'my_members': my_members
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    # reverse fungsi untuk mengembalikan ke halaman sebelum nya ketika setelah submit form
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    my_members = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'my_members' : my_members
    }
    return HttpResponse(template.render(context, request))

def update_record(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member =Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))
