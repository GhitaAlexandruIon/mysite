from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html', {})


def add_address(requet):
    return render(requet, 'add_address.html', {})
