from django.shortcuts import  render_to_response, render
from django.http import  HttpResponseRedirect
from django.core.context_processors import csrf
from .forms import SignupForm, SensorForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from .models import SensorReading, Sensor


def index(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/smart_agro/home')
    else:
        form = SignupForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form
    return render(request, 'index.html', token)

def login(request):
	print "Enetred login"
	if request.method == "POST":
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = auth.authenticate(username = username, password = password)
		if user is not None:
			print 'logged in'
			auth.login(request,user)
			return HttpResponseRedirect('/smart_agro/home')
		else:
			print "Login error"
			messages.error(request, 'Incorrect username or password')
			return HttpResponseRedirect('/smart_agro')
	else:
		token = {}
		token.update(csrf(request))
		return render_to_response('index.html',token)

def log_out(request):
	auth.logout(request)
	return render(request,'logout.html')

@login_required(login_url="/smart_agro/")
def home(request):
    sensor = None
    sensor_reading = None
    try:
        sensor = Sensor.objects.get(owner=request.user)
        sensor_reading = SensorReading.objects.all().filter(sensor=sensor)
    except:
        print "Error reading data"

    token = {}
    if sensor_reading:
        token['sensor_reading'] = sensor_reading
        token['sensor'] = sensor
    return render(request, "home.html", token)


