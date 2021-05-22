from django.db.models.enums import Choices
from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth import login as LoginUser
from .models import  *
from django.http import HttpResponseRedirect
import json
 
#def index(request):
    #return HttpResponse("This is homepage")
def index(request):
    context = {
         "variable":"this is sent"

    }
    return render(request,'index.html',context)
@csrf_exempt
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            LoginUser(request,user)
            return redirect(index)
        print("username")
        print("password")
    return render(request, "login.html")
def Logout(request):
    logout(request,user)

def rooms(request):
    return render(request,'rooms.html')
    #return HttpResponse("This is rooms page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is services page")

def result(request):
    program = Student.objects.all()
    d = {'program': program}
    #m=list()
    #for prog in program:
        #m.append(prog.name)
    #ma='<br>'.join(m)
    #return HttpResponse(ma)
    return render(request,'result.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')

def preferences(request):
    program = Student.objects.all()
    d = {'program': program}
    testing=[]
    prin=Student.objects.values()
    #m=list()
    for prog in program:
        testing.append(prog.name)
    student=Student()
    student.name=json.dumps(testing)
    student.save()
    

     

    return render(request,'preferences.html',d)
   
    #return render(request,'preferences.html',d)


def stable(request):
    # Python3 program for stable marriage problem

    # Number of Men or Women
    N = 4

    # This function returns true if
    # woman 'w' prefers man 'm1' over man 'm'
    def wPrefersM1OverM(prefer, w, m, m1):
        
        # Check if w prefers m over her
        # current engagment m1
        for i in range(N):
            
            # If m1 comes before m in lisr of w,
            # then w prefers her current engagement,
            # don't do anything
            if (prefer[w][i] == m1):
                return True

            # If m cmes before m1 in w's list,
            # then free her current engagement
            # and engage her with m
            if (prefer[w][i] == m):
                return False

    # Prints stable matching for N boys and N girls.
    # Boys are numbered as 0 to N-1.
    # Girls are numbereed as N to 2N-1.
    def stableMarriage(prefer):
        
        # Stores partner of women. This is our output
        # array that stores paing information.
        # The value of wPartner[i] indicates the partner
        # assigned to woman N+i. Note that the woman numbers
        # between N and 2*N-1. The value -1 indicates
        # that (N+i)'th woman is free
        wPartner = [-1 for i in range(N)]

        # An array to store availability of men.
        # If mFree[i] is false, then man 'i' is free,
        # otherwise engaged.
        mFree = [False for i in range(N)]

        freeCount = N

        # While there are free men
        while (freeCount > 0):
            
            # Pick the first free man (we could pick any)
            m = 0
            while (m < N):
                if (mFree[m] == False):
                    break
                m += 1

            # One by one go to all women according to
            # m's preferences. Here m is the picked free man
            i = 0
            while i < N and mFree[m] == False:
                w = prefer[m][i]

                # The woman of preference is free,
                # w and m become partners (Note that
                # the partnership maybe changed later).
                # So we can say they are engaged not married
                if (wPartner[w - N] == -1):
                    wPartner[w - N] = m
                    mFree[m] = True
                    freeCount -= 1

                else:
                    
                    # If w is not free
                    # Find current engagement of w
                    m1 = wPartner[w - N]

                    # If w prefers m over her current engagement m1,
                    # then break the engagement between w and m1 and
                    # engage m with w.
                    if (wPrefersM1OverM(prefer, w, m, m1) == False):
                        wPartner[w - N] = m
                        mFree[m] = True
                        mFree[m1] = False
                i += 1

                # End of Else
            # End of the for loop that goes
            # to all women in m's list
        # End of main while loop

        # Prthe solution
        print("Woman ", " Man")
        for i in range(N):
            print(i + N, "\t", wPartner[i])
    #
    # s=Student.objects.get(id=1)

    prefer = [[1,5, 6, 4], [5, 4, 6, 7],
            [4, 5, 6, 7], [4, 5, 6, 7],
            [0, 1, 2, 3], [0, 1, 2, 3],
            [0, 1, 2, 3], [0, 1, 2, 3]]
    stableMarriage(prefer)
    return render(request,'result.html')

    