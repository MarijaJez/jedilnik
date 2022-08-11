% rebase('tpl/base.tpl', title="Jedilnik")

    <div class="na-sredini">
        <div class="zozano">
            <h1> Napaka </h1>
            <p>Gospodinjstvo z imenom "{{ime_gospodinjstva}}" že obstaja. Če se želite pridružiti 
                že obstoječemu gospodinjstvu s tem imenom, izberite prvo možnost, če želite ustvariti 
                novo gospodinjstvo, pa izberite novo ime in drugo možnost.</p>
            <div class = "gumbi">
                <a class = "gumb" href="/pridruzi_se"> Pridruži se gospodinjstvu "{{ime_gospodinjstva}}"</a>
                <a  class = "gumb" href="/dodaj_gospodinjstvo"> Ustvari novo gospodinjstvo </a>
            </div>
            <a href="/osebna_stran"> Nazaj na osebno stran </a>
        </div>
    </div>
%end