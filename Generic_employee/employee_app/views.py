from django.urls import reverse_lazy
from .forms import EmployeeForm
from .models import Employee
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.

class EmployeeView(ListView):
    model = Employee
    paginate_by = 2
    fields = '__all__'   

class AddEmployee(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('showemployee_url')

    
class UpdateEmployee(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('showemployee_url')
    

class DeleteEmployee(DeleteView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('showemployee_url')
    
    
    
    