from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate, logout
from .models import Profile, Tag
from .forms import ProfileForm, TagForm, CustomUserCreationForm 
from django.contrib import messages


# Create your views here.
class RegisterUser(View):
    
    def get(self, request):
        page = 'register'
        form = CustomUserCreationForm()
        context = {'page':page, 'form': form,}
        return render(request, 'login_register.html', context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
    
            messages.success(request, 'User account was created!') 

            login(request, user)
            profileId=Profile.objects.last().id
            return redirect('profile-edit',profileId)
        else:    
            messages.error(request, 'User account Failed?!') 

        return render(request, 'login_register.html')  

class LoginUser(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home') 
        else:
            page = 'login'      
            return render(request, 'login_register.html')

    def post(self, request):
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist!') 

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User name or password is incorrect')
            return render(request, 'login_register.html')

class LogoutUser(View):
    def get(self, request):
        logout(request)
        messages.error(request, 'User was logged out') 
        return redirect('login')




class ProfileCreate(View):

    def get(self, request):
        form = ProfileForm()
        context = {'form': form}
        return render(request, "profiles/profile_create.html", context)

    def post(self, request):
        form = ProfileForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('profile-list')
        return render(request, "profiles/profile_create.html", context)    
               
class ProfileList(View):

    def get(self, request):
        profiles = Profile.objects.all()
        context = {'profiles': profiles}
        return render(request, "profiles/profile_list.html", context)



class ProfileEdit(View):
    
    def get(self, request, pk): 
        profile = get_object_or_404(Profile, pk=pk)
        form = ProfileForm(instance=profile)
        context = {'form': form, 'profile': profile,}
        return render(request, 'profiles/profile_detail.html', context)

    def post(self, request, pk): 
        profile = get_object_or_404(Profile, pk=pk)
        form = ProfileForm(request.POST, instance=profile)
        context = {'form': form, 'profile': profile,}
        if form.is_valid():
            form.save()
            messages.success(request, "Profile was updated successfully!")
            return redirect('profile-list')
        return render(request, 'profiles/profile_detail.html', context)    

class ProfileDelete(View):
          
    def post(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        profile.delete()
        messages.success(request, "Profile was deleted!")
        return redirect('profile-list')




class TagList(View):
    def get(self, request):
        tag = Tag.objects.filter(user=request.user.id)
        context = {'tag': tag}
        return render(request, "profiles/tag_list.html", context)

class TagCreate(View):

    def get(self, request):
        form = TagForm()
        data = {"user": request.user,}

        context = {'form': form, 'data': data}
        return render(request, "profiles/tag_create.html", context)

    def post(self, request):
        form = TagForm(request.POST)
        data = {"user": request.user.id,}
        context = {'form': form, 'data': data,}
        if form.is_valid():
            form.save()
            return redirect('tag-list')
   
        print(form.errors)    
        return render(request, "profiles/tag_create.html", context)    

class TagEdit(View):
    
    def get(self, request, pk): 
        tag = get_object_or_404(Tag, pk=pk)
        form = TagForm(instance=tag)
        context = {'form': form, 'tag': tag,}
        return render(request, 'profiles/tag_detail.html', context)

    def post(self, request, pk): 
        tag = get_object_or_404(Tag, pk=pk)
        form = TagForm(request.POST, instance=tag)
        context = {'form': form, 'tag': tag,}
        if form.is_valid():
            form.save()
            messages.success(request, "Tag was updated successfully!")
            return redirect('tag-list')
        return render(request, 'profiles/tag_detail.html', context)        


class TagDelete(View):
          
    def post(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        tag.delete()
        messages.success(request, "Tag was deleted!")
        return redirect('tag-list')
    
