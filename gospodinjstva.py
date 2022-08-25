import json
from pomozne_funkcije import hashSHA256, izberi


class Gospodinjstva:
    def __init__(self):
        with open("gospodinjstva.json", encoding="utf8") as d:
            try:
                surova_gospodinjstva = json.loads(d.read())
            except:
                surova_gospodinjstva = []

            self.gospodinjstva = [
                Gospodinjstvo(self, g["ime"], g["geslo"], g["clani"], g["jedi"], g["jedilniki"])
                for g in surova_gospodinjstva
            ]


    def shrani(self):
        with open("gospodinjstva.json", "w", encoding="utf8") as f:
            json.dump(
                [(gc := g.__dict__.copy(), gc.pop("gospodinjstva", None), gc)[2] for g in self.gospodinjstva],
                f,
                ensure_ascii=False,
                default=lambda o: o.__dict__,
                sort_keys=False,
                indent=4,
            )


    def poisci(self, ime, geslo):
        for gospodinjstvo in self.gospodinjstva:
            if ime == gospodinjstvo.ime and hashSHA256(geslo) == gospodinjstvo.geslo:
                return gospodinjstvo
        return None


    def poisci_z_imenom(self, ime):
        for gospodinjstvo in self.gospodinjstva:
            if ime == gospodinjstvo.ime:
                return gospodinjstvo
        return None


    def seznam_uporabnika(self, uporabnisko_ime):
        moja_gospodinjstva = []

        for gospodinjstvo in self.gospodinjstva:
            if uporabnisko_ime in gospodinjstvo.clani:
                moja_gospodinjstva.append(gospodinjstvo.ime)

        return moja_gospodinjstva


    def dodaj(self, ime, geslo, lastnik):
        if ime == "" or geslo == "":
            print(ime, geslo)
            raise Exception("Polja za uporabniško ime ali geslo ne smete pustiti praznega")

        if self.poisci_z_imenom(ime) is not None:
            raise Exception("ime_zasedeno")
        else:
            self.gospodinjstva.append(Gospodinjstvo(self, ime, hashSHA256(geslo), [lastnik], [], []))

        self.shrani()


class Gospodinjstvo:
    def __init__(self, gospodinjstva, ime, geslo, clani, jedi, jedilniki):
        self.gospodinjstva = gospodinjstva
        self.ime = ime
        self.geslo = geslo
        self.clani = clani
        self.jedi = jedi
        self.jedilniki = jedilniki


    def dodaj_clana(self, ime):
        if ime not in self.clani:
            self.clani.append(ime)
            self.gospodinjstva.shrani()
        else:
            raise Exception("V tem gospodinjstvu ste že včlanjeni.")

    
    def dodaj_jed(self, jed):
        jedi = [j["ime_jedi"] for j in self.jedi]

        if jed not in jedi and jed != "":
            self.jedi.append({"ime_jedi": jed, "všeč": [], "ni všeč": []})

        self.gospodinjstva.shrani()


    def obtezi(self):
        seznam = []
        for jed in self.jedi:
            z = len(self.clani) + 1
            z += len(jed["všeč"])
            z -= len(jed["ni všeč"])
            while z:
                seznam.append(jed["ime_jedi"])
                z -= 1

        return seznam


    def zgeneriraj_jedilnik(self, teden):
        prazni = 0
        jedi = [jed["ime_jedi"] for jed in self.jedi]

        for dan in teden:
            if dan == "":
                prazni += 1

        if len(self.jedi) < prazni:
            raise Exception("V bazi ni dovolj jedi")

        obtezene_jedi = self.obtezi()
        dodaj = izberi(obtezene_jedi, prazni)

        for i, dan in enumerate(teden):
            if dan == "":
                teden[i] = dodaj[prazni - 1]
                prazni -= 1
            elif dan not in jedi:
                self.jedi.append({"ime_jedi": dan, "všeč": [], "ni všeč": []})

        self.jedilniki.insert(0, teden)

        self.gospodinjstva.shrani()


    def zapusti_gospodinjstvo(self, uporabnisko_ime):
        self.clani.remove(uporabnisko_ime)
        for jed in self.jedi:
            if uporabnisko_ime in jed["všeč"]:
                jed["všeč"].remove(uporabnisko_ime)
            if uporabnisko_ime in jed["ni všeč"]:
                jed["ni všeč"].remove(uporabnisko_ime)

        self.gospodinjstva.shrani()


    def izbriši_jed(self, ime_jedi):
        for j in self.jedi:
            if j["ime_jedi"] == ime_jedi:
                jed = j
        self.jedi.remove(jed)

        self.gospodinjstva.shrani()


    def izbriši_jedilnik(self, indeks):
        self.jedilniki.pop(int(indeks))

        self.gospodinjstva.shrani()


    def všečkaj(self, uporabnik, ime_jedi):
        for j in self.jedi:
            if j["ime_jedi"] == ime_jedi:
                if uporabnik in j["všeč"]:
                    j["všeč"].remove(uporabnik)
                else:
                    j["všeč"].append(uporabnik)

        self.gospodinjstva.shrani()


    def nevšečkaj(self, uporabnik, ime_jedi):
        for j in self.jedi:
            if j["ime_jedi"] == ime_jedi:
                if uporabnik in j["ni všeč"]:
                    j["ni všeč"].remove(uporabnik)
                else:
                    j["ni všeč"].append(uporabnik)

        self.gospodinjstva.shrani()


