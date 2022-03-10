from django.shortcuts import redirect, render

def home_page(request):
    if request.method == "POST":
        print(request.POST)
        return redirect("aboutpage")
    
    context = {
        "section" : "home"
    }

    return render(request, "home.html", context=context)

def about_page(request):


    context = {
        "section" : "about"
    }

    return render(request, "about.html", context=context)


def about_pages(request, name, age):

    name = name+age 
    
    context = {
        "section" : "about",
        "name" : name
    }

    return render(request, "about.html", context=context)

