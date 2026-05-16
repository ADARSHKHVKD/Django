from django.shortcuts import render

# Create your views here.
def create(request):
    if request.POST:
        print(request.POST.get('title'))
        print(request.POST.get('year'))
    return render(request,'create.html')
movie_details={
        'movies':[
        {
        'title':'DDLJ',
        'year':1999,
        'summary':'love story of two young people',
        'success':True,
        'img':'logo.webp'
    },
    {
        'title':'godfather',
        'year':1989,
      
        'success':True
    },
    {
        'title':'forest gump',
        'year':2000,
        'summary':'motivational film',
        'success':True
    },
    {
        'title':'shawshank redemption',
        'year':2001,
        'summary':'life of prisoners',
        'success':True
    },
    {
        'title':'life of pi',
        'year':2005,
        'summary':'adventure of young boy',
        'success':True
    }

    ]}

def list(request):
    return render(request,'list.html',movie_details)


def edit(request):
    return render(request,'edit.html')
