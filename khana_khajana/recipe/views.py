from django.shortcuts import render
from .models import Receipe

# Create your views here.
def receipe(request):
    pass
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_discription = data.get('receipe_discription') # for normal text ,input text filed get values simeple
        receipe_image = request.FILES.get('receipe_image')       # for getting files /image use request.FILES
        print(receipe_name,receipe_discription,receipe_image )
        receipe_obj = Receipe(receipe_name=receipe_name, 
                              receipe_discription=receipe_discription, 
                              receipe_image=receipe_image)
        receipe_obj.save()
    return render(request, 'receipe.html')

def index(request):
    pass
    return render(request, 'index.html')