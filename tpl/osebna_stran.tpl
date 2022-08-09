<!DOCTYPE html>
<html>
<head>
    <title>Jedilnik</title>
</head>
<body>
<h1>Moj račun</h1>
Živjo, {{ime}}. <br>
Moja gospodinjstva:
<ul>
%for gospodinjstvo in gospodinjstva:
  <li>
  <a href='/stran_gospodinjstva/{{gospodinjstvo}}'> {{gospodinjstvo}} </a>
  </li>
</ul>
%end


<a href='/dodaj_gospodinjstvo'> Dodaj gospodinjstvo </a>
<a href='/pridruzi_se'> Pridruži se novemu gospodinjstvu </a>
<a href='/odjava'> Odjava </a>
</body>

</html>