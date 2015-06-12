from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from app1.models import Book, Library
from forms import BookForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.signals import request_finished
from django.dispatch import receiver

# Create your views here.


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")


def listing(request):
    """
    List all instances of the model Book with pagination.
    :author Nourhan Fawzy:
    :param request:
    :return:
    """
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 3)

    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render_to_response('list.html', {"books": books})


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'year', 'about', 'library']


class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'year', 'about', 'library']
    template_name_suffix = '_update_form'


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')


class BookListView(ListView):
    model = Book


    def get_queryset(self):
        """
        @comment: Library name is not passed in GET or POST data. 
        This was changed to pass the library ID in the url
        @author: Nader Alexan
        """
        # self.library = get_object_or_404(Library, name=self.args[5])
        return Book.objects.filter(library_id=self.kwargs['library_id'])

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super(BookListView, self).get_context_data(**kwargs)
    # Add in the publisher
        """
        @comment: You cannot use self.library because the class BookListView does not
        have library as an instance variable.
        @author: Nader Alexan
        """
        library = get_object_or_404(Library, id=self.kwargs['library_id'])
        context['library'] = library
        return context
    


class BookDetailView(DetailView):
	model = Book

	def get_context_data(self, **kwargs):
		context = super(BookDetailView, self).get_context_data(**kwargs)
		return context



class LibraryCreate(CreateView):
	model = Library
	fields = ['name','location']


class LibraryUpdate(UpdateView):
	model = Library
	fields = ['name','location']
	template_name_suffix = '_update_form'


class LibraryDelete(DeleteView):
    model = Library
    success_url = reverse_lazy('library-list')



class LibraryListView(ListView):
    model = Library
    
    def get_context_data(self, **kwargs):
		context = super(LibraryListView, self).get_context_data(**kwargs)
		return context


class LibraryDetailView(DetailView):
	model = Library

	def get_context_data(self, **kwargs):
		context = super(LibraryDetailView, self).get_context_data(**kwargs)
		return context


"""

class BookFormView(View):
	form_class = BookForm
	initial = {}
	template_name = 'book_form.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request, self.template_name, {'form':form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()

			return render_to_response('app1/book_list.html', {'object_list':Book.objects.all()})

"""



