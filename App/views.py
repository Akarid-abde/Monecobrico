from django.views.generic import DetailView
from django.shortcuts import render
from .models import Metiers
from django.views import generic
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request, 'MonEcoBrico/index.html', {'metiers': Metiers.objects.all()})


def privacy_policy(request):
    return render(request, 'MonEcoBrico/privacy_policy.html')


def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        tele = request.POST.get('tele')
        message = request.POST.get('message')
        form_data = {
            'nom': nom,
            'tele': tele,
            'message': message,
        }
        message = '''
        From:\t\t{}\t
        Tele:\t\t{}\t
        Message:\t\t{}\t
        '''.format(form_data['nom'], form_data['tele'], form_data['message'])

        send_mail('Message d\'un Client!', message, "agentmetier@gmail.com", [
                  'agentmetier@gmail.com'])
        messages.success(request, f"La demande a été bien envoyer.Merci")

    return render(request, 'MonEcoBrico/contact.html')


def service(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        metier = request.POST.get('metier')
        tele = request.POST.get('tele')
        ville = request.POST.get('ville')
        form_data = {
            'nom': nom,
            'metier': metier,
            'tele': tele,
            'ville': ville,
        }
        message = '''
        From:\t\t\t{}\t
        metier:\t\t\t{}\t
        Tele:\t\t\t{}\t
        ville:\t\t\t{}\t
        '''.format(form_data['nom'], form_data['metier'], form_data['tele'], form_data['ville'])

        send_mail('Message From Client!', message, "agentmetier@gmail.com", [
                  'agentmetier@gmail.com'])
        messages.success(
            request, f"La demande a été bien envoyer.on va vous contacter va vous contacter prochainement, Merci")

    return render(request, 'MonEcoBrico/service.html')


class DetailView(generic.DetailView):
    model = Metiers
    template_name = 'MonEcoBrico/service.html'


def ServiceDetail(request, slug):
    metier = Metiers.objects.get(slug=slug)
    args = {'metier': metier}
    if request.method == 'POST':
        nom = request.POST.get('nom')
        metier = request.POST.get('metier')
        tele = request.POST.get('tele')
        ville = request.POST.get('ville')
        form_data = {
            'nom': nom,
            'metier': metier,
            'tele': tele,
            'ville': ville,
        }
        message = '''
        From:\t\t\t{}\t
        metier:\t\t\t{}\t
        Tele:\t\t\t{}\t
        ville:\t\t\t{}\t
        '''.format(form_data['nom'], form_data['metier'], form_data['tele'], form_data['ville'])

        send_mail(' Demande d\'un Client : ', message, "agentmetier@gmail.com", [
            'agentmetier@gmail.com'])
        messages.success(
            request, f"La demande a été bien envoyer.on va vous contacter prochainement, Merci")

    return render(request, 'MonEcoBrico/service.html', args)


def error_500(request):
    return render(request, '500.html')


def error_404(request, exception):
    return render(request, '404.html')


# def privacy(request):
#     return render(request, 'MonEcoBrico/privacy_policy.html')


# class ServiceList(generic.ListView):
#     queryset = Metiers.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'


# class Service(generic.Service):
#     model = Metiers
#     template_name = 'MonEcoBrico/index.html'
