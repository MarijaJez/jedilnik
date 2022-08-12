% rebase('tpl/base.tpl', title="Jedilnik")

    <div class="na-sredini">
        <div class="zozano">
            <h1>{{naslov}}</h1>
            <p>{{opis}}</p>

            <div class="gumbi">
                <a class="gumb" href="{{povezava}}"> {{gumb}} </a>
            </div>
        </div>
    </div>

%end