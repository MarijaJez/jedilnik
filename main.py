SKRIVNOST = "r!atk!XJH1UXAZ0$U#*BN8bYb34MMC&RCy$3Gw&qgv9$44zYS7"

import imp
import bottle
import hashlib
from bottle import route, run, template, request
import json
import random 

import uporabniki
import gospodinjstva

uporabniki.preberi()
gospodinjstva.preberi() 

def hashSHA256(s):
    h = hashlib.sha256(s.encode('utf8'))
    return h.hexdigest()

def preveri_uporabnika(redirect=True):
    ime = bottle.request.get_cookie('uporabnisko_ime', secret=SKRIVNOST)
    if ime == None and redirect:
        bottle.redirect("/")
        
    return ime

@bottle.get("/")
def indeks():
    return bottle.template("tpl/zacetna_stran.tpl")

@bottle.get("/osebna_stran")
def funkcija():
    uporabnisko_ime = preveri_uporabnika()
    moja_gospodinjstva = gospodinjstva.seznam_uporabnika(uporabnisko_ime)
    return bottle.template("tpl/osebna_stran.tpl", {'ime': uporabnisko_ime, 'gospodinjstva': moja_gospodinjstva})

@bottle.get("/prijava")
def indeks():
    if preveri_uporabnika(redirect=False) is not None:
        return bottle.redirect("/osebna_stran")
    
    return bottle.template("tpl/prijava.tpl")

@bottle.post("/prijava")
def prijava():
    ime = request.forms.ime
    geslo = request.forms.geslo
    uporabnik = uporabniki.poisci(ime, geslo)
    if uporabnik is None:
        return bottle.template("tpl/napaka.tpl", naslov="Napaka pri prijavi", opis="Uporabniško ime ali geslo ni ustrezno!", gumb="Nazaj na prijavo", povezava="/prijava")
    else:
        bottle.response.set_cookie('uporabnisko_ime', ime, path="/", secret=SKRIVNOST)
        return bottle.redirect("/osebna_stran") 

@bottle.get("/registracija")
def indeks():
    if preveri_uporabnika(redirect=False) is not None:
        return bottle.redirect("/osebna_stran")
    
    return bottle.template("tpl/registracija.tpl")

@bottle.post("/registracija")
def registracija():
    ime = request.forms.ime
    geslo = request.forms.geslo
    potrditev = request.forms.potrditev

    try:
        uporabniki.dodaj(ime, geslo, potrditev)
    except Exception as e:
        return bottle.template("tpl/napaka.tpl", naslov="Napaka pri registraciji", opis=str(e), gumb="Poskusi ponovno", povezava="/registracija")

    bottle.response.set_cookie('uporabnisko_ime', ime, path='/', secret=SKRIVNOST)
    return bottle.redirect("/osebna_stran")

@bottle.get("/zamenjaj_geslo")
def indeks():
    uporabnisko_ime = preveri_uporabnika()
    return bottle.template("tpl/zamenjaj_geslo.tpl", {'ime': uporabnisko_ime})
    
@bottle.post("/zamenjaj_geslo")
def zamenjaj_geslo():
    uporabnisko_ime = preveri_uporabnika()
    geslo = hashSHA256(request.forms.geslo)
    novo_geslo = request.forms.novo_geslo
    potrditev = request.forms.potrditev
    
    try:
        uporabniki.zamenjaj_geslo(uporabnisko_ime, geslo, novo_geslo, potrditev)
    except Exception as e:
        return bottle.template("tpl/napaka.tpl", naslov="Napaka pri menjavi gesla", opis=str(e), gumb="Poskusi ponovno", povezava="/zamenjaj_geslo")
    
    return bottle.redirect("/osebna_stran")

@bottle.get("/odjava")
def odjava():
    bottle.response.delete_cookie('uporabnisko_ime')
    return bottle.redirect("/")

@bottle.get("/dodaj_gospodinjstvo")
def indeks():
    uporabnisko_ime = preveri_uporabnika()
    return bottle.template("tpl/dodaj_gospodinjstvo.tpl", {'ime': uporabnisko_ime})

@bottle.post("/dodaj_gospodinjstvo")
def dodaj_gospodinjstvo():
    uporabnisko_ime = preveri_uporabnika()
    ime = request.forms.ime_gospodinjstva
    geslo = request.forms.geslo

    try:
        gospodinjstva.dodaj(ime, geslo, uporabnisko_ime)
    except Exception as e:
        if str(e) == "ime_zasedeno":
            return bottle.redirect(f"/ze_obstaja/{ime}")
        else:
            return bottle.template("tpl/napaka.tpl", naslov="Napaka", opis="Polja za uporabniško ime ali geslo ne smete pustiti praznega", gumb="Poskusi ponovno", povezava="/dodaj_gospodinjstvo")
    
    return bottle.redirect("/osebna_stran")
    
@bottle.get("/ze_obstaja/<ime_gospodinjstva>")
def indeks(ime_gospodinjstva):
    return bottle.template("tpl/ze_obstaja.tpl", ime_gospodinjstva=ime_gospodinjstva)

@bottle.get("/pridruzi_se")
def indeks():
    uporabnisko_ime = preveri_uporabnika()
    return bottle.template("tpl/pridruzi_se.tpl", {'ime': uporabnisko_ime})

