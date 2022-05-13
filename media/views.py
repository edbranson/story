from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from .models import Media
from entries.models import Entry
from .forms import MediaForm 
from django.contrib import messages

# Create your views here.


class MediaCreate(View):

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

class MediaList(View):

    def get(self, request, col):  
        sortby = col
        media = Media.objects.all()
        entries = Entry.objects.all()
        if sortby != 'list':
            media = media.order_by(sortby)            
      

        context = {'media': media, 'entries': entries,}
        return render(request, "media/media_list.html", context)

class MediaEdit(View):
    
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

class MediaSelect(View):
    
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

class MediaDelete(View):
        
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