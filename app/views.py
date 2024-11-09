from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'my Name IS K RajendRa Prasad','dt':dt,"c":1}
 
    return render(request,'filters.html',d)
def swap(request):
    d={'data':'My naMe iS k RAjendra pRASad','l':[1,2,3,4,5]}
    d['l'].append('rajendra')
    return render(request,'swap.html',d)
