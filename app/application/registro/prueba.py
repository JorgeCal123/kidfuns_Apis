#System



from registro.models import Kid
from registro.models import Progres
from registro.models import Level



for p in Kid.objects.raw('SELECT * FROM myapp_person'):
    print(p)