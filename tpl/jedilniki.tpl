% rebase('tpl/base.tpl', title="Jedilnik")

<div class="glava">
    <a class="uporabnik" href="/osebna_stran"> {{ime}} </a>
</div>

<div class="glava-gospodinjstva">
    <a class="gospodinjstvo" href="/stran_gospodinjstva/{{ime_gospodinjstva}}"> {{ime_gospodinjstva}} </a>
    <div class="glava-desno">
        <a class="gumbek2" href="/nov_jedilnik/{{ime_gospodinjstva}}"> Nov jedilnik </a>
    </div>
</div>

<div class="osnovno">
    <p>Vaši jedilniki:</p>
    <div class="tabele">
        %for indeks, jedilnik in enumerate(jedilniki):
        <table>
            %imena_dnevov = ["ponedeljek", "torek", "sreda", "četrtek", "petek", "sobota", "nedelja"]
            %for dan, jed in zip(imena_dnevov, jedilnik):
            <tr>
                <td>{{dan}}</td>
                <td>{{jed}}</td>
            </tr>
            %end
        </table>
        <a class="gumbek2" href="/izbriši_jedilnik/{{ime_gospodinjstva}}/{{indeks}}"> Izbriši ta jedilnik. </a>
        %end
    </div>
</div>

%end