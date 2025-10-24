import os 
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'School.settings')
django.setup()

from schoolapp.models import Teacher

def main():
    teachers = Teacher.objects.all().order_by('id')
    if not teachers:
        print("No teachers found.")
        return
    print("Teacher in DB:")
    for t in teachers:
        print(f"{t.id} | {t.name} | photo: {t.photo.url if t.photo else 'None'} ")
if __name__=='__main__':
    main()        

