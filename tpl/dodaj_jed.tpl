% rebase('tpl/base.tpl', title="Jedilnik")

<div class="na-sredini">
    <div class="zozano">
        <h1> Dodaj jed! </h1>
        <form action="/dodaj_jed/{{ime_gospodinjstva}}" method="POST">
            <label for="ime_jedi">Ime jedi:</label>
            <input type="text" id="ime_jedi" name="ime_jedi"><br><br>
            <input class="gumb" type="submit" value="Dodaj!">
        </form>
        <a href="/stran_gospodinjstva/{{ime_gospodinjstva}}"> Nazaj na stran gospodinjstva. </a>
    </div>
</div>

%end