from django.views import generic
from .models import MenuItem


class MenuListView(generic.ListView):
    # variables name must be spelled the same as the model
    queryset = MenuItem.objects.order_by("meal")
    template_name = "index.html"

    def get_context_data(self):
        context = {
            "meals": ["pizza", "pasta", "salad"],
            "ingredients": [
                "tomato",
                "tomato",
            ],
        }
        return context


class MenuItemDetailView(generic.DetailView):
    model = MenuItem
    template_name = "menu_item_detail.html"
