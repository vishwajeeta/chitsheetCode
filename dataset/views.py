from itertools import chain
from django.shortcuts import render
from .models import sample
# Create your views here.
def home(request):
    data=sample.objects.all()
    return render(request,'home.html',{"data":data})

def search(request):

    if request.method == 'POST':
        username = request.POST['userdata']
        username_object = sample.objects.filter(topic__icontains=username)

        username_profile = []
        username_profile_list = []

        for topic in username_object:
            username_profile.append(topic.id)

        for ids in username_profile:
            profile_lists = sample.objects.filter(id=ids)
            username_profile_list.append(profile_lists)
        
        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html', { 'data': username_profile_list,'searched':username})
    
def show_data(request,pk):
    
       data=sample.objects.filter(id=pk)
       
       return render(request,'show.html',{'data':data})
    