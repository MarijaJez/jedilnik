% rebase('tpl/base.tpl', title="Jedilnik")
    <div class = "glava">
        <a class = "uporabnik" href="/osebna_stran"> {{ime}} </a>
    </div>

    <div class = "glava-gospodinjstva">
        <a class = "gospodinjstvo"> {{ime_gospodinjstva}} </a>
        <div class = "glava-desno">
            <a class = "gumbek2" href="/nov_jedilnik/{{ime_gospodinjstva}}"> Nov jedilnik </a>
            <a class = "gumbek2" href="/jedilniki/{{ime_gospodinjstva}}"> Vaši jedilniki </a>
            <a class = "gumbek2" href="/zapusti_gospodinjstvo/{{ime_gospodinjstva}}"> Zapusti gospodinjstvo </a>
        </div>
    </div>

    <div class = "row">
        <div class = "column middle">
            <p>Člani gospodinjstva:</p>
            <ul>
            %for clan in clani:
                <li>
                {{clan}}
                </li>
            %end
            </ul>
        
            <p>Vaše jedi:</p>
            <ul>
            %for ime_jedi in jedi:
                <li>
                {{ime_jedi}}
                <a class = "gumbek1" href="/izbriši_jed/{{ime_gospodinjstva}}/{{ime_jedi}}"> Izbriši </a>
                </li>
            %end
            </ul>
            <a class = "gumbek2" href="/dodaj_jed/{{ime_gospodinjstva}}"> Dodajte novo jed </a>
        </div>
    
        <div class = "column side">
            <p>Trenutni jedilnik:</p>
        
            %if len(jedilniki) > 0:
                %jedilnik = jedilniki[0]
                <table>
                    %imena_dnevov = ["ponedeljek", "torek", "sreda", "četrtek", "petek", "sobota", "nedelja"]
                    %for dan, jed in zip(imena_dnevov, jedilnik):
                        <tr>
                            <td>{{dan}}</td>
                            <td>{{jed}}</td>
                        </tr>
                    %end
                </table>
            %else:
                <p>Nimate še jedilnika za prikaz.</p>
            %end
        </div>
    </div>


%end