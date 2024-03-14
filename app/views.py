from django.shortcuts import render

# Create your views here.



from django.http import HttpResponse
from django.core.mail import send_mail

def mail(request):

    # email = 'ashrithaakumar@gmail.com'
    email = 'neethubv10@gmail.com'

    send_mail(
        'Registration',
        'Registration successfull',
        'kalamallarajasekhar256@gmail.com',
        [email],
        fail_silently = False
    )


    return HttpResponse("mail sent successfully")


def register(request):
    
    # email = 'ashrithaakumar@gmail.com'
    # email = 'neethubv10@gmail.com'


    if request.method == 'POST':

        email = request.POST['email']
        send_mail(
            'Registration',
            'Registration successfull',
            'kalamallarajasekhar256@gmail.com',
            [email],
            fail_silently = False
        )


    # return HttpResponse("mail sent successfully")
    return render(request,'register.html')





