% rebase('tpl/base.tpl', title="Jedilnik")

<div class="na-sredini">
    <div class="zozano">
        <h1>Prijava</h1>
        <form action="/prijava" method="POST">
            <label for="ime">Ime:</label>
            <input type="text" id="ime" name="ime"><br><br>
            <label for="geslo">Geslo:</label>
            <input type="password" id="geslo" name="geslo"><br><br>
            <input class="gumb" type="submit" value="Prijava">
        </form>
    </div>
</div>

%end