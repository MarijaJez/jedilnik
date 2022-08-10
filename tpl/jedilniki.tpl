<!DOCTYPE html>
<html>
<head>
    <title>Jedilnik</title>
</head>
<body>
<h1>{{ime_gospodinjstva}}</h1>

%for indeks, jedilnik in enumerate(jedilniki):
<table border="1">
    %imena_dnevov = ["ponedeljek", "torek", "sreda", "četrtek", "petek", "sobota", "nedelja"]
    %for dan, jed in zip(imena_dnevov, jedilnik):
        <tr>
            <td>{{dan}}</td>
            <td>{{jed}}</td>
        </tr>
    %end
<a href='/izbriši_jedilnik/{{ime_gospodinjstva}}/{{indeks}}'> Izbriši ta jedilnik. </a>
%end
</table>

<a href='/nov_jedilnik/{{ime_gospodinjstva}}'> Ustvarite nov jedilnik. </a>
<a href='/stran_gospodinjstva/{{ime_gospodinjstva}}'> Nazaj na stran gospodinjstva. </a>

<a href='/osebna_stran'> Nazaj na osebno stran. </a>
</body>

</html>