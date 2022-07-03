from django.db import connections
from models import Kid


for p in Kid.objects.raw('SELECT * FROM myapp_person'):
    print(p.name)