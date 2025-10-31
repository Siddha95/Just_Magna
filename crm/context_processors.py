from .models import Course

def all_courses(request):
    
    return {'all_courses': Course.objects.all()}