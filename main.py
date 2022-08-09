SKRIVNOST = "r!atk!XJH1UXAZ0$U#*BN8bYb34MMC&RCy$3Gw&qgv9$44zYS7"

import bottle
import hashlib
from bottle import route, run, template, request
import json

def hashSHA256(s):
    h = hashlib.sha256(s.encode('utf8'))
    return h.hexdigest()

def preveri_uporabnika():
    ime = bottle.request.get_cookie('uporabnisko_ime', secret=SKRIVNOST)
    if ime == None:
        bottle.redirect("/")
    return ime

@bottle.get("/")
def indeks():
    return bottle.template("tpl/zacetna_stran.tpl")

@bottle.get("/osebna_stran")
def funkcija():
    uporabnisko_ime = preveri_uporabnika()
    return bottle.template("tpl/osebna_stran.tpl", {'ime': uporabnisko_ime})

@bottle.get("/prijava")
def indeks():
    return bottle.template("tpl/prijava.tpl")

@bottle.post("/prijava")
def prijava():
    ime = request.forms.get('ime')
    geslo = hashSHA256(request.forms.get('geslo'))
    with open("uporabniki.json") as d:
        uporabniki = json.loads(d.read())
    for uporabnik in uporabniki:
        if ime == uporabnik["uporabnisko_ime"] and geslo == uporabnik["geslo"]:
            bottle.response.set_cookie('uporabnisko_ime', ime, path='/', secret=SKRIVNOST)
            return bottle.redirect("/osebna_stran")
    return bottle.template("tpl/napaka.tpl")

@bottle.get("/registracija")
def indeks():
    return bottle.template("tpl/registracija.tpl")

@bottle.post("/registracija")
def registracija():
    ime = request.forms.get('ime')
    geslo = hashSHA256(request.forms.get('geslo'))
    nov_uporabnik = {"uporabnisko_ime": ime,
        "geslo": geslo}
    with open("uporabniki.json") as d:
        uporabniki = json.loads(d.read())
    for uporabnik in uporabniki:
        if ime == uporabnik["uporabnisko_ime"]:
            return bottle.template("tpl/napaka.tpl")
    uporabniki.append(nov_uporabnik)
    with open('uporabniki.json', 'w') as d:
        json.dump(uporabniki, d)
    bottle.response.set_cookie('uporabnisko_ime', ime, path='/', secret=SKRIVNOST)
    return bottle.redirect("/osebna_stran")

@bottle.get("/odjava")
def odjava():
    bottle.response.delete_cookie('uporabnisko_ime')
    return bottle.redirect("/")

@bottle.get("/dodaj_gospodinjstvo")
def indeks():
    return bottle.template("tpl/dodaj_gospodinjstvo.tpl")

@bottle.post("/dodaj_gospodinjstvo")
def dodaj_gospodinjstvo():
    uporabnisko_ime = preveri_uporabnika()
    ime = request.forms.get('ime_gospodinjstva')
    geslo = hashSHA256(request.forms.get('geslo'))
    novo_gospodinjstvo = {
        "ime_gospodinjstva": ime, 
        "geslo": geslo, 
        "člani": [uporabnisko_ime]
    }
    with open("gospodinjstva.json") as d:
        gospodinjstva = json.loads(d.read())
    for gospodinjstvo in gospodinjstva:
        if ime == gospodinjstvo["ime_gospodinjstva"]:
            return bottle.redirect(f"/ze_obstaja/{ime}")
    gospodinjstva.append(novo_gospodinjstvo)
    with open('gospodinjstva.json', 'w') as d:
        json.dump(gospodinjstva, d)
    return bottle.template("tpl/osebna_stran.tpl", {'ime': uporabnisko_ime})

@bottle.get("/ze_obstaja/<ime_gospodinjstva>")
def indeks(ime_gospodinjstva):
    return bottle.template("tpl/ze_obstaja.tpl", ime_gospodinjstva=ime_gospodinjstva)

@bottle.get("/pridruzi_se_n/<ime_gospodinjstva>")
def pridruzi_se_n(ime_gospodinjstva):
    uporabnisko_ime = preveri_uporabnika()
    with open("gospodinjstva.json") as d:
        gospodinjstva = json.loads(d.read())
    for gospodinjstvo in gospodinjstva:
        if gospodinjstvo["ime_gospodinjstva"] == ime_gospodinjstva:
            gospodinjstvo["člani"].append(uporabnisko_ime)
    with open('gospodinjstva.json', 'w') as d:
        json.dump(gospodinjstva, d)   
    return bottle.template("tpl/osebna_stran.tpl", {'ime': uporabnisko_ime})

@bottle.get("/pridruzi_se")
def indeks():
    return bottle.template("tpl/pridruzi_se.tpl")

@bottle.post("/pridruzi_se")
def pridruzi_se():
    uporabnisko_ime = preveri_uporabnika()
    ime = request.forms.get('ime_gospodinjstva')
    geslo = hashSHA256(request.forms.get('geslo'))
    with open("gospodinjstva.json") as d:
        gospodinjstva = json.loads(d.read())
    for gospodinjstvo in gospodinjstva:
        if gospodinjstvo["ime_gospodinjstva"] == ime and gospodinjstvo["geslo"] == geslo:
            if uporabnisko_ime in gospodinjstvo["člani"]:
                return bottle.template("tpl/napaka.tpl")
            else:
                gospodinjstvo["člani"].append(uporabnisko_ime)
    with open('gospodinjstva.json', 'w') as d:
        json.dump(gospodinjstva, d)
    return bottle.redirect("/osebna_stran")

run(host='localhost', port=8080, reloader=True)
