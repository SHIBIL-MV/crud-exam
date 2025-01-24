from django.shortcuts import render,redirect
from django.views.generic import View
from leadapp import forms
from leadapp.models import LEAD

# Create your views here.


class CreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=forms.LeadForm()

        return render(request,"lead_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=forms.LeadForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            LEAD.objects.create(

                name=data.get("name"),
                email=data.get("email"),

                phone_number=data.get("phone_number"),

                status=data.get("status"),

                source=data.get("source"),



            )

            return redirect("lead-add")
        
        return render(request,"lead_add.html",{"form":form_instance})
    
class DetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=LEAD.objects.get(id=id)

        return render(request,"lead_detail.html",{"data":qs})
class DeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=LEAD.objects.get(id=id).delete()

        return redirect("all")
    
class ListView(View):


    def get(self,request,*args,**kwargs):

        qs=LEAD.objects.all()

        return render(request,"lead_list.html",{"data":qs})
    

class UpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        lead_obj=LEAD.objects.get(id=id)

        lead_dict={

            "name":lead_obj.name,
            "email":lead_obj.email,
            "phone_number":lead_obj.phone_number,
            "status":lead_obj.status,

            "source":lead_obj.source,

        }

        form_instance=forms.LeadForm(initial=lead_dict)



        return render(request,"lead_update.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        form_data=request.POST

        form_instance=forms.LeadForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            LEAD.objects.filter(id=id).update(**data)

            return redirect("all")
        
        return render(request,"lead_update.html",{"form":form_instance})
