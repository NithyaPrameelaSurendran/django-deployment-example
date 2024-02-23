from django.shortcuts import render
from second_app.models import User
from  second_app.forms import New_User_Form
# Create your views here.
'''def help(request):
    help_dict={'insert_me':"Go to /users to see the list of user information!"}
    return render(request,'second_app/help.html',context=help_dict)'''
    
def index(request):
    
    return render(request,'second_app/index.html')

def user(request):
    form=New_User_Form()
    
    if request.method=="POST":
        form=New_User_Form(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
        else:
            print("Error form invalid!")
    
    return render(request,'second_app/user.html',{'form':form})

    '''user_lists=User.objects.all()
    user_dict={'user_list':user_lists}
    return render(request,'second_app/user.html',context=user_dict)'''