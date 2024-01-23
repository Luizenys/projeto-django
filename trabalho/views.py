from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Shows
from .forms import ShowForm
from django.shortcuts import render, get_object_or_404


class IndexView(generic.ListView):
    template_name = 'trabalho/subpaginas/index.html'
    context_object_name = 'lista_de_shows'

    def get_queryset(self):
        return Shows.objects.filter(data__year=2017)


class ListaDeShows(generic.ListView):
    template_name = 'trabalho/listaShows.html'
    context_object_name = 'lista_de_shows'

    def get_queryset(self):
        return Shows.objects.all()

# -------------------------------------------------------------------


def menu(request):
    return render(request, 'trabalho/subpaginas/menu.html')


def footer(request):
    return render(request, 'trabalho/subpaginas/footer.html')


def cadastro(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['id'] == 0:
                show = Shows(local=cd['local'],
                            endereco=cd['endereco'],
                            data=cd['data'])
                show.save()
                return HttpResponseRedirect(reverse('trabalho:show', args=(show.id,)))
            else:
                show = get_object_or_404(Shows, pk=cd['id'])
                show.local = cd['local']
                show.endereco = cd['endereco']
                show.data = cd['data']
                show.save()
                return HttpResponseRedirect(reverse('trabalho:show', args=(show.id,)))
    else:
        form = ShowForm(initial={'id': 0, 'local': '', 'endereco': '', 'data': ''})

    return render(request, 'trabalho/cadastro.html', {'form': form})


def mostrarShow(request, show_id):
    show = get_object_or_404(Shows, pk=show_id)
    return render(request, 'trabalho/show.html', {'show': show, 'acao': 'agendado'})


def alterar(request):
    show = get_object_or_404(Shows, pk=request.POST['id'])
    form = ShowForm(initial={'id': show.id,
                                'local': show.local,
                                'endereco': show.endereco,
                                'data': show.data})
    return render(request, 'trabalho/cadastro.html', {'form': form})


def alterado(request, show_id):
    show = get_object_or_404(Shows, pk=show_id)
    return render(request, 'trabalho/show.html', {'show': show, 'acao': 'alterado'})


def remover(request):
    show = get_object_or_404(Shows, pk=request.POST['id'])
    form = ShowForm(initial={'id': show.id,
                                'local': show.local,
                                'endereco': show.endereco,
                                'data': show.data})
    show.delete()
    return render(request, 'trabalho/show.html', {'show': show, 'acao': 'removido'})
# -------------------------------------------------------------------

