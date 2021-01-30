from django.shortcuts import render, redirect
from .  import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
    
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
                    return redirect('demande:index') # page si connect
                
            else:
                message ="Username et/ou mot de passe incorrecte"
        data = {
            "statut": True,
            "username":username,
            "password": password,
            "message": message,
            'next': next_page
        }
        return render(request, 'pages/demande/connexion.html', data)
    else:
        data={
            "statut":False,
            "username":'',
            "password": ''
        }
        return render(request, 'pages/demande/connexion.html', data)

@login_required(login_url='demande:connexion')
def home(request):
    return render(request, 'pages/demande/index.html')

@login_required(login_url='demande:connexion')
def compte(request):
    myprof = request.user.professeur
    demandes = list()
    attestationconges = models.Attestationconge.objects.filter(prof=myprof)
    certi_travails = models.Certificattravail.objects.filter(prof=myprof)
    certi_services = models.Certificatpriseservice.objects.filter(prof=myprof)
  
    user = User.objects.get(username=request.user.username)
    anneepriseservice = models.Professeur.objects.get(user=user).annee_de_prise_de_travail
                 
    demandes.append(attestationconges)
    demandes.append(certi_travails)
    demandes.append(certi_services)

    data = {
        'demandes':demandes,
        'anneepriseservice':anneepriseservice
    }
    return render(request, 'pages/demande/compte.html', data)

@login_required(login_url='demande:connexion')
def annuleconge(request, id):
    try:
        obj = models.Attestationconge.objects.get(pk=id)
        obj.etat = 'Annulé'
        obj.save()
        return redirect('demande:compte')
    except:
        return redirect('demande:compte')


@login_required(login_url='demande:connexion')
def annuletravail(request, id):
    try:
        obj = models.Certificattravail.objects.get(pk=id)
        obj.etat = 'Annulé'
        obj.save()
        return redirect('demande:compte')
    except:
        return redirect('demande:compte')

@login_required(login_url='demande:connexion')
def annuleservice(request, id):
    try:
        obj = models.Certificatpriseservice.objects.get(pk=id)
        obj.etat = 'Annulé'
        obj.save()
        return redirect('demande:compte')
    except:
        return redirect('demande:compte')

@login_required(login_url='demande:connexion')
def modify(request):   
    if request.POST:
        password = repassword =  anneepriseservice = ""
        statut=False
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        anneepriseservice = request.POST.get('mois')
        print("anneepriseservice")
        print(anneepriseservice)
        
        if anneepriseservice != "":
            try:
                user = User.objects.get(username=request.user.username)
                prof = models.Professeur.objects.get(user=user)
                prof.annee_de_prise_de_travail = anneepriseservice
                prof.save()
                message = "Année de prise de service mise à jour avec succès !"
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
            "anneepriseservice":anneepriseservice
        }
        return render(request, 'pages/demande/compte.html', data )
    else:
        return redirect('demande:compte')


@login_required(login_url='demande:connexion')
def travail(request):
    message = nom = prenom=  matricule = emploi = grade =""
    statut =False
    if request.POST:
        saisi = True
        nom= request.POST.get('nom')
        prenom= request.POST.get('prenom')
        matricule= request.POST.get('matricule')
        emploi= request.POST.get('emploi')
        grade= request.POST.get('grade')

        if nom =="" or prenom == "" or matricule =="" or emploi == grade =="":
            saisi = False
            message="Veuillez remplir tous les champs svp !"
    
        if  saisi == True:
            myprof = request.user.professeur
            # save data
            try:
                certificat = models.Certificattravail(
                    prof= myprof,
                    nom= nom,
                    prenom= prenom,
                    matricule= matricule,
                    emploi= emploi,
                    grade= grade
                )
                certificat.save()
                statut = True
                message="Votre demande a été enregistrée avec succès!"
                try:
                    notification = models.Notification(
                        prof= myprof,
                        titre= "Demande d'attestation de travail",
                        type_demande= 'travail',
                        demande_id = certificat.id
                    )
                    notification.save()
                except Exception as e:
                    print(str(e))
                nom = prenom=  matricule = emploi = grade =""
            except Exception as e:
                statut = False
                message = "Probleme d'enregistrement, veuillez reessayer svp !" 
                print(str(e))
        data = {
            'message':message,
            'nom':nom,
            'prenom':prenom,
            'matricule':matricule,
            'emploi':emploi,
            'grade':grade,
            'statut':statut,
        }
        return render(request, 'pages/demande/travail.html', data)
    else:
        data = {
            'message':message,
            'nom':nom,
            'prenom':prenom,
            'matricule':matricule,
            'emploi':emploi,
            'grade':grade,
            'statut':statut,
        }
        return render(request, 'pages/demande/travail.html', data)

@login_required(login_url='demande:connexion')
def attestation_conge(request):
    message = nom = prenom=  matricule = fonction = datebebut = datefin = destination= motif=""
    statut =False
    if request.POST:
        saisi = True
        nom= request.POST.get('nom')
        prenom= request.POST.get('prenom')
        fonction= request.POST.get('fonction')
        matricule= request.POST.get('matricule')
        datebebut= request.POST.get('date_debut')
        datefin= request.POST.get('date_fin')
        destination= request.POST.get('destination')
        motif= request.POST.get('motif')

        if nom =="" or prenom == "" or matricule =="" or fonction =="" or datebebut =="" or datefin == destination== motif=="":
            saisi = False
            message="Veuillez remplir tous les champs svp !"
    
        if  saisi == True:
            myprof = request.user.professeur
            # save data
            try:
                certificat = models.Attestationconge(
                    prof= myprof,
                    nom= nom,
                    prenom= prenom,
                    fonction= fonction,
                    matricule= matricule,
                    datedebut= datebebut,
                    datefin= datefin,
                    destination= destination,
                    motif= motif
                )
                certificat.save()
                statut = True
                message="Votre demande a été enregistrée avec succès!"
                try:
                    notification = models.Notification(
                        prof= myprof,
                        titre= "Demande d'attestation de congé exceptionnel",
                        type_demande= 'conge',
                        demande_id = certificat.id
                    )
                    notification.save()
                except Exception as e:
                    print(str(e))
                nom = prenom=  matricule = fonction = datebebut = datefin = destination= motif=""
            except Exception as e:
                statut = False
                message = "Probleme d'enregistrement, veuillez reessayer svp !"
                print(str(e))
        data = {
            'message':message,
            'nom':nom,
            'prenom':prenom,
            'matricule':matricule,
            'fonction':fonction,
            'datebebut':datebebut,
            'datefin':datefin,
            'destination':destination,
            'motif':motif,
            'statut':statut,
        }
        return render(request, 'pages/demande/attestation_conge.html', data)
    else:
        data = {
            'message':message,
            'nom':nom,
            'prenom':prenom,
            'matricule':matricule,
            'fonction':fonction,
            'datebebut':datebebut,
            'datefin':datefin,
            'destination':destination,
            'motif':motif,
            'statut':statut,
        }
        return render(request, 'pages/demande/attestation_conge.html', data)
        
@login_required(login_url='demande:connexion')  
def service(request):
    message = nom = prenom=  matricule = emploi = grade =""
    statut =False
    if request.POST:
        saisi = True
        nom= request.POST.get('nom')
        prenom= request.POST.get('prenom')
        matricule= request.POST.get('matricule')
        emploi= request.POST.get('emploi')
        grade= request.POST.get('grade')

        if nom =="" or prenom == "" or matricule =="" or emploi == grade =="":
            saisi = False
            message="Veuillez remplir tous les champs svp !"
    
        if  saisi == True:
            myprof = request.user.professeur
            # save data
            try:
                certificat = models.Certificatpriseservice(
                    prof= myprof,
                    nom= nom,
                    prenom= prenom,
                    matricule= matricule,
                    emploi= emploi,
                    grade= grade
                )
                certificat.save()
                statut = True
                message="Votre demande a été enregistrée avec succès!"
                try:
                    notification = models.Notification(
                        prof = myprof,
                        titre = "Demande de certificat de prise de service",
                        type_demande= 'service',
                        demande_id = certificat.id
                    )
                    notification.save()
                except Exception as e:
                    print(str(e))
                nom = prenom=  matricule = emploi = grade =""
            except Exception as e:
                statut = False
                message = "Probleme d'enregistrement, veuillez reessayer svp !"
                print(str(e))
        data = {
            'message':message,
            'nom':nom,
            'prenom':prenom,
            'matricule':matricule,
            'emploi':emploi,
            'grade':grade,
            'statut':statut,
        }
        return render(request, 'pages/demande/service.html', data)
    else:
        data = {
            'message':message,
            'nom':nom,
            'prenom':prenom,
            'matricule':matricule,
            'emploi':emploi,
            'grade':grade,
            'statut':statut,
        }
        return render(request, 'pages/demande/service.html', data)

def deconnexion(request):
    logout(request)
    return redirect('demande:connexion')