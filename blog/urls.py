from django.urls import path

from .views import ContactUsPageView, HostelServicesPageView, LandingPageView,AboutUsPageView,CoursesPageView,PromotionsPageView
urlpatterns = [
    path('',LandingPageView.as_view(),name='landing'),
    path('about_us/',AboutUsPageView.as_view(),name='about_us'),
    path('courses/',CoursesPageView.as_view(),name='courses'),
    path('promotions/',PromotionsPageView.as_view(),name='promotions'),
    path('hostelservice/',HostelServicesPageView.as_view(),name='hostelservice'),
    path('contactus/',ContactUsPageView.as_view(),name='contactus'),
    
]