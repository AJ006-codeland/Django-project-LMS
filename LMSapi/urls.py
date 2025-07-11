from django.urls import path
from LMSapi.views import TeacherApiView, TeacherApiListCreateView

urlpatterns= [
    # teacher API
    path('teacher/<int:pk>/detail/', TeacherApiView.as_view(),name='details'),
    path('teacher/<int:pk>/update/', TeacherApiView.as_view(),name='api.teacher.update'),
    path('teacher/<int:pk>/edit/', TeacherApiView.as_view(),name='api.teacher.edit'),
    path('teacher/<int:pk>/delete/', TeacherApiView.as_view(), name='api.teacher.delete'),
    # teacher api:for list and create
    path('teacher/list/', TeacherApiListCreateView.as_view(), name='api.teacher.list'),
    path('teacher/create/', TeacherApiListCreateView.as_view(), name='api.teacher.create'),
]