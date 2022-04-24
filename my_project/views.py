from django.shortcuts import render

def get_some(request):
    return render(request, 'proj/index.html', context={'a': 1, 'b': 2})