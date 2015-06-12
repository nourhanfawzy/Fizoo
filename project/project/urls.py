from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required

from app1.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^about/', login_required(TemplateView.as_view(template_name="about.html"))),
    #url(r'^about/', AboutView.as_view()),
    #url(r'^about/', MyView.as_view()),
    #url(r'^about/', GreetingView.as_view()),
    #url(r'^about/', permission_required(GreetingView.as_view(greeting="G'day"))),
    url(r'^home', TemplateView.as_view(template_name="home.html")),

    url(
        r'^book-list/(?P<library_id>\d+)/$',
        BookListView.as_view(), name='book-list'),
    url(r'^book-form$', BookCreate.as_view(), name='book-form'),
	url(r'^(?P<pk>[-\w]+)/BookDetail$', BookDetailView.as_view(), name='book-detail'),
    url(r'^(?P<pk>[-\w]+)/BookUpdate$', BookUpdate.as_view(), name='book-update'),
   	url(r'^(?P<pk>[-\w]+)/BookDelete$', BookDelete.as_view(), name='book-delete'),



    url(r'^library-list$', LibraryListView.as_view(), name='library-list'),
    url(r'^library-form$', LibraryCreate.as_view(), name='library-form'),
    url(r'^(?P<pk>[-\w]+)/LibraryDetail$', LibraryDetailView.as_view(), name='library-detail'),
    url(r'^(?P<pk>[-\w]+)/LibraryUpdate$', LibraryUpdate.as_view(), name='library-update'),
    url(r'^(?P<pk>[-\w]+)/LibraryDelete$', LibraryDelete.as_view(), name='library-delete'),


    url(r'^book-list2$', listing, name='book-list2'),




)
