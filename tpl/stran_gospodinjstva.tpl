<!DOCTYPE html>
<html>
<head>
    <title>Jedilnik</title>
</head>
<body>
<h1>{{ime_gospodinjstva}}</h1>

Člani gospodinjstva:
<ul>
%for clan in clani:
    <li>
    {{clan}}
    </li>
</ul>
%end

Vaše jedi:
<ul>
%for ime_jedi in jedi:
    <li>
    {{ime_jedi}}
    <a href='/izbriši_jed/{{ime_gospodinjstva}}/{{ime_jedi}}'> Izbriši </a>
    </li>
</ul>
%end

<a href='/dodaj_jed/{{ime_gospodinjstva}}'> Dodajte novo jed. </a>
<a href='/nov_jedilnik/{{ime_gospodinjstva}}'> Ustvarite nov jedilnik. </a>
<a href='/jedilniki/{{ime_gospodinjstva}}'> Vaši jedilniki </a>
<a href='/zapusti_gospodinjstvo/{{ime_gospodinjstva}}'> Zapusti gospodinjstvo </a>

<a href='/osebna_stran'> Nazaj na osebno stran. </a>
</body>

</html>