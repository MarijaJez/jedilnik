% rebase('tpl/base.tpl', title="Jedilnik")

    <div class="na-sredini">
        <div class="zozano">
            <h1> Ustvarite nov jedilnik! </h1>
            <p>Če za katere dneve že veste, kaj bi radi jedli, vpišite v obrazec, sicer pa se bodo 
            prazna mesta zapolnila sama.</p>
            <form action="/nov_jedilnik/{{ime_gospodinjstva}}" method="POST">
                <label for="ponedeljek"> Ponedeljek: </label>
                <input type="text" id="ponedeljek" name="ponedeljek"><br><br>
                <label for="torek"> Torek: </label>
                <input type="text" id="torek" name="torek"><br><br>
                <label for="sreda"> Sreda: </label>
                <input type="text" id="sreda" name="sreda"><br><br>
                <label for="cetrtek"> Četrtek: </label>
                <input type="text" id="cetrtek" name="cetrtek"><br><br>
                <label for="petek"> Petek: </label>
                <input type="text" id="petek" name="petek"><br><br>
                <label for="sobota"> Sobota: </label>
                <input type="text" id="sobota" name="sobota"><br><br>
                <label for="nedelja"> Nedelja: </label>
                <input type="text" id="nedelja" name="nedelja"><br><br>
                <input class = "gumb" type="submit" value="Ustvari!">
            </form>
        </div>
    </div>
    <a href="/stran_gospodinjstva/{{ime_gospodinjstva}}"> Nazaj na stran gospodinjstva. </a>

%end