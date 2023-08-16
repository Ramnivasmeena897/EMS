from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePageView,name='home'),  path('uregister/',views.userRegistrationView,name='uregistration'),
    path('insert/',views.insertUserDataBase,name='userinsert'),
    path('userloginpage/',views.userLoginPage,name='userloginpage'),
    path('ulogin/',views.uLogin,name='ulogin'),
    #========================================================================
    path('aregister/',views.adminRegistrationView,name='aregistration'),
    path('admininsert/',views.insertAdminDataBase,name='admininsert'),
    path('adminloginpage/',views.adminLoginPage,name='adminloginpage'),
    path('alogin/',views.aLogin,name='alogin'),
    #========================================================================
    path('enquiry/',views.enquiryView,name='enquiry'),
    path('enquiryinsert/',views.insertEnquiryDataBase,name='enquiryinsert'),
    #========================================================================
    path('showpage/',views.showPage,name='showpage'),
    path('editpage/<int:pk>/',views.EditPage,name='editpage'),
    path('update/<int:pk>/',views.UpdateData,name='update'),
    path('delete/<int:pk>/',views.DeleteData,name='delete'),
    
    
    
    #======extra admin details=====
    path('admin1/',views.Admin1,name='admin1'),
    path('user1',views.user1,name='user1'),
    
    
    
]