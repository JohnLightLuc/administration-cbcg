from django.shortcuts import render, redirect
from demande import models  as demande_models
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='myadmin:connexion')
def home(request):
    attestationconges = demande_models.Attestationconge.objects.filter(status=True)
    certi_travails = demande_models.Certificattravail.objects.filter(status=True)
    certi_services = demande_models.Certificatpriseservice.objects.filter(status=True)
    nbre_traite = len(attestationconges.filter(etat="Traité")) + len(certi_travails.filter(etat="Traité")) + len(certi_services.filter(etat="Traité"))
    nbre_conge = len(attestationconges)
    nbre_travail = len(certi_travails)
    nbre_service = len(certi_services)
    total = nbre_conge + nbre_travail + nbre_service
    maximum = max(nbre_conge, nbre_travail, nbre_service)
    demandes = list()
    demandes.append(attestationconges)
    demandes.append(certi_travails)
    demandes.append(certi_services)

    notifications = demande_models.Notification.objects.filter(status=True).order_by('-date_add')

    data = {
        'total':total,
        'demandes':demandes,
        "nbre_traite": nbre_traite,
        'notifications':notifications
    }
    return render(request, 'pages/myadmin/home.html', data)

@login_required(login_url='myadmin:connexion')
def deletenotification(request, id):
    try:
        notification = demande_models.Notification.objects.get(pk = id)
        notification.delete()
        return redirect('myadmin:home')
    except:
        return redirect('myadmin:home')

@login_required(login_url='myadmin:connexion')
def delete_all_notification(request):
    try:
        notifications = demande_models.Notification.objects.all()
        for item in notifications:
            item.delete()
        return redirect('myadmin:home')
    except:
        return redirect('myadmin:home')

@login_required(login_url='myadmin:connexion')
def supprimerConge(request, id):
    try:
        conge = demande_models.Attestationconge.objects.get(pk = id)
        conge.status = False
        conge.save()
        return redirect("myadmin:home")
    except:
        return redirect("myadmin:home")

@login_required(login_url='myadmin:connexion')
def supprimertravail(request, id):
    try:
        travail = demande_models.Certificattravail.objects.get(pk = id)
        travail.status = False
        travail.save()
        return redirect("myadmin:home")
    except:
        return redirect("myadmin:home")

@login_required(login_url='myadmin:connexion')
def supprimerservice(request, id):
    try:
        service = demande_models.Certificatpriseservice.get(pk = id)
        service.status = False
        service.save()
        return redirect("myadmin:home")
    except:
        return redirect("myadmin:home")

@login_required(login_url='myadmin:connexion')
def compte(request):
    notifications = demande_models.Notification.objects.filter(status=True).order_by('-date_add')
    if request.POST:
        password = repassword =  photo = ""
        statut=False
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        photo = request.FILES.get('profileImg')
        
        if photo != "":
            try:
                user = User.objects.get(username=request.user.username)
                admin = models.Administration.objects.get(user=user)
                admin.photo = photo
                admin.save()
                message = "Photo mise à jour avec succès !"
                statut=True
            except Exception as e:
                print(str(e))
                message = "Probleme d'enregistrement. Si cela persite, contactez l'administrateur !"

        if password !="":
            if password != repassword:
                message = "Les mots de passe ne sont pas identiques !"
            else:
                try:
                    myusername = request.user.username
                    user = User.objects.get(username=myusername)
                    print(user)
                    user.set_password(password)
                    user.save()
                    message = "Mot de passe modifié avec succès !"
                    statut=True
                    password = repassword =""
                except:
                    message = "Probleme survenu lors de la modification veuillez reéssayer svp !"

        data={
            "response":True,
            "statut":statut,
            "message":message,
            "password":password,
            "repassword": repassword,
            'notifications':notifications
        }
        return render(request, 'pages/myadmin/compte.html', data )
    else:
        data={
            'notifications':notifications,
            "response":False,
            "password":'',
            "repassword": ''
        }
        return render(request, 'pages/myadmin/compte.html', data )

@login_required(login_url='myadmin:connexion')
def attestation_conge(request, id):
    conge = demande_models.Attestationconge.objects.get(pk=id)
    data = {
        'conge':conge
    }
    return render(request, 'pages/myadmin/attestation_conge.html', data)

@login_required(login_url='myadmin:connexion')
def attestation_travail(request, id):
    certi_travail = demande_models.Certificattravail.objects.get(pk=id)
    data = {
        'certi_travail': certi_travail
    }
    return render(request, 'pages/myadmin/attestation_travail.html', data)

@login_required(login_url='myadmin:connexion')
def certificat_service(request, id):
    service = demande_models.Certificatpriseservice.objects.get(pk=id)
    data = {
        'service': service
    }
    return render(request, 'pages/myadmin/certificat_prise_service.html', data)

def connexion(request):
    if request.POST:
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if username =="" or password =="":
            message = "Veuillez remplir tous les champs svp !"
        else:
            next_page = request.POST.get('next', False) 
            user = authenticate(username=username, password=password)

            if user is not None and user.is_active:

                print("user is login")
                
                login(request, user)

                if next_page: 
                    return redirect(next_page)
                else:
                    return redirect('myadmin:home') # page si connect
                
            else:
                message ="Username et/ou mot de passe incorrecte"
        data = {
            "statut": True,
            "username":username,
            "password": password,
            "message": message,
            'next': next_page
        }
        return render(request, 'pages/myadmin/connexion.html', data)
    else:
        data={
            "statut":False,
            "username":'',
            "password": ''
        }
        return render(request, 'pages/myadmin/connexion.html', data)

def deconnexion(request):
    logout(request)
    return redirect('myadmin:connexion')

