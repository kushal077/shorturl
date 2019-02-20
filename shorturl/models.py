from django.db import models
from shorturl.utils import code_generator , create_shortcode
# Create your models here.
# manager.
#class shorturlsmanager(models.Model):
#    def all(self,*args,**kwargs):
#        qs = super(shorturlsmanager,self).all(*args,**kwargs).filter(active=False)
#        #qs=qs_main.filter(active=False)
#        return qs

class shorturls(models.Model):
    url= models.CharField(max_length=300)
    short=models.CharField(max_length=14, unique=True ,blank=True , null=False)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    #    objects=shorturlsmanager()
    #some_random =shorturlsmanager()
    
    def save(self ,*args ,**kwargs):
        if self.short== None or self.short== "":
            self.short=code_generator()
        super(shorturls,self).save(*args ,**kwargs)


    def __str__(self):
        return self.url

    def __unicode__(self):
        return self.url


