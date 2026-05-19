from django.shortcuts import render
from . models import MovieInfo
from . forms import MovieForm
# Create your views here.
def create(request):
    frm =MovieForm ()
    if request.POST:
        title=(request.POST.get('title'))
        year=(request.POST.get('year'))
        description=(request.POST.get('description'))
        movie_obj=MovieInfo(title=title,year=year,description=description)
        movie_obj.save()
    return render(request,'create.html',{'frm':frm})
# movie_details={
#         'movies':[
#         {
#         'title':'DDLJ',
#         'year':1999,
#         'summary':'love story of two young people',
#         'success':True,
#         'img':'logo.webp'
#     },
#     {
#         'title':'godfather',
#         'year':1989,
      
#         'success':True
#     },
#     {
#         'title':'forest gump',
#         'year':2000,
#         'summary':'motivational film',
#         'success':True
#     },
#     {
#         'title':'shawshank redemption',
#         'year':2001,
#         'summary':'life of prisoners',
#         'success':True
#     },
#     {
#         'title':'life of pi',
#         'year':2005,
#         'summary':'adventure of young boy',
#         'success':True
#     }

#     ]}


def list(request):
    movie_set=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_set})


def edit(request):
    return render(request,'edit.html')
