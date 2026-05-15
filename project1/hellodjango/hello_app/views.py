from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_hello(request):
    movie_details={
        'movies':[
        {
        'title':'DDLJ',
        'year':1999,
        'summary':'love story of two young people',
        'success':True
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
    return  render(request,'hello.html',movie_details)
