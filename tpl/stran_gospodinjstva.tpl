<!DOCTYPE html>
<html>
<head>
    <title>Jedilnik</title>
</head>
<body>
<h1>{{ime_gospodinjstva}}</h1>

Člani gospodinjstva:
<ul>
%for član in člani:
    <li>
    {{član}}
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

<a href='/zgeneriraj_jedilnik'> Ustvarite nov jedilnik. </a>
<a href='/dodaj_jed/{{ime_gospodinjstva}}'> Dodajte novo jed. </a>
<a href='/osebna_stran'> Nazaj na osebno stran. </a>
</body>

</html>