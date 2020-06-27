from django.shortcuts import render
from .CommentsAnalyzer import comment_analyzer
import json


def index(request):
    
    x = [
			['Country', 'Popularity'],
			['Germany', 200],
			['United States', 300],
			['Brazil', 400],
			['Canada', 500],
			['France', 600],
			['RU', 700]
			]
    args = {'arr':json.dumps(x),'name':"Jaswanth"}
    template_name = 'IBM_home.html'
    return render(request,template_name,args)

def analysis(request):
    link = request.POST['link']
    template_name = 'Analysis.html'
    id = link.split('/')[-1]
    sentiment = comment_analyzer(link)
    positive = sentiment['positive']
    negative = sentiment['negative']
    context = {'id':id,'positive':positive,'negative':negative}
    return render(request,template_name,context)