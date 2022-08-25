import json
from pomozne_funkcije import hashSHA256


class Uporabniki:
    def __init__(self):
        with open("uporabniki.json", encoding="utf8") as d:
            try:
                surovi_uporabniki = json.loads(d.read())
            except:
                surovi_uporabniki = []

            self.uporabniki = [Uporabnik(self, u["ime"], u["geslo"]) for u in surovi_uporabniki]


    def shrani(self):
        with open("uporabniki.json", "w", encoding="utf8") as f:
            json.dump(
                [(uc := u.__dict__.copy(), uc.pop("uporabniki", None), uc)[2] for u in self.uporabniki],
                f,
                ensure_ascii=False,
                default=lambda o: o.__dict__,
                sort_keys=False,
                indent=4,
            )


    def poisci(self, uporabnisko_ime, geslo):
        for uporabnik in self.uporabniki:
            if uporabnisko_ime == uporabnik.ime and hashSHA256(geslo) == uporabnik.geslo:
                return uporabnik
        return None


    def poisci_z_imenom(self, uporabnisko_ime):
        for uporabnik in self.uporabniki:
            if uporabnisko_ime == uporabnik.ime:
                return uporabnik

        return None


    def dodaj(self, uporabnisko_ime, geslo, potrditev):
        if uporabnisko_ime == "" or geslo == "":
            raise Exception("Polja za uporabniško ime ali geslo ne smete pustiti praznega")

        if self.poisci_z_imenom(uporabnisko_ime) is None:
            if geslo == potrditev:
                self.uporabniki.append(Uporabnik(self, uporabnisko_ime, hashSHA256(geslo)))
            else:
                raise Exception("Gesli se ne ujemata")
        else:
            raise Exception(
                f"Uporabniško ime '{uporabnisko_ime}' že obstaja! Izberite si novo ime in se poskusite ponovno registrirati."
            )

        self.shrani()


class Uporabnik:
    def __init__(self, uporabniki, ime, geslo):
        self.uporabniki = uporabniki
        self.ime = ime
        self.geslo = geslo

    
    def zamenjaj_geslo(self, geslo, novo_geslo, potrditev):
        if geslo == self.geslo:
            if novo_geslo == potrditev:
                self.geslo = hashSHA256(novo_geslo)
            else:
                raise Exception("Gesli se ne ujemata")
        else:
            raise Exception("Napačno geslo")

        self.uporabniki.shrani()