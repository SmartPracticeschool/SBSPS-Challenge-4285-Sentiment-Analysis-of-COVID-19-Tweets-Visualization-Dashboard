from django.shortcuts import render

# Create your views here.
def view(request):
    template_name = 'general_sentiment.html'
    return render(request,template_name)
