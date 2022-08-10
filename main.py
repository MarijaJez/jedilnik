SKRIVNOST = "r!atk!XJH1UXAZ0$U#*BN8bYb34MMC&RCy$3Gw&qgv9$44zYS7"

import bottle
import hashlib
from bottle import route, run, template, request
import json
import random 

def hashSHA256(s):
    h = hashlib.sha256(s.encode('utf8'))
    return h.hexdigest()

def preveri_uporabnika():
    ime = bottle.request.get_cookie('uporabnisko_ime', secret=SKRIVNOST)
    if ime == None:
        bottle.redirect("/")
    return ime

def preveri_gospodinjstva():
    uporabnisko_ime = preveri_uporabnika()
    moja_gospodinjstva = []
    with open("gospodinjstva.json", encoding='utf8') as d:
        gospodinjstva = json.loads(d.read())
    for gospodinjstvo in gospodinjstva:
        if uporabnisko_ime in gospodinjstvo["clani"]:
            moja_gospodinjstva.append(gospodinjstvo["ime_gospodinjstva"])
    return moja_gospodinjstva

@bottle.get("/")
def indeks():
    return bottle.template("tpl/zacetna_stran.tpl")

@bottle.get("/osebna_stran")
def funkcija():
    uporabnisko_ime = preveri_uporabnika()
    moja_gospodinjstva = preveri_gospodinjstva()
    return bottle.template("tpl/osebna_stran.tpl", {'ime': uporabnisko_ime, 'gospodinjstva': moja_gospodinjstva})

@bottle.get("/prijava")
def indeks():
    return bottle.template("tpl/prijava.tpl")

@bottle.post("/prijava")
def prijava():
    ime = request.forms.ime
    geslo = hashSHA256(request.forms.geslo)
    with open("uporabniki.json", encoding='utf8') as d:
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
    ime = request.forms.ime
    geslo = hashSHA256(request.forms.geslo)
    nov_uporabnik = {"uporabnisko_ime": ime,
        "geslo": geslo}
    with open("uporabniki.json", encoding='utf8') as d:
        uporabniki = json.loads(d.read())
    for uporabnik in uporabniki:
        if ime == uporabnik["uporabnisko_ime"]:
            return bottle.template("tpl/napaka.tpl")
    uporabniki.append(nov_uporabnik)
    with open('uporabniki.json', 'w', encoding='utf8') as d:
        json.dump(uporabniki, d, ensure_ascii=False)
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
    ime = request.forms.ime_gospodinjstva
    geslo = hashSHA256(request.forms.geslo)
    jedi = [request.forms.jed1, request.forms.jed2, request.forms.jed3, request.forms.jed4, request.forms.jed5, request.forms.jed6, request.forms.jed7]
    novo_gospodinjstvo = {
        "ime_gospodinjstva": ime, 
        "geslo": geslo, 
        "clani": [uporabnisko_ime],
        "jedi": jedi,
        "jedilniki": []
    }
    with open("gospodinjstva.json", encoding='utf8') as d:
        gospodinjstva = json.loads(d.read())
    for gospodinjstvo in gospodinjstva:
        if ime == gospodinjstvo["ime_gospodinjstva"]:
            return bottle.redirect(f"/ze_obstaja/{ime}")
    gospodinjstva.append(novo_gospodinjstvo)
    with open('gospodinjstva.json', 'w', encoding='utf8') as d:
        json.dump(gospodinjstva, d, ensure_ascii=False)
    moja_gospodinjstva = preveri_gospodinjstva()
    return bottle.template("tpl/osebna_stran.tpl", {'ime': uporabnisko_ime, 'gospodinjstva': moja_gospodinjstva})

@bottle.get("/ze_obstaja/<ime_gospodinjstva>")
def indeks(ime_gospodinjstva):
    return bottle.template("tpl/ze_obstaja.tpl", ime_gospodinjstva=ime_gospodinjstva)

@bottle.get("/pridruzi_se_n/<ime_gospodinjstva>")
def pridruzi_se_n(ime_gospodinjstva):
    uporabnisko_ime = preveri_uporabnika()
    with open("gospodinjstva.json", encoding='utf8') as d:
        gospodinjstva = json.loads(d.read())
    for gospodinjstvo in gospodinjstva:
        if gospodinjstvo["ime_gospodinjstva"] == ime_gospodinjstva:
            if uporabnisko_ime not in gospodinjstvo["clani"]:
                gospodinjstvo["clani"].append(uporabnisko_ime)
            else:
                return bottle.template("tpl/napaka.tpl")
    with open('gospodinjstva.json', 'w', encoding='utf8') as d:
        json.dump(gospodinjstva, d, ensure_ascii=False)   
    moja_gospodinjstva = preveri_gospodinjstva()
    return bottle.template("tpl/osebna_stran.tpl", {'ime': uporabnisko_ime, 'gospodinjstva': moja_gospodinjstva})

@bottle.get("/pridruzi_se")
def indeks():
    return bottle.template("tpl/pridruzi_se.tpl")

@bottle.post("/pridruzi_se")
def pridruzi_se():
    uporabnisko_ime = preveri_uporabnika() 
    ime = request.forms.ime_gospodinjstva
    geslo = hashSHA256(request.forms.geslo)
    with open("gospodinjstva.json", encoding='utf8') as d:
        gospodinjstva = json.loads(d.read())
    for gospodinjstvo in gospodinjstva:
        if gospodinjstvo["ime_gospodinjstva"] == ime and gospodinjstvo["geslo"] == geslo:
            if uporabnisko_ime in gospodinjstvo["clani"]:
                return bottle.template("tpl/napaka.tpl")
            else:
                gospodinjstvo["clani"].append(uporabnisko_ime)
    with open('gospodinjstva.json', 'w', encoding='utf8') as d:
        json.dump(gospodinjstva, d, ensure_ascii=False)
    return bottle.redirect("/osebna_stran")

@bottle.get("/stran_gospodinjstva/<gospodinjstvo>")
def indeks(gospodinjstvo): 
    with open("gospodinjstva.json", encoding='utf8') as d:
        gospodinjstva = json.loads(d.read()) 
    for g in gospodinjstva:
        if gospodinjstvo == g["ime_gospodinjstva"]: 
            clani, jedi = g["clani"], g["jedi"]
    return bottle.template("tpl/stran_gospodinjstva.tpl", {"ime_gospodinjstva": gospodinjstvo, "clani": clani, "jedi": jedi})

@bottle.get("/dodaj_jed/<gospodinjstvo>")
def indeks(gospodinjstvo):
    return bottle.template("tpl/dodaj_jed.tpl", {"ime_gospodinjstva": gospodinjstvo})

@bottle.post("/dodaj_jed/<gospodinjstvo>")
def dodaj_jed(gospodinjstvo):
    jed = request.forms.ime_jedi
    with open("gospodinjstva.json", encoding='utf8') as d:
        gospodinjstva = json.loads(d.read()) 
    for g in gospodinjstva:
        if gospodinjstvo == g["ime_gospodinjstva"]:
            jedi = g["jedi"]
    jedi.append(jed)
    print(jed)
    with open('gospodinjstva.json', 'w', encoding='utf8') as d:
        json.dump(gospodinjstva, d, ensure_ascii=False)
    return bottle.redirect(f"/stran_gospodinjstva/{gospodinjstvo}")

@bottle.get("/nov_jedilnik/<ime_gospodinjstva>")
def indeks(ime_gospodinjstva):
    return bottle.template("tpl/nov_jedilnik.tpl", {"ime_gospodinjstva": ime_gospodinjstva})

@bottle.post("/nov_jedilnik/<ime_gospodinjstva>")
def zgeneriraj_jedilnik(ime_gospodinjstva):
    ponedeljek = request.forms.ponedeljek
    torek = request.forms.torek
    sreda = request.forms.sreda
    četrtek = request.forms.četrtek
    petek = request.forms.petek
    sobota = request.forms.sobota
    nedelja = request.forms.nedelja
    teden = [ponedeljek, torek, sreda, četrtek, petek, sobota, nedelja]
    with open("gospodinjstva.json",  encoding='utf8') as d:
        gospodinjstva = json.loads(d.read())
    prazni = 0
    for gospodinjstvo in gospodinjstva:
        if gospodinjstvo["ime_gospodinjstva"] == ime_gospodinjstva:
            jedi = gospodinjstvo["jedi"]
    for dan in teden:
        if dan == "":
            prazni += 1
    dodaj = random.sample(jedi, prazni)
    for i, dan in enumerate(teden):
        if dan == "":
            teden[i] = dodaj[prazni - 1]
            prazni -= 1
        elif dan not in jedi:
            jedi.append(dan)
    for gospodinjstvo in gospodinjstva:
        if gospodinjstvo["ime_gospodinjstva"] == ime_gospodinjstva:
            gospodinjstvo["jedilniki"].append(teden)
    with open("gospodinjstva.json", "w", encoding='utf8') as d:
        json.dump(gospodinjstva, d, ensure_ascii=False)
    return bottle.redirect(f"/stran_gospodinjstva/{ime_gospodinjstva}")

@bottle.get("/jedilniki/<ime_gospodinjstva>")
def indeks(ime_gospodinjstva):
    with open("gospodinjstva.json", encoding='utf8') as d:
        gospodinjstva = json.loads(d.read()) 
    for g in gospodinjstva:
        if ime_gospodinjstva == g["ime_gospodinjstva"]: 
            jedilniki = g["jedilniki"]
    return bottle.template("tpl/jedilniki.tpl", {"ime_gospodinjstva": ime_gospodinjstva, "jedilniki": jedilniki})

@bottle.get("/zapusti_gospodinjstvo/<ime_gospodinjstva>")
def zapusti_gospodinjstvo(ime_gospodinjstva):
    uporabnisko_ime = preveri_uporabnika()
    with open("gospodinjstva.json", encoding='utf8') as d:
        gospodinjstva = json.loads(d.read()) 
    for g in gospodinjstva:
        if ime_gospodinjstva == g["ime_gospodinjstva"]: 
            g["clani"].remove(uporabnisko_ime)
    with open("gospodinjstva.json", "w", encoding='utf8') as d:
        json.dump(gospodinjstva, d, ensure_ascii=False)
    return bottle.redirect("/osebna_stran")

@bottle.get("/izbriši_jed/<ime_gospodinjstva>/<ime_jedi>")
def izbriši_jed(ime_gospodinjstva, ime_jedi):
    with open("gospodinjstva.json", encoding='utf8') as d:
        gospodinjstva = json.loads(d.read()) 
    for g in gospodinjstva:
        if ime_gospodinjstva == g["ime_gospodinjstva"]: 
            g["jedi"].remove(ime_jedi)
    with open("gospodinjstva.json", "w", encoding='utf8') as d:
        json.dump(gospodinjstva, d, ensure_ascii=False)
    return bottle.redirect(f"/stran_gospodinjstva/{ime_gospodinjstva}")

@bottle.get("/izbriši_jedilnik/<ime_gospodinjstva>/<indeks>")
def izbriši_jedilnik(ime_gospodinjstva, indeks):
    with open("gospodinjstva.json", encoding='utf8') as d:
        gospodinjstva = json.loads(d.read()) 
    for g in gospodinjstva:
        if ime_gospodinjstva == g["ime_gospodinjstva"]: 
            g["jedilniki"].pop(int(indeks))
    with open("gospodinjstva.json", "w", encoding='utf8') as d:
        json.dump(gospodinjstva, d, ensure_ascii=False)
    return bottle.redirect(f"/jedilniki/{ime_gospodinjstva}")

run(host='localhost', port=8080, reloader=True)
