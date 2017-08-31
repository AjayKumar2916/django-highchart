from django.shortcuts import render
from .models import RainFall

def home(request, template_name="home.html"):
	args = {}
	data = RainFall.objects.all()

	month_list = []
	centimeter_list = []
	for d in data:
		month_list.append(d.month)
		centimeter_list.append(d.centimeter)

	args['month_list'] = month_list
	args['centimeter_list'] = centimeter_list
	return render(request, template_name, args)
