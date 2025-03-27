from django.urls import path
from django.urls import include
from .views import HelloWorld
from .views import ContactListView
from .views import  Students


urlpatterns = [

path('hello/', HelloWorld.as_view(), name='hello_world'),
path('contact/', ContactListView.as_view(), name='contact_new'),
path('students/', Students.as_view(), name='list_student'),

# Include exam-related URLs
path('api/exam/', include('api.exam_urls')),

]


