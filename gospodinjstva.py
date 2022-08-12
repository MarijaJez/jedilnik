import imp
import bottle
import hashlib
from bottle import route, run, template, request
import json
import random 

def hashSHA256(s):
    h = hashlib.sha256(s.encode('utf8'))
    return h.hexdigest()

class Gospodinjstvo:
    def __init__(self, ime, geslo, clani, jedi, jedilniki):
        self.ime = ime
        self.geslo = geslo
        self.clani = clani
        self.jedi = jedi
        self.jedilniki = jedilniki
        
    def dodaj_clana(self, ime):
        if ime not in self.clani:
            self.clani.append(ime)
            shrani()
        else:
            raise Exception("V tem gospodinjstvu ste že včlanjeni.")

gospodinjstva = list[Gospodinjstvo]
      
def preberi():
    global gospodinjstva
    with open("gospodinjstva.json", encoding='utf8') as d:
        try:
            surova_gospodinjstva = json.loads(d.read())
        except:
            surova_gospodinjstva = []
        
        gospodinjstva = [Gospodinjstvo(g['ime'], g['geslo'], g['clani'], g['jedi'], g['jedilniki']) for g in surova_gospodinjstva]
        
def shrani():
    global gospodinjstva
    with open('gospodinjstva.json', 'w', encoding='utf8') as f:
        json.dump(gospodinjstva, f, ensure_ascii=False, default=lambda o: o.__dict__, sort_keys=False, indent=4)

def poisci(ime, geslo):
    global gospodinjstva
    for gospodinjstvo in gospodinjstva:
        if ime == gospodinjstvo.ime and hashSHA256(geslo) == gospodinjstvo.geslo:
            return gospodinjstvo
    return None

def poisci_z_imenom(ime):
    global gospodinjstva
    for gospodinjstvo in gospodinjstva:
        if ime == gospodinjstvo.ime:
            return gospodinjstvo
    return None

def seznam_uporabnika(uporabnisko_ime):
    global gospodinjstva
    moja_gospodinjstva = []
        
    for gospodinjstvo in gospodinjstva:
        if uporabnisko_ime in gospodinjstvo.clani:
            moja_gospodinjstva.append(gospodinjstvo.ime)
            
    return moja_gospodinjstva

def dodaj(ime, geslo, lastnik):
    global gospodinjstva
    
    if ime == "" or geslo == "":
        raise Exception("Polja za uporabniško ime ali geslo ne smete pustiti praznega")

    if poisci_z_imenom(ime) is not None:
        raise Exception("ime_zasedeno")
    else:
        gospodinjstva.append(Gospodinjstvo(ime,  hashSHA256(geslo), [lastnik], [], []))
    
    shrani()

def dodaj_jed(ime, jed):
    global gospodinjstva
    gospodinjstvo = poisci_z_imenom(ime)
    jedi = [j["ime_jedi"] for j in gospodinjstvo.jedi]
    
    if jed not in jedi and jed != "":
        gospodinjstvo.jedi.append({"ime_jedi": jed, "všeč": [], "ni všeč": []})
    
    shrani()

def obtezi(jedi, clani_gospodinjstva):
    seznam = []
    for jed in jedi:
        z = len(clani_gospodinjstva) + 1
        z += len(jed["všeč"])
        z -= len(jed["ni všeč"])
        while z:
            seznam.append(jed["ime_jedi"])
            z -= 1

    return seznam

def izberi(obtezen_seznam, koliko):
    izbrani = []
    while koliko:
        izbira = random.choice(obtezen_seznam)
        while izbira in obtezen_seznam:
            obtezen_seznam.remove(izbira)
        izbrani.append(izbira)
        koliko -= 1

    return izbrani
    
def zgeneriraj_jedilnik(ime, teden):
    global gospodinjstva
    prazni = 0
    
    gospodinjstvo = poisci_z_imenom(ime)
    jedi = [jed["ime_jedi"] for jed in gospodinjstvo.jedi]
            
    for dan in teden:
        if dan == "":
            prazni += 1

    if len(gospodinjstvo.jedi) < prazni:
        raise Exception("V bazi ni dovolj jedi")

    j = gospodinjstvo.jedi
    c = gospodinjstvo.clani

    obtezene_jedi = obtezi(j, c)
    dodaj = izberi(obtezene_jedi, prazni)

    for i, dan in enumerate(teden):
        if dan == "":
            teden[i] = dodaj[prazni - 1]
            prazni -= 1
        elif dan not in jedi:
            gospodinjstvo.jedi.append({"ime_jedi": dan, "všeč": [], "ni všeč": []})
            
    for gospodinjstvo in gospodinjstva:
        if gospodinjstvo.ime == ime:
            gospodinjstvo.jedilniki.insert(0, teden)

    shrani()

def zapusti_gospodinjstvo(ime_gospodinjstva, uporabnisko_ime):
    global gospodinjstva
    gospodinjstvo = poisci_z_imenom(ime_gospodinjstva)
    gospodinjstvo.clani.remove(uporabnisko_ime)
    for jed in gospodinjstvo.jedi:
        if uporabnisko_ime in jed["všeč"]:
            jed["všeč"].remove(uporabnisko_ime)
        if uporabnisko_ime in jed["ni všeč"]:
            jed["ni všeč"].remove(uporabnisko_ime)
            
    shrani()
    
def izbriši_jed(ime_gospodinjstva, ime_jedi):
    global gospodinjstva
    gospodinjstvo = poisci_z_imenom(ime_gospodinjstva)   
    for j in gospodinjstvo.jedi:
        if j["ime_jedi"] == ime_jedi:
            jed = j
    gospodinjstvo.jedi.remove(jed)
            
    shrani()
    
def izbriši_jedilnik(ime_gospodinjstva, indeks):
    global gospodinjstva
    gospodinjstvo = poisci_z_imenom(ime_gospodinjstva)
    gospodinjstvo.jedilniki.pop(int(indeks))
            
    shrani()

def všečkaj(uporabnik, ime_gospodinjstva, ime_jedi):
    global gospodinjstva
    gospodinjstvo = poisci_z_imenom(ime_gospodinjstva)

    for j in gospodinjstvo.jedi:
        if j["ime_jedi"] == ime_jedi:
            if uporabnik in j["všeč"]:
                j["všeč"].remove(uporabnik)
            else:
                j["všeč"].append(uporabnik)

    shrani()

def nevšečkaj(uporabnik, ime_gospodinjstva, ime_jedi):
    global gospodinjstva
    gospodinjstvo = poisci_z_imenom(ime_gospodinjstva)

    for j in gospodinjstvo.jedi:
        if j["ime_jedi"] == ime_jedi:
            if uporabnik in j["ni všeč"]:
                j["ni všeč"].remove(uporabnik)
            else:
                j["ni všeč"].append(uporabnik)

    shrani()
