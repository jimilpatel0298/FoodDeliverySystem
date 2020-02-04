import json
import io
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from weasyprint import HTML

from .models import Product, Orders, TotalOrders
from django.template.loader import render_to_string


def home(request):
    return render(request, "home.html", {})


def home_menu(request):
    product_list = Product.objects.all()
    context = {'products': product_list}
    return render(request, "home_menu.html", context)


def orders(request):
    context = {}
    return render(request, "orders.html", context)


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


# from io import BytesIO
# from django.http import HttpResponse
# from django.template.loader import get_template
# import xhtml2pdf.pisa as pisa
#
#
# class Render:
#
#     @staticmethod
#     def render(path: str, params: dict):
#         template = get_template(path)
#         html = template.render(params)
#         response = BytesIO()
#         pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
#         if not pdf.err:
#             return HttpResponse(response.getvalue(), content_type='application/pdf')
#         else:
#             return HttpResponse("Error Rendering PDF", status=400)
#
#
# # def html_to_pdf_view(request):
# #     data = Orders.objects.filter(user=request.user).latest('id')
# #     data = data.orders
# #     sum = 0
# #     for order in data:
# #         sum += order.total_price
# #     return render(request,"invoice.html", {'data': data, "sum": sum})

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

