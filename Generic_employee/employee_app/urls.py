from django.urls import path
from . import views

urlpatterns = [
   path('add/',views.AddEmployee.as_view(), name='Employee_url'),
   path('show/',views.EmployeeView.as_view(), name='showemployee_url'),
   path('show/<int:page>/',views.EmployeeView.as_view(), name='showemployee_url'),
   path('update/<int:pk>/',views.UpdateEmployee.as_view(), name='update_url'),
   path('del/<int:pk>/',views.DeleteEmployee.as_view(), name='delete_url')
]

