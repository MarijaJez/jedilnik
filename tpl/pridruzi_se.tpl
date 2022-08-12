% rebase('tpl/base.tpl', title="Jedilnik")

<div class="glava">
    <a class="uporabnik" href="/osebna_stran"> {{ime}} </a>
</div>

<div class="na-sredini">
    <div class="zozano">
        <h1> Pridružite se gospodinjstvu! </h1>
        <p>Prosite skrbnika gospodinjstva, da vam zaupa ime gospodinjstva in geslo, in se pridružite gospodinjstvu!</p>
        <form action="/pridruzi_se" method="POST">
            <label for="ime_gospodinjstva">Ime gospodinjstva:</label>
            <input type="text" id="ime_gospodinjstva" name="ime_gospodinjstva"><br><br>
            <label for="geslo">Geslo:</label>
            <input type="password" id="geslo" name="geslo"><br><br>
            <input class="gumb" type="submit" value="Pridružite se!">
        </form>
    </div>
</div>

%end