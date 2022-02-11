from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.getlist('sort')
    if sort:
        if sort[0] == 'name':
            phones_objects = Phone.objects.order_by('name')
        if sort[0] == 'min_price':
            phones_objects = Phone.objects.order_by('price')
        if sort[0] == 'max_price':
            phones_objects = Phone.objects.order_by('-price')
    else:
        phones_objects = Phone.objects.all()

    phones_list = [{'name': ph_o.name, 'price': ph_o.price, 'image': ph_o.image, 'slug': ph_o.slug} for ph_o in phones_objects]
    context = {'phones': phones_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product_obj = Phone.objects.filter(slug=slug)[0]
    context = {'phone': product_obj}
    return render(request, template, context)
