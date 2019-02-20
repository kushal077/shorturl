from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from django.views import View
from .models import shorturls
from .forms import submiturlform



class homeview(View):
    def get(self,request,*args, **kwargs):
        the_form=submiturlform()
        context={"title":"submit url", "form":the_form }
        return render(request,"shorturl/shorturl.html",context)

    def post(self,request,*args,**kwargs):
        form=submiturlform(request.POST)
        context={"title":"kirr.co","form":form}
        templates="shorturl/shorturl.html"
        if form.is_valid():
            n_url=form.cleaned_data.get("url")
            obj , created = shorturls.objects.get_or_create(url=n_url)
            context={"object":obj, "created" : created, }
            if created:
                templates="shorturl/success.html"
            else:
                templates="shorturl/already.html"
        return render(request,templates,context)


class urlsho(View):
    def get(self,request,*args, short=None, **kwargs):
        obj= get_object_or_404(shorturls, short=short)
        return HttpResponseRedirect(obj.url)

    def post(self,request,*args,**kwargs):
        return HttpResponse()
