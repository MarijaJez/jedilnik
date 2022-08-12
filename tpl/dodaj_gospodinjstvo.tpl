% rebase('tpl/base.tpl', title="Jedilnik")

<div class="glava">
    <a class="uporabnik" href="/osebna_stran"> {{ime}} </a>
</div>

<div class="na-sredini">
    <div class="zozano">
        <h1> Novo gospodinjstvo </h1>
        <p>Da ustvarite svoje gospodinjstvo, vnesite njegovo ime in željeno geslo,
            ki si ga nujno zapomnite, saj ga boste morali posredovati ostalim uporabnikom,
            ki se bodo želeli pridružiti vašemu gospodinjstvu.</p>
        <form action="/dodaj_gospodinjstvo" method="POST">
            <label for="ime_gospodinjstva">Ime gospodinjstva:</label>
            <input type="text" id="ime_gospodinjstva" name="ime_gospodinjstva"><br><br>
            <label for="geslo">Geslo:</label>
            <input type="password" id="geslo" name="geslo"><br><br>
            <input class="gumb" type="submit" value="Ustvarite svoje gospodinjstvo!">
        </form>
    </div>
</div>

%end