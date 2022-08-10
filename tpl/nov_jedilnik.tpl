<!DOCTYPE html>
<html>
<head>
    <title>Jedilnik</title>
</head>
<body>
<h1> Ustvarite nov jedilnik! </h1>
Če za katere dneve že veste, kaj bi radi jedli, vpišite v obrazec, sicer pa se bodo prazna mesta zapolnila sama.
<form action="/nov_jedilnik/{{ime_gospodinjstva}}" method="POST">
    <label for="ponedeljek"> Ponedeljek: </label>
    <input type="text" id="ponedeljek" name="ponedeljek"><br><br>
    <label for="torek"> torek: </label>
    <input type="text" id="torek" name="torek"><br><br>
    <label for="sreda"> sreda: </label>
    <input type="text" id="sreda" name="sreda"><br><br>
    <label for="četrtek"> četrtek: </label>
    <input type="text" id="četrtek" name="četrtek"><br><br>
    <label for="petek"> petek: </label>
    <input type="text" id="petek" name="petek"><br><br>
    <label for="sobota"> sobota: </label>
    <input type="text" id="sobota" name="sobota"><br><br>
    <label for="nedelja"> nedelja: </label>
    <input type="text" id="nedelja" name="nedelja"><br><br>
    <input type="submit" value="Ustvari!">
</form>
</body>

</html>