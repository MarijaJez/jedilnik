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
    if poisci_z_imenom(ime) is not None:
        raise Exception("To ime gospodinjstva je že zasedeno")
    else:
        gospodinjstva.append(Gospodinjstvo(ime,  hashSHA256(geslo), [lastnik], [], []))
    
    shrani()

def dodaj_jed(ime, jed):
    global gospodinjstva
    gospodinjstvo = poisci_z_imenom(ime)
    
    if jed not in gospodinjstvo.jedi:
        gospodinjstvo.jedi.append(jed)
    
    shrani()
    
def zgeneriraj_jedilnik(ime, teden):
    global gospodinjstva
    prazni = 0
    
    gospodinjstvo = poisci_z_imenom(ime)
    jedi = gospodinjstvo.jedi
            
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
        if gospodinjstvo.ime == ime:
            gospodinjstvo.jedilniki.append(teden)

    shrani()

def zapusti_gospodinjstvo(ime_gospodinjstva, uporabnisko_ime):
    global gospodinjstva
    gospodinjstvo = poisci_z_imenom(ime_gospodinjstva)
    gospodinjstvo.clani.remove(uporabnisko_ime)
            
    shrani()
    
def izbriši_jed(ime_gospodinjstva, ime_jedi):
    global gospodinjstva
    gospodinjstvo = poisci_z_imenom(ime_gospodinjstva)   
    gospodinjstvo.jedi.remove(ime_jedi)
            
    shrani()
    
def izbriši_jedilnik(ime_gospodinjstva, indeks):
    global gospodinjstva
    gospodinjstvo = poisci_z_imenom(ime_gospodinjstva)
    gospodinjstvo.jedilniki.pop(int(indeks))
            
    shrani()