from django.shortcuts import render
from django.views import View

# Create your views here.

class LandingPageView(View):
    def get(self,request):
        return render(request,'landing.html',{})

class AboutUsPageView(View):
    def get(self,request):
        return render(request,'about_us.html',{})


class CoursesPageView(View):
    def get(self,request):
        return render(request,'courses.html',{})


class PromotionsPageView(View):
    def get(self,request):
        return render(request,'promotions.html',{})


class HostelServicesPageView(View):
    def get(self,request):
        return render(request,'hostelservice.html',{})        


class ContactUsPageView(View):
    def get(self,request):
        return render(request,'contactus.html',{})        