@bottle.post("/pridruzi_se")
def pridruzi_se():
    uporabnisko_ime = preveri_uporabnika()
    ime = request.forms.ime_gospodinjstva
    geslo = request.forms.geslo
    
    gospodinjstvo = gospodinjstva.poisci_z_imenom(ime)
    
    if gospodinjstvo is None:
        return bottle.template("tpl/napaka.tpl", naslov="Napaka pri pridružitvi gospodinjstvu", opis="To gospodinjstvo ne obstaja.", gumb="Poskusi ponovno.", povezava="/pridruzi_se")
    
    gospodinjstvo = gospodinjstva.poisci(ime, geslo)
    
    if gospodinjstvo is None:
        return bottle.template("tpl/napaka.tpl", naslov="Napaka pri pridružitvi gospodinjstvu", opis="Napačno geslo.", gumb="Poskusi ponovno.", povezava="/pridruzi_se")

    try:
        gospodinjstvo.dodaj_clana(uporabnisko_ime)
    except:
        return bottle.template("tpl/napaka.tpl", naslov="Napaka pri pridruzitvi gospodinjstvu", opis="Ste že član tega gospodinjstva! Ne morete se prodružiti ponovno.", gumb="Nazaj na osebno stran.", povezava="/osebna_stran")

    return bottle.redirect("/osebna_stran")

@bottle.get("/stran_gospodinjstva/<ime>")
def indeks(ime): 
    gospodinjstvo = gospodinjstva.poisci_z_imenom(ime)
    uporabnisko_ime = preveri_uporabnika()

    return bottle.template("tpl/stran_gospodinjstva.tpl", {"ime" : uporabnisko_ime, "ime_gospodinjstva": ime, "clani": gospodinjstvo.clani, "jedi": gospodinjstvo.jedi, "jedilniki": gospodinjstvo.jedilniki})

@bottle.get("/dodaj_jed/<gospodinjstvo>")
def indeks(gospodinjstvo):
    return bottle.template("tpl/dodaj_jed.tpl", {"ime_gospodinjstva": gospodinjstvo})

@bottle.post("/dodaj_jed/<ime>")
def dodaj_jed(ime):
    jed = request.forms.ime_jedi
    gospodinjstva.dodaj_jed(ime, jed)

    return bottle.redirect(f"/stran_gospodinjstva/{ime}")

@bottle.get("/nov_jedilnik/<ime_gospodinjstva>")
def indeks(ime_gospodinjstva):
    return bottle.template("tpl/nov_jedilnik.tpl", {"ime_gospodinjstva": ime_gospodinjstva})

@bottle.post("/nov_jedilnik/<ime>")
def zgeneriraj_jedilnik(ime): 

    ponedeljek = request.forms.ponedeljek
    torek = request.forms.torek
    sreda = request.forms.sreda
    četrtek = request.forms.četrtek
    petek = request.forms.petek
    sobota = request.forms.sobota
    nedelja = request.forms.nedelja
    teden = [ponedeljek, torek, sreda, četrtek, petek, sobota, nedelja]
    try:
        gospodinjstva.zgeneriraj_jedilnik(ime, teden)
    except:
        return bottle.template("tpl/napaka.tpl", naslov="Napaka pri generiranju jedilnika", opis="V bazi jedi tega gospodinjstva še ni dovolj jedi. Najprej dodajte zadostno količino jedi v bazo, nato pa poskusite ponovno.", gumb="Nazaj na stran gospodinjstva.", povezava=f"/stran_gospodinjstva/{ime}")
    return bottle.redirect(f"/jedilniki/{ime}")

@bottle.get("/jedilniki/<ime_gospodinjstva>")
def indeks(ime_gospodinjstva):
    gospodinjstvo = gospodinjstva.poisci_z_imenom(ime_gospodinjstva)
    uporabnisko_ime = preveri_uporabnika()
    
    return bottle.template("tpl/jedilniki.tpl", {"ime": uporabnisko_ime, "ime_gospodinjstva": ime_gospodinjstva, "jedilniki": gospodinjstvo.jedilniki})

@bottle.get("/zapusti_gospodinjstvo/<ime_gospodinjstva>")
def zapusti_gospodinjstvo(ime_gospodinjstva):
    uporabnisko_ime = preveri_uporabnika()
    gospodinjstva.zapusti_gospodinjstvo(ime_gospodinjstva, uporabnisko_ime)
    
    return bottle.redirect("/osebna_stran")
 
@bottle.get("/izbriši_jed/<ime_gospodinjstva>/<ime_jedi>")
def izbriši_jed(ime_gospodinjstva, ime_jedi):
    gospodinjstva.izbriši_jed(ime_gospodinjstva, ime_jedi)

    return bottle.redirect(f"/stran_gospodinjstva/{ime_gospodinjstva}")

@bottle.get("/izbriši_jedilnik/<ime_gospodinjstva>/<indeks>")
def izbriši_jedilnik(ime_gospodinjstva, indeks):
    gospodinjstva.izbriši_jedilnik(ime_gospodinjstva, indeks)
        
    return bottle.redirect(f"/jedilniki/{ime_gospodinjstva}")

@bottle.get("/style.css")
def slog():
    return bottle.static_file("style.css", root="tpl")

@bottle.get("/normalize.css")
def slog():
    return bottle.static_file("normalize.css", root="tpl")

run(host='localhost', port=8080, reloader=True)
