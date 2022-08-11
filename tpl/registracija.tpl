% rebase('tpl/base.tpl', title="Jedilnik")

    <div class="na-sredini">
        <div class="zozano">
            <h1>Registracija</h1>
                <form action="/registracija" method="POST">
                    <label for="ime">Ime:</label>
                    <input type="text" id="ime" name="ime"><br><br>
                    <label for="geslo">Geslo:</label>
                    <input type="password" id="geslo" name="geslo"><br><br>
                    <label for="potrditev">Potrdite novo geslo:</label>
                    <input type="password" id="potrditev" name="potrditev"><br><br>
                    <input class="gumb" type="submit" value="Registrirajte se!">
                </form>
        </div>
    </div>

%end