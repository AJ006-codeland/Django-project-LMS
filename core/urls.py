from django.urls import path 
from core.views import HomePageView,TeacherCreateView,TeacherListView, TeacherDeleteView, TeacherDetailView, TeacherUpdateView
urlpatterns =[
    path('',HomePageView.as_view, name='home'),
    path('teacher/create/', TeacherCreateView.as_view(), name= 'teacher.create'),
    path('teacher/list/', TeacherListView.as_view(), name='teacher.index'),
    path('teacher/<int:pk>/detail/', TeacherDetailView.as_view(), name= 'teacher.detail'),
    path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name= 'teacher.delete'),
    path('teacher/<int:pk>/update/', TeacherUpdateView.as_view(), name= 'teacher.update'),
]