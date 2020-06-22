from django.shortcuts import render
from .CommentsAnalyzer import comment_analyzer
# Create your views here.

def index(request):
    template_name = 'generalTwitter.html'
    return render(request,template_name)

def analysis(request):
    link = request.POST['link']
    template_name = 'Analysis.html'
    id = link.split('/')[-1]
    sentiment = comment_analyzer(link)
    positive = sentiment['positive']
    negative = sentiment['negative']
    context = {'id':id,'positive':positive,'negative':negative}
    return render(request,template_name,context)