from django.shortcuts import render
from  . forms import SearchForm ,SearchModelForm
from django.forms import formset_factory,modelform_factory,modelformset_factory
from .models import Blog




def formset_view(request):
    TextFormset = modelformset_factory(Blog , fields=['user' , 'title']  )
    formset = TextFormset(request.POST or None, 
                          queryset= Blog.objects.filter(user=request.user).filter(id__gt = 10) )
    if formset.is_valid():
        for form in formset:
            obj = form.save(commit=False)
            obj.title = "This is title"
            obj.save()
            
        print("allllllllllllllllllllllll")
        print(formset.cleaned_data)
    context = {
        "formset" : formset
    }
    return render(request,"blog/form_set.html",context)


# def formset_view(request):
#     TextFormset = modelformset_factory(Blog , fields=['user' , 'title']  )
#     formset = TextFormset(request.POST or None)
#     if formset.is_valid():
#         for form in formset:
#             obj = form.save(commit=False)
#             obj.title = "This is title"
#             obj.save()
            
#         print("allllllllllllllllllllllll")
#         print(formset.cleaned_data)
#     context = {
#         "formset" : formset
#     }
#     return render(request,"blog/form_set.html",context)




# def formset_view(request):
#     TextFormset = formset_factory(SearchForm , extra=2)
#     formset = TextFormset(request.POST or None)
#     if formset.is_valid():
#         print("allllllllllllllllllllllll")
#         print(formset.cleaned_data)
#     context = {
#         "formset" : formset
#     }
#     return render(request,"blog/form_set.html",context)


# Create your views here.
def home_view(request):
    # a = request.POST['q']
    # print(a)
    return render(request,"blog/form.html")

def home(request):
    # initial_dict = {
	# 	# "some_text" : 'Text'
	# }
    # form = SearchForm(request.POST or None, initial= initial_dict)
    context = {}
    # # if request.method =="POST":
    # #     print(request.POST.get('q'))
    # if form.is_valid():
    #     print(form.cleaned_data)
    
    # if request.method == "POST":
    #     form = SearchForm(data=request.POST)
    # elif request.method == "GET":
    #     form = SearchForm()
    form = SearchModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.title = "Some Random"
        obj.save()
    context["form"] = form
    return render(request, "blog/form.html" , context)