from .models import Course

def courses_list(request):
    
    return {'courses_list': Course.objects.all()}