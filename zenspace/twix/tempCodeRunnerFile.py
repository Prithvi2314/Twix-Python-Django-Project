def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request , 'profile_list.html', {'profiles':profiles})
    else:
        messages.success(request,("You Must Be Logged In To View This Page..."))
        return redirect('twix_list.html')
