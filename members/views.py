from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Member
from .forms import MemberForm

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def members(request):
  mymembers = Member.objects.all().values()
  activemembers = mymembers.filter(active=True)
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
    'activemembers': activemembers,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=mymember)
        if form.is_valid():
            form.save()
    else:
        form = MemberForm(instance=mymember)
    mymember = Member.objects.get(id=id)    
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
    

def updaterecord(request, id):  
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    phone = request.POST['phone']
    active = request.POST['active']
    member = Member.objects.get(id=id)
    
    member.firstname = firstname
    member.lastname = lastname
    member.phone = phone
    member.active = 'True' if active == 'on' else 'False'
    member.save()
    
    return HttpResponseRedirect(reverse('members'))

def member_change_active(request, id):
    member = Member.objects.get(id=id)
    member.active = 'True' if member.active == 'False' else 'False'
    member.save()
    
    return HttpResponseRedirect(reverse('members'))