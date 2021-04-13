from django.shortcuts import render, redirect


def index(request):
    context = {
        "locations": [
            "Select One",
            "San Jose",
            "San Francisco",
            "Chicago",
            "New York"
        ],
        "languages": [
            "Select One",
            "Python",
            "JavaScript",
            "Java",
            "C#"
        ]
    }
    return render(request, "index.html", context)


def success(request):
    print(request.POST)
    # return render (request, "show.html")
    return redirect("/result")


def result(request):
    return render(request, "show.html")


# def success(request):
#     return render (request, "index.html")

