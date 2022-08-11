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
  <a href='/zapusti_gospodinjstvo/{{gospodinjstvo}}'> Zapusti gospodinjstvo </a>
  </li>
%end
</ul>


<a href='/dodaj_gospodinjstvo'> Dodaj gospodinjstvo </a>
<a href='/pridruzi_se'> Pridruži se novemu gospodinjstvu </a>
<a href='/zamenjaj_geslo'> Zamenjaj_geslo </a>
<a href='/odjava'> Odjava </a>
</body>

</html>