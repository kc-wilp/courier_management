from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


customers = [

{
    'customer_id': 1,
    'customer_name': "Kaushik",
    'customer_email': 'kaushik@email.com'

},
{
    'customer_id': 2,
    'customer_name': "Ram",
    'customer_email': 'ram@email.com'

}

]

def home(request):

    context = {
        'customers': customers
    }

    return render(request, 'courier_mgt/index.html', context)
