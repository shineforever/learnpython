from django.shortcuts import render
import json

# Create your views here.

data = [1, 2, 3, 4]


def view(request, id):
    print(id)
    print({"data": json.dumps(data)})
    return render(request, "view1.html", {"data": ["1", "2", "3"]})
