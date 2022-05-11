from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView
from .models import Media, Entry
from profiles.models import Tag, Profile
from .forms import EntryForm
from django.contrib import messages

# Create your views here.
class Home(View):

    def get(self, request):
        return render(request, "home.html")

        
class EntryCreate(CreateView):

    def get(self, request, *args, **kwargs):
        media = get_object_or_404(Media, pk=kwargs['med'])
        data = {"userId": request.user.id, "mediaId": media.id,}
        form = EntryForm(userId=request.user.id)
        context = {'form': form, 'media': media, 'data': data,}
        return render(request, "entries/entry_create.html", context)


    def post(self, request, *args, **kwargs):
        media = get_object_or_404(Media, pk=kwargs['med'])
        data = {"userId": request.user.id, "mediaId": media.id,}
        form = EntryForm(request.POST, userId=request.user.id)
        context = {'form': form, 'media': media, 'data': data,}
        if form.is_valid():
            entry_form_save = form.save(commit=False)
            date_started = entry_form_save.date_started
            date_finished = entry_form_save.date_finished
            status = entry_form_save.status
            if status != "QUIT":
                if date_finished:
                    entry_form_save.status = "FINISHED"
                elif date_started:
                    entry_form_save.status = "STARTED"
                else:
                    entry_form_save.status = "WISHLIST"    
            entry_form_save.save()
            form.save_m2m()
           

            return redirect('entry-list', 'list')   
        print(form.errors)    
        return render(request, "entries/entry_create.html", context)


class EntryList(View):

    def get(self, request, col):  
        sortby = col
        entry = Entry.objects.all()
        if sortby != 'list':
            entry = media.order_by(sortby)            
        userList = Profile.objects.all()

        context = {'entry': entry, 'users': userList}
        return render(request, "entries/entry_list.html", context) 

class EntryEdit(UpdateView):
    
    def get(self, request, pk): 
        entry = get_object_or_404(Entry, pk=pk)
        form = EntryForm(instance=entry, userId=request.user.id)
        context = {'form': form, 'entry': entry,}
        return render(request, 'entries/entry_detail.html', context)

    def post(self, request, pk): 
        entry = get_object_or_404(Entry, pk=pk)
        form = EntryForm(request.POST, instance=entry, userId=request.user.id)
        context = {'form': form, 'entry': entry,}
        if form.is_valid():
            entry_form_save = form.save(commit=False)
            date_started = entry_form_save.date_started
            date_finished = entry_form_save.date_finished
            status = entry_form_save.status
            if status != "QUIT":
                if date_finished:
                    entry_form_save.status = "FINISHED"
                elif date_started:
                    entry_form_save.status = "STARTED"
                else:
                    entry_form_save.status = "WISHLIST"    
            entry_form_save.save()
            form.save_m2m()

            
            messages.success(request, "Entry was updated successfully!") 
            return redirect('entry-list', 'list')
        print(form.errors)
        print('trying to save')    
        return render(request, 'entries/entry_detail.html', context)  

class EntryDelete(View):
        
    def post(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()
        messages.success(request, "Entry was deleted!")
        return redirect('entry-list', 'list') 


class EntrySelect(View):

    def get(self, request, med):
        entries = Entry.objects.filter(media=med)
        print(entries)
        context = {'entries': entries}
        return render(request, 'entries/entry_select.html', context)               