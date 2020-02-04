import json
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from weasyprint import HTML
from .models import Product, Orders, TotalOrders
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html", {})


@login_required
def home_menu(request):
    product_list = Product.objects.all()
    context = {'products': product_list}
    return render(request, "home_menu.html", context)


@login_required
def orders(request):
    context = {}
    return render(request, "orders.html", context)


@login_required
def order_placed(request):
    context = {}
    if request.method == "POST":
        print('hey')
        get_value = request.body
        dict = json.loads(get_value)
        ls=[]
        for item in dict:
            obj = TotalOrders.objects.create(title=item['Title'], quantity=item['Quantity'], price=item['Price'],
                                             total_price=item['Total_Price'])
            ls.append(obj)
        Orders.objects.create(user=request.user, orders=ls)
    return render(request, "order_placed.html", context)


@login_required
def html_to_pdf_view(request):
    data = Orders.objects.filter(user=request.user).latest('id')
    data = data.orders
    sum = 0
    for order in data:
        sum += order.total_price

    html_string = render_to_string('invoice.html', {'data': data, "sum": sum, "user": request.user})
    html = HTML(string=html_string)
    html.write_pdf(target='invoice.pdf')

    fs = FileSystemStorage('')
    with fs.open('invoice.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attatchment; filename="invoice.pdf"'
        return response
    return response

