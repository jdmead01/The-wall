from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is the equivalent of @app.route('/')!")
    context = {}
    return render(request, "the_wall_app/index.html", context)

def wall(request):
    context = {}
    return render(request, "the_wall_app/wall.html", context)
