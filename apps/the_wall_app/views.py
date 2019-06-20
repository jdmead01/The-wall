from django.shortcuts import render, HttpResponse, redirect
from .models import User, UserManager, BaseModel, Message, Comment #importing class to avoid user not defined (name-error)
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("This is the equivalent of @app.route('/')!")
    context = {}
    return render(request, "the_wall_app/index.html", context)

def login(request):
    # return HttpResponse("This is the equivalent of @app.route('/')!")
    context = {}
    return redirect('/wall')


def delete(request, id):
    comment = Comment.objects.get(id=comment_id).delete()
    return redirect('/wall')

def wall(request):
    context = {
        'users': User.objects.all(), 
        'current_user': User.objects.get(id=request.session['user_id']),
        # getting the object from all the user objects that matches ONLY the current user in the session
        'comments': Comment.objects.all(), 
        'messages': Message.objects.all()
    }
    return render(request, "the_wall_app/wall.html", context)

# what the form submission is creating within the DB - fields from the Models.py 
def register(request):
    # make user as an object
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'])
    # pass something into session once user is added to the DB so it is saved globally to the site. 
    request.session['user_id'] = User.objects.last().id
    return redirect('/wall')

def post_message(request):
    current_user = User.objects.get(id=request.session['user_id'])#user name variable is equal to the current user
    current_message = request.POST['message'] # because thats the name I called it in HTML (name for the input) 
    Message.objects.create(message=current_message,author=current_user)
    return redirect ('/wall')


def post_comment(request):
    current_user = User.objects.get(id=request.session['user_id'])#user name variable is equal to the current user in session 
    current_comment = request.POST['comment'] # because thats the name I called it in HTML (name for the input) 
    commented_on = Message.objects.get(id=request.POST['current_message']) #grabbing the message that the user is in going to make a comments on within session grabbing the user ID using request.POST and referencing the name given in index "current_message"
    Comment.objects.create(comment=current_comment,commented_on=commented_on,author=current_user)
    return redirect ('/wall')

def logoff(request):
    return redirect('/')