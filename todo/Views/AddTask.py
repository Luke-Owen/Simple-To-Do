from django.shortcuts import redirect, render
from todo.Forms.UserInputForm import UserInputForm
def add_task(request):
    if request.method == "POST":
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserInputForm()

    return render(request, "todo/addtask.html", {'form': form})
