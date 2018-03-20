"""
Definition of views.
"""
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import *
from .forms import UserForm, supportForm
from .forms import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,'app/index.html')

def qanda(request):
    ho=request.POST.get('question')
    print(ho)
    a=support(question=ho, answer="")
    a.save()
    form=supportForm
    q=support.objects.all()
    return render(request,'app/supportForm.html',{'form':form, 'q':q})

def main(request):
    """Renders the home page."""
    return render(request,'app/main.html')

def maps(request):
    """Renders the home page."""
    q=request.POST.get('mapdata')
    return render(request,'app/maps.html',{'q':q})


def support1(request):
    """Renders the home page."""
    form=supportForm
    q=support.objects.all()
    return render(request,'app/supportForm.html',{'form':form, 'q':q})

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request,'app/contact.html')
def outcome(request):
    """Renders the contact page."""
    ans=request.POST.get('arra[]')
    print(ans)
    return render(request,'app/outcome.html')

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def output(request):
    home=request.POST.get('home')
    state=request.POST.get('state')
    package=request.POST.get('package')
    mood=request.POST.getlist('option[]')
    print(home)
    p_art=int(mood[0])
    p_adventure=int(mood[1])
    p_historical=int(mood[2])
    p_religious=int(mood[3])
    p_romantic=int(mood[4])
    print(p_art, p_adventure, p_historical, p_religious, p_romantic)
    if p_art==1:
        x='-art'
    elif p_adventure==1:
        x='-adventure'
    elif p_historical==1:
        x='-historical'
    elif p_religious==1:
        x='-religious'
    else:
        x='-romantic'

    if p_art==2:
        y='-art'
    elif p_adventure==2:
        y='-adventure'
    elif p_historical==2:
        y='-historical'
    elif p_religious==2:
        y='-religious'
    else:
        y='-romantic'

    if p_art==3:
        z='-art'
    elif p_adventure==3:
        z='-adventure'
    elif p_historical==3:
        z='-historical'
    elif p_religious==3:
        z='-religious'
    else:
        z='-romantic'

    if p_art==4:
        p='-art'
    elif p_adventure==4:
        p='-adventure'
    elif p_historical==4:
        p='-historical'
    elif p_religious==4:
        p='-religious'
    else:
        p='-romantic'
    
    if p_art==5:
        q='-art'
    elif p_adventure==5:
        q='-adventure'
    elif p_historical==5:
        q='-historical'
    elif p_religious==5:
        q='-religious'
    else:
        q='-romantic'

    ans=rating.objects.order_by(q).order_by(p).order_by(z).order_by(y).order_by(x)[:10]
    #print(ans)
    return render(request,'app/packages.html',{'form':ans})

class UserFormView(View):
    form_class=UserForm
    template_name='registration_form.html'
    def get(self,request):
        form=self.form_class(None)
        return render(request, self.template_name,{'form':form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        return render(request, self.template_name,{'form':form})

def feedback(request):
    form=ratingForm()
    return render(request, 'app/feedback.html',{'form':form})

def feedback_output(request):
    form_class=ratingForm
    form=form_class(request.POST)
    if request.method == "POST" and form.is_valid():
        place=request.POST.get('place_name')
        artist=rating.objects.get(place_name=place)
        

        #post = form.save(commit=False)
        art=int(request.POST.get('art'))
        adventure=int(request.POST.get('adventure'))
        historical=int(request.POST.get('historical'))
        religious=int(request.POST.get('religious'))
        romantic=int(request.POST.get('romantic'))
        budget=int(request.POST.get('budget'))
        #place=request.POST.get('place')
        #artist=rating.objects.get(place_name=place)
        n=int(artist.total)
        artist.art=int(round(((n*int(artist.art))+art)/(n+1),0))
        artist.adventure=int(round(((n*int(artist.adventure))+adventure)/(n+1),0))
        artist.historical=int(round(((n*int(artist.historical))+historical)/(n+1),0))
        artist.religious=int(round(((n*int(artist.religious))+religious)/(n+1),0))
        artist.romantic=int(round(((n*int(artist.romantic))+romantic)/(n+1),0))
        artist.budget=int(round(((n*int(artist.budget))+budget)/(n+1),0))
        artist.total=n+1
        artist.save()

        return render(request, 'app/thankyou.html')
