from django.urls import path 
from core.views import HomePageView,TeacherCreateView,TeacherListView
urlpatterns =[
    path('',HomePageView.as_view, name='home'),
    path('teacher/create/', TeacherCreateView.as_view(), name= 'teacher.create'),
    path('teacher/list/', TeacherListView.as_view(), name='teacher.index')
]