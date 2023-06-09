from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.student_detail_page,name='home'),
    path('add_data/',views.add_data,name='add_data'),
    path('stu_insert/',views.stu_insert,name='stu_insert'),
    # path('injest_data/',views.injest_data,name='injest'),
    # path('pre_conform/',views.student_pre_conform,name='Pre-conform'),
    # path('conform/',views.student_conform,name='conform'),    
]