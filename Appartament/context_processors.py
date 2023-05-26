from User.models import User
def base(request):
    data ={
        'users': User.objects.all(),
        'user_count': User.objects.all().count()
    }
    return data