from django.shortcuts import render
from django.utils.html import escape
import os

# Create your views here.
def index(request):
    sukkel = "godefrey"
    if "message" in request.GET:
        sukkel = escape(request.GET["message"])
        with open("chat/ff.txt", 'a') as kyle:
            kyle.write(request.GET["message"] + "\n")
    
    print(os.getcwd())
    with open("chat/ff.txt", "r") as file:
        lol = file.readlines()
        for i in range(len(lol)):
            lol[i] = lol[i].rstrip("\n")

    return render(request, "index.html", {"lol": lol})