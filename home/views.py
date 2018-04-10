from django.shortcuts import render, get_object_or_404
from django.views import View

from . import models
from . import forms

from staff import models as staff_model

#index
class Home(View):
    template_name = 'home/index.html'

    def get(self, request):

        products = staff_model.Product.objects.all()

        variables = {
            'products': products,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        pass


#product detail
class ProductDetail(View):
    template_name = 'home/product-detail.html'

    def get(self, request, product_id):
        product = get_object_or_404(staff_model.Product, pk=product_id)

        variables = {
            'product': product,
        }

        return render(request, self.template_name, variables)

    def post(self, request, product_id):
        pass



#search
class Search(View):
    template_name = 'home/search.html'

    def get(self, request):

        variables = {

        }

        return render(request, self.template_name, variables)

    def post(self, request):
        search_query = request.POST.get('query_text')

        variables = {
            'search_query': search_query,
        }

        return render(request, self.template_name, variables)

