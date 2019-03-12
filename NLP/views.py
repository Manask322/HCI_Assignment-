from django.shortcuts import render
from django.core import serializers
import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from NLP.forms import UserForm, OrganisationForm
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from NLP.models import NLP_MAPS
# Create your views here.
import googlemaps
from . import text2info , audio2text

from .models import NLP_MAPS

def index(converted_text):
    template = 'NLP/index.html'
    map = NLP_MAPS()
    res = {}
    res = text2info.get_info(converted_text)
    print("here ", res)
    gmaps = googlemaps.Client(key='AIzaSyBt50Fsl9GeVl0DBf1RIWorWpVfVxdlAV8')
    print("kiops")
    geocode_result = gmaps.geocode(res['Address'])
    print("asaasa")
    print(geocode_result)
    # print(geocode_result)
    map.user_id = 2
    map.Address = res['Address']
    map.x = geocode_result[0]['geometry']['location']['lat']
    map.y = geocode_result[0]['geometry']['location']['lng']
    map.intensity = res['Intensity']
    map.Remarks = res['Remark']
    map.save() 

def dashboard(request):
    address = NLP_MAPS.objects.all()
    return render(request,'dashboard.html',{'address': address})

def manual_entry(request):
    if request.method == 'POST':
        print(request.POST['name'] )
        print(request.POST['remark'])
        print(request.user)
        gmaps = googlemaps.Client(key='AIzaSyCQQIUtvPUSukJ93gTexnAnz1uqXkz79MI')
        geocode_result = gmaps.geocode(request.POST['name'])
        print(geocode_result)
        map = NLP_MAPS()
        map.Address = request.POST['name']
        map.x = geocode_result[0]['geometry']['location']['lat']
        map.y = geocode_result[0]['geometry']['location']['lng']
        map.intensity = 2
        map.Remarks = request.POST['remark']
        map.user_id = request.user
        map.save() 
        return render(request,'Home/home.html') 
    else:
        return render(request,'Home/home.html') 

@csrf_exempt
def audio_data(request):
    if request.method == 'POST':
        print(request.POST['send'])
        gmaps = googlemaps.Client(key='AIzaSyCQQIUtvPUSukJ93gTexnAnz1uqXkz79MI')
        geocode_result = gmaps.geocode(request.POST['send'])
        print(geocode_result)
        map = NLP_MAPS()
        map.user_id = request.user
        map.Address = request.POST['send']
        map.x = geocode_result[0]['geometry']['location']['lat']
        map.y = geocode_result[0]['geometry']['location']['lng']
        map.intensity = 2
        map.Remarks = 2
        map.save() 
        print("jio")
    else:
        print("get") 
    message = "hello"
    return HttpResponse(message)


def home(request):
    user = User.objects.get(pk=1)
    print(user.organisation.organisation)
    return render(request,'Home/home.html') 

def maps(request):
    address = NLP_MAPS.objects.values('id','x','y','Address')
    # serial = serializers.serialize('json', [ address, ])
    json_data = json.dumps(list(address))
    return render(request,'NLP/maps.html',{'address':json_data})


def upload(request):
    print("fshuhdsi")
    if request.method == 'POST' and request.FILES['myfile']:
        print("ywuueiwi")
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        converted_text = audio2text.get_text_from_audio(uploaded_file_url)
        index(converted_text)
        # file_path = os.path.join(BASE_DIR, uploaded_file_url)
        # pass_file_path(file_path)
        # index()
        print(uploaded_file_url)
        return render(request, 'NLP/index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'NLP/upload.html')

    if request.method == 'GET':
        print("jujdsd .....")
        return render(request, 'NLP/upload.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = OrganisationForm(request.POST, instance=request.user.organisation)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return render(request,'Home/home.html')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = OrganisationForm(instance=request.user.organisation)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def create_profile(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        # profile_form = OrganisationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            # profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return render(request,'registration/login.html')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserCreationForm()
        # profile_form = OrganisationForm()
    return render(request, 'profiles/new.html', {
        'user_form': user_form,
        # 'profile_form': profile_form
    })


