from .models import Category

def categories(request):
    """This context processor adds categories to every template."""
    return {'categories': Category.objects.all()}
