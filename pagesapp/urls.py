from  django.urls import  path
from .views import HomePageView, AboutPageView,ResumePageView,ServesPageView

urlpatterns = [
    path('', HomePageView.as_view(),name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('resume/', ResumePageView.as_view(), name='resume'),
    path('serves/', ServesPageView.as_view(), name='serves')
]