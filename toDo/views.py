from django.shortcuts import render, HttpResponseRedirect
from .models import ToDoList
from .forms import ToDoChecked, AddToDoForm
# Create your views here.


def deleteToDo(request, todo_id):
    print('id of the to do is: ', todo_id)
    toDoItem = ToDoList.objects.get(id=todo_id)
    toDoItem.delete()
    return HttpResponseRedirect('/')


def main_list_view(request):
    try:
        full_list = ToDoList.objects.all()
    except Content.DoesNotExist:
        full_list = None
    if request.method == 'POST':
        print("getting somewhere")
    # form = ToDoChecked()
    # if request.method == 'POST':
    #     form = ToDoChecked(request.POST)
    #     print(request.POST.get('name'))
    #     test = full_list.get(task='test 2')
    #     print(test.id)
    #     print(form)
        # Product.objects.create(**my_form.cleaned_data)
        # form = ToDoChecked()
    add_form = AddToDoForm(request.POST or None)
    if add_form.is_valid():
        print(add_form.cleaned_data)
        ToDoList.objects.create(**add_form.cleaned_data)
        add_form = AddToDoForm()
    context = {
        'full_list': full_list,
        'add_form': add_form
    }
    return render(request, 'index.html', context)


# def product_form_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#             my_form = RawProductForm()
#     context = {'form': my_form}
#     return render(request, "products/product_create.html", context)
