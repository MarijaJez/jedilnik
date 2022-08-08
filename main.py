SKRIVNOST = "r!atk!XJH1UXAZ0$U#*BN8bYb34MMC&RCy$3Gw&qgv9$44zYS7"

import bottle
from bottle import route, run, template, request
import json

@bottle.get("/")
def indeks():
    return bottle.template("tpl/zacetna_stran.tpl")

@bottle.get("/osebna_stran")
def funkcija():
    ime = bottle.request.get_cookie('uporabnisko_ime', secret=SKRIVNOST)
    if ime == None:
        return bottle.redirect("/")
    return bottle.template("tpl/osebna_stran.tpl", {'ime': ime})

@bottle.get("/prijava")
def indeks():
    return bottle.template("tpl/prijava.tpl")

@bottle.post("/prijava")
def prijava():
    ime = request.forms.get('ime')
    geslo = request.forms.get('geslo')
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
def registracija(): #isto ime kot pri prijavi?
    ime = request.forms.get('ime')
    geslo = request.forms.get('geslo')
    nov_uporabnik = {"uporabnisko_ime": ime,
        "geslo": geslo}
    with open("uporabniki.json") as d:
        uporabniki = json.loads(d.read())
    uporabniki.append(nov_uporabnik)
    with open('uporabniki.json', 'w') as d:
        json.dump(uporabniki, d)
    for uporabnik in uporabniki:
        if ime == uporabnik["uporabnisko_ime"] and geslo == uporabnik["geslo"]:
            bottle.response.set_cookie('uporabnisko_ime', ime, path='/', secret=SKRIVNOST)
            return bottle.redirect("/osebna_stran")
    else:
        return bottle.template("tpl/napaka.tpl")

@bottle.get("/odjava")
def odjava():
    bottle.response.delete_cookie('uporabnisko_ime')
    return bottle.redirect("/")


run(host='localhost', port=8080, reloader=True)
