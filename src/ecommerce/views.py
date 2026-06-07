from django.shortcuts import render, get_object_or_404
from .models import ProductModel
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ProductModelForm



def product_model_list_view(request):
    qs = ProductModel.objects.all()
    print(qs)

    context = {
        "products" : qs,
        "user" : request.user
    }

    template = "ecommerce/list-view.html"

    return render(request, template, context)

def product_model_detail_view(request, id):
    instance = get_object_or_404(ProductModel, id=id)

    context = {
        "product" : instance,
    }

    template = "ecommerce/detail-view.html"

    return render(request, template, context)


def product_model_create_view(request):
    form = ProductModelForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data)
        instance.save()
        messages.success(request, "Producto creado exitosamente")
        return HttpResponseRedirect("/ecommerce/products/{product_id}/".format(product_id=instance.id))

    context = {
        "form" : form,
    }

    template = "ecommerce/create-view.html"

    return render(request, template, context)

def product_model_update_view(request, product_id = None):
    instance = get_object_or_404(ProductModel, id=product_id)
    form = ProductModelForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data)
        instance.save()
        messages.success(request, "Producto actualizado exitosamente")
        return HttpResponseRedirect("/ecommerce/products/{product_id}/".format(product_id=instance.id))

    context = {
        "form" : form,
    }

    template = "ecommerce/update-view.html"

    return render(request, template, context)

def product_model_delete_view(request, product_id = None):
    instance = get_object_or_404(ProductModel, id=product_id)
    

    if request.method == "POST":
        print("Deleting...")
        instance.delete()
        messages.success(request, "Producto eliminado exitosamente")
        return HttpResponseRedirect("/ecommerce/")

    context = {
        "product" : instance,
    }

    template = "ecommerce/delete-view.html"

    return render(request, template, context)