from django.views.generic import View
from django.shortcuts import render

# Create your views here.
class Helloworldview(View):

    def get(self,request,*args,**kwargs):

        return render(request,"hello_world.html"),



class Goodmorningview(View):

    def get(self,request,*args,**kwargs):

        return render(request,"good_morning.html"),



class Goodafternoonview(View):

    def get(self,request,*args,**kwargs):

        return render(request,"good_afternoon.html"),




class Goodeveningview(View):

    def get(self,request,*args,**kwargs):

        return render(request,"good_evening.html"),


class Mohanlalview(View):

    def get(self,request,*args,**kwargs):

        data={"name":"mohanlal","age":70,"total_movies":150}

        return render(request,"mohan_lal.html",data)
     

