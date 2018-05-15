"""hyx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from ky.api.student import StudentAPI
from ky.api.teacher import TeacherAPI


from ky.excel import teacher_template,teacher_upload,student_template,student_upload

from django.http.response import HttpResponse
from django.conf.urls import handler404, handler500
from ky.views import index,dev

def test(request):
    return HttpResponse('hello world')

handler404 = 'ky.status.page404'
handler500 = 'ky.status.page500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('dev/', dev),
    path('v1/api/student/', include(StudentAPI.urls())),
    path('v1/api/teacher/', include(TeacherAPI.urls())),
    # path('v1/api/lesson/', include(Order.urls())),
    # path('v1/api/pro/', include(Pro.urls())),
    # path('v1/api/com/', include(Com.urls())),
    # path('v1/api/eng/', include(Eng.urls())),
    # path('v1/api/pol/', include(Pol.urls())),

    path('v1/excel/teacher_template',teacher_template),
    path('v1/excel/teacher_upload', teacher_upload),
    path('v1/excel/student_template', student_template),
    path('v1/excel/student_upload', student_upload),
    path('test/',test)
]
