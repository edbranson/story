from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Media
from entries.models import Entry
from .forms import MediaForm, MediaSearchForm 
from django.contrib import messages

# Create your views here.


class MediaCreate(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        form = MediaForm()
        context = {'form': form}
        return render(request, "media/media_create.html", context)

    def post(self, request):
        form = MediaForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('media-list', 'list')
        return render(request, "media/media_create.html", context) 

class MediaCreateFor(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        form = MediaForm()
        context = {'form': form}
        return render(request, "media/media_create_for_entry.html", context)

    def post(self, request):
        form = MediaForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            media = Media.objects.last()
            return redirect('entry-create', med=media.id)
        return render(request, "media/media_create_for_entry.html", context) 

class MediaCloneFor(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        # clone = {}
        clone = get_object_or_404(Media, pk=kwargs['pk'])
        clone.media_type = kwargs['format']
        form = MediaForm()
        context = {'form': form, 'clone': clone,}
        return render(request, "media/media_clone_for_entry.html", context)

    def post(self, request, *args, **kwargs):
        form = MediaForm(request.POST)
        # clone = get_object_or_404(Media, pk=kwargs['pk'])
        # context = {'form': form, 'clone': clone}
        context = {'form': form,}
        if form.is_valid():
            form.save()
            media = Media.objects.last()
            return redirect('entry-create', med=media.id)
        return render(request, "media/media_clone_for_entry.html", context) 


class MediaList(View):

    def get(self, request, col):  
        sortby = col
        media = Media.objects.all()
        media_total_count = media.count()
        count = {'total':media_total_count,}

        entries = Entry.objects.all()
        if sortby != 'list':
            media = media.order_by(sortby)            
      

        context = {'media': media, 'entries': entries, 'count': count}
        return render(request, "media/media_list.html", context)

class MediaSearch(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request):
        form = MediaSearchForm()
        context = {"form": form}
        return render(request, "media/media_search.html", context)

    def post(self, request):
        form = MediaSearchForm(request.POST)
        title = request.POST["title"]
        type = request.POST["media_type"]
        match = {"title": False, "type": False}
        source = Media.objects.filter(title__iexact=title)
        context = {"form": form, "source": source, "title": title, "type": type, "match": match}
        if source:
            match["title"] = True
            if source[0].media_type == type and len(source) == 1:
                match["type"] = True
                return redirect('entry-create', med=source[0].id)
            else:
                for x in source:
                    if x.media_type == type:
                        match['type'] = True
                        return redirect('entry-create', med=x.id)   
            return render(request, 'media/media_list_for_entry.html', context)
        else:
            return render(request, 'media/media_create_for_entry.html', context)
        return render(request, "media/media_search.html", context)


# class MediaListForEntry(LoginRequiredMixin,View):
#     login_url = '/login/'
#     def get(self, request, *args, **kwargs):  
#         media = Media.objects.all()
#         entries = Entry.objects.all()
#         print("mediaListForEntry")

#         context = {'media': media, 'entries': entries,}
#         return render(request, "media/media_list_for_entry.html", context)        

class MediaEdit(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, pk): 
        media = get_object_or_404(Media, pk=pk)
        form = MediaForm(instance=media)
        context = {'form': form, 'media': media,}
        return render(request, 'media/media_detailOld.html', context)

    def post(self, request, pk): 
        media = get_object_or_404(Media, pk=pk)
        form = MediaForm(request.POST, instance=media)
        context = {'form': form, 'media': media,}
        if form.is_valid():
            form.save()
            messages.success(request, "Media was updated successfully!") 
            return redirect('media-list', 'list')
        return render(request, 'media/media_detailOld.html', context)  

class MediaSelect(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, pk): 
        media = get_object_or_404(Media, pk=pk)
        form = MediaForm(instance=media)
        context = {'form': form, 'media': media,}
        return render(request, 'media/media_select.html', context)

    def post(self, request, pk): 
        media = get_object_or_404(Media, pk=pk)
        form = MediaForm(request.POST, instance=media)
        context = {'form': form, 'media': media,}
        if form.is_valid():
            form.save()
            messages.success(request, "Media was updated successfully!") 
            return redirect('media-list', 'list')
        messages.error(request, "Validation failed")
        print("form did not validate")    
        print(form.errors)
        return render(request, 'media/media_select.html', context)  

class MediaDelete(LoginRequiredMixin, View):
        
    def post(self, request, pk):
        media = get_object_or_404(Media, pk=pk)
        media.delete()
        messages.success(request, "Media was deleted!")
        return redirect('media-list', 'list')        

class Tagged(View):

    def get(self, request):
        media = get_object_or_404(Media, pk=pk)
        tags = Tag.objects.filter(user=request.user.id)        
        tagged = Tagged.objects.filter(tag=tags, media=media.id)
        form = TaggedCreateForm(instance=tagged or None)
        context = {'form': form, 'tags': tags}
        return render(request, 'entries/entry_create.html', context)        