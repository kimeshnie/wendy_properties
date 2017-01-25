from django.contrib import admin
from .models import Leads
from .models import Listings
from .models import Agents


def upload_agent(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Agents.objects.get(pk=course_id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')

class personadmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cellphone', 'email', 'model_pic')  

def upload_listing(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Listings.objects.get(pk=course_id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')
 

class listingsdisplay(admin.ModelAdmin):
    list_display = ('price', 'bedrooms', 'heading', 'desc', 'suburb', 'agent', 'model_pic', 'featured')   

admin.site.register(Agents, personadmin)
admin.site.register(Listings, listingsdisplay)
admin.site.register(Leads)
