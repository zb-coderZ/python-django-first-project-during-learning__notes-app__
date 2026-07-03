from django.shortcuts import render
from .models import Note,store
from django.shortcuts import get_object_or_404
from .forms import notes_forms

# def notes(re
# quest):
#     return render(request,'testing_notes.html')

def notes(request):
    all_notes=Note.objects.all()
    return render(request,'testing_notes.html',{'notes':all_notes})

def notes_detail(request,id):
     note=get_object_or_404(Note,pk=id)
     return render(request,'note_detail.html',{'note':note})

def forms_concept(request):
     stores=None
     form=notes_forms()  
     
     if request.method=='POST':
          form=notes_forms(request.POST)
     if form.is_valid():
          notes_variety=form.cleaned_data['notes_variety']
          stores=store.objects.filter (note_varities=notes_variety)     
     else:
          form=notes_forms()     
     return render(request, 'forms.html',{'stores':stores, 'form':form})