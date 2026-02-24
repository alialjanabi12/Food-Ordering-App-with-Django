from django.views import generic
from .models import MEAL_TYPE, MenuItem


class MenuListView(generic.ListView):
    # variables name must be spelled the same as the model
    queryset = MenuItem.objects.order_by("meal")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context


class MenuItemDetailView(generic.DetailView):
    model = MenuItem
    template_name = "menu_item_detail.html"
