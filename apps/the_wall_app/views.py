from django.shortcuts import render, HttpResponse, redirect
from .models import User, Message, Comment #importing class to avoid user not defined (name-error)
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("This is the equivalent of @app.route('/')!")
    context = {}
    return render(request, "the_wall_app/index.html", context)

def login(request):
    # return HttpResponse("This is the equivalent of @app.route('/')!")
    # context = {}
    request.session['user_id'] = User.objects.get(email=request.POST['email']).id

    return redirect('/wall')


def delete_comment(request, comment_id):
    Comment.objects.get(id=comment_id).delete()
    return redirect('/wall')

def delete_message(request, message_id):
    Message.objects.get(id=message_id).delete()
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
    errors = User.objects.register_validator(request.POST) # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        # user = User.objects.get(id = id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.last_name = request.POST['last_name']
        user.email = rwquest.POST['email']
        blog.save()
        messages.success(request, "Blog successfully updated")
        # redirect to a success route
        return redirect('/')
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