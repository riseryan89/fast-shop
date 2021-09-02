from app.models import Category


def left_menu(request):
    category = Category.objects.all()
    return {"category": category}
