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
%for jed in jedi:
    <li>
    {{jed}}
    </li>
</ul>
%end

<a href='/dodaj_jed/{{ime_gospodinjstva}}'> Dodajte novo jed. </a>
<a href='/nov_jedilnik/{{ime_gospodinjstva}}'> Ustvarite nov jedilnik. </a>
<a href='/jedilniki/{{ime_gospodinjstva}}'> Vaši jedilniki </a>

<a href='/osebna_stran'> Nazaj na osebno stran. </a>
</body>

</html>