import json
from json import JSONEncoder
import hashlib
from tkinter import image_names
from unittest import skip

def hashSHA256(s):
    h = hashlib.sha256(s.encode('utf8'))
    return h.hexdigest()

class Uporabnik:
    def __init__(self, ime, geslo):
        self.ime = ime
        self.geslo = geslo

uporabniki = []

def preberi():
    global uporabniki
    with open("uporabniki.json", encoding='utf8') as d:
        try:
            surovi_uporabniki = json.loads(d.read())
        except:
            surovi_uporabniki = []
        
        uporabniki = [Uporabnik(u['ime'], u['geslo']) for u in surovi_uporabniki]

def shrani():
    with open('uporabniki.json', 'w', encoding='utf8') as f:
        json.dump(uporabniki, f, ensure_ascii=False, default=lambda o: o.__dict__, sort_keys=False, indent=4)

def poisci(uporabnisko_ime, geslo):
    for uporabnik in uporabniki:
        if uporabnisko_ime == uporabnik.ime and hashSHA256(geslo) == uporabnik.geslo:
            return uporabnik
    return None

def poisci_z_imenom(uporabnisko_ime):
    for uporabnik in uporabniki:
        if uporabnisko_ime == uporabnik.ime:
            return uporabnik

    return None

def dodaj( uporabnisko_ime, geslo):
    if poisci_z_imenom(uporabnisko_ime) is not None:
        raise Exception("To uporabniško ime je že zasedeno")
    else:
        uporabniki.append(Uporabnik(uporabnisko_ime,  hashSHA256(geslo)))
    
    shrani()

def spremeni_geslo( uporabnisko_ime, novo_geslo):
    uporabnik = poisci_z_imenom(uporabnisko_ime)
    uporabnik.geslo = hashSHA256(novo_geslo)
    shrani()
