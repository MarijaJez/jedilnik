<!DOCTYPE html>
<html>
<head>
    <title>Jedilnik</title>
</head>
<body>
<h1>{{ime_gospodinjstva}}</h1>

%for jedilnik in jedilniki:
<table border="1">
    %for jed in jedilnik:
        <tr>
            <td>{{jed}}</td>
        </tr>
    %end
%end
</table>

<a href='/nov_jedilnik/{{ime_gospodinjstva}}'> Ustvarite nov jedilnik. </a>
<a href='/stran_gospodinjstva/{{ime_gospodinjstva}}'> Nazaj na stran gospodinjstva. </a>

<a href='/osebna_stran'> Nazaj na osebno stran. </a>
</body>

</html>