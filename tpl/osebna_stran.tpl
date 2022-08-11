% rebase('tpl/base.tpl', title="Jedilnik")
    <div class = "glava">
        <a class = "uporabnik" href="/osebna_stran"> {{ime}} </a>
        <div class = "glava-desno">
            <a href="/zamenjaj_geslo"> Zamenjaj geslo </a>
            <a href="/odjava"> Odjava </a>
        </div>
    </div>
    
    <div class = "osnovno">
        <p>Moja gospodinjstva:</p>
        <ul>
        %for gospodinjstvo in gospodinjstva:
        <li>
        <a class = "alineja" href="/stran_gospodinjstva/{{gospodinjstvo}}"> {{gospodinjstvo}} </a>
        <a class = "gumbek1" href="/zapusti_gospodinjstvo/{{gospodinjstvo}}"> Zapusti gospodinjstvo </a>
        </li>
        %end
        </ul>
    
    
        <a class = "gumbek2" href="/dodaj_gospodinjstvo"> Dodaj gospodinjstvo </a>
        <a class = "gumbek2" href="/pridruzi_se"> Pridruži se novemu gospodinjstvu </a>
    </div>

%end
