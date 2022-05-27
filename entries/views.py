from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Media, Entry
from profiles.models import Tag, Profile
from .forms import EntryForm
from django.contrib import messages

# Create your views here.
class Home(View):

    def get(self, request):
        return redirect('media-list', 'list')

        
class EntryCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        media = get_object_or_404(Media, pk=kwargs['med'])
        data = {"userId": request.user.id, "mediaId": media.id,}
        form = EntryForm(userId=request.user.id)
        context = {'form': form, 'media': media, 'data': data,}
        return render(request, "entries/entry_create.html", context)


    def post(self, request, *args, **kwargs):
        media = get_object_or_404(Media, pk=kwargs['med'])
        entries_ratings = Entry.objects.filter(media=kwargs['med']).values_list('rating', flat=True)
        entrieslen = len(entries_ratings)
        ratingsum = sum(entries_ratings)
        data = {"userId": request.user.id, "mediaId": media.id,}
        form = EntryForm(request.POST, userId=request.user.id)
        context = {'form': form, 'media': media, 'data': data,}
        if form.is_valid():
            entry_form_save = form.save(commit=False)
            date_started = entry_form_save.date_started
            date_finished = entry_form_save.date_finished
            rating = entry_form_save.rating
            status = entry_form_save.status
            if status != "QUIT":
                if date_finished:
                    entry_form_save.status = "FINISHED"
                elif date_started:
                    entry_form_save.status = "STARTED"
                else:
                    entry_form_save.status = "WISHLIST"
            if rating == 0:
                if ratingsum > 0:
                    media.ave_rating = ratingsum / entrieslen
                    media.save()
            else:
                entrieslen = entrieslen + 1
                ratingsum = ratingsum + rating
                media.ave_rating = ratingsum / entrieslen
                media.save()    

            entry_form_save.save()
            form.save_m2m()
           

            return redirect('media-list', 'list')   
        print(form.errors)    
        return render(request, "entries/entry_create.html", context)


class EntryList(View):

    def get(self, request, col):  
        sortby = col
        entry = Entry.objects.all()
        # if sortby != 'list':
        #     entry = entry.order_by(sortby)            
        userList = Profile.objects.all()

        context = {'entry': entry, 'users': userList}
        return render(request, "entries/entry_list.html", context) 

class EntryEdit(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    def get(self, request, pk): 
        entry = get_object_or_404(Entry, pk=pk)
        form = EntryForm(instance=entry, userId=request.user.id)
        context = {'form': form, 'entry': entry,}
        return render(request, 'entries/entry_detail.html', context)

    def post(self, request, pk): 
        entry = get_object_or_404(Entry, pk=pk)
        media = get_object_or_404(Media, pk=entry.media_id)
        entries_ratings = Entry.objects.filter(media=entry.media_id).values_list('rating', flat=True)
        entrieslen = len(entries_ratings)
        ratingsum = sum(entries_ratings)
        form = EntryForm(request.POST, instance=entry, userId=request.user.id)
        context = {'form': form, 'entry': entry,}
        if form.is_valid():
            entry_form_save = form.save(commit=False)
            date_started = entry_form_save.date_started
            date_finished = entry_form_save.date_finished
            rating = entry_form_save.rating
            status = entry_form_save.status
            if status != "QUIT":
                if date_finished:
                    entry_form_save.status = "FINISHED"
                elif date_started:
                    entry_form_save.status = "STARTED"
                else:
                    entry_form_save.status = "WISHLIST"
            if rating == 0:
                if ratingsum > 0:
                    media.ave_rating = ratingsum / entrieslen
                    media.save()
            else:
                entrieslen += entrieslen
                ratingsum = ratingsum + rating
                media.ave_rating = ratingsum / entrieslen
                media.save()                        
            entry_form_save.save()
            form.save_m2m()

            
            messages.success(request, "Entry was updated successfully!") 
            return redirect('media-list', 'list')
        print(form.errors)   
        return render(request, 'entries/entry_detail.html', context)  

class EntryDelete(LoginRequiredMixin, View):
    login_url = '/login/'   
    def post(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()
        messages.success(request, "Entry was deleted!")
        return redirect('media-list', 'list') 


class EntrySelect(View):

    def get(self, request, med):
        entries = Entry.objects.filter(media=med)
        print(entries)
        context = {'entries': entries}
        return render(request, 'entries/entry_select.html', context)               