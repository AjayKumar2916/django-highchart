import os

import django
os.environ['DJANGO_SETTINGS_MODULE']='djchart.settings'
django.setup()

from chart.models import RainFall

rainfall_data = [
	{'month':"JAN", 'centimeter':33},
	{'month':"FEB", 'centimeter':55},
	{'month':"MAR", 'centimeter':75},
	{'month':"APR", 'centimeter':45},
	{'month':"MAY", 'centimeter':36},
	{'month':"JUN", 'centimeter':15},
	{'month':"JUL", 'centimeter':26},
	{'month':"AUG", 'centimeter':66},
	{'month':"SEP", 'centimeter':93},
	{'month':"OCT", 'centimeter':40},
	{'month':"NOV", 'centimeter':16},
	{'month':"DEC", 'centimeter':82},
]

for data in rainfall_data:
	RainFall.objects.create(**data)

print('Data populated')
