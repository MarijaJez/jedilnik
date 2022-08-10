<!DOCTYPE html>
<html>
<head>
    <title>Jedilnik</title>
</head>
<body>
<h1> Novo gospodinjstvo </h1>
Da ustvarite svoje gospodinjstvo, vnesite njegovo ime in željeno geslo, ki si ga nujno zapomnite, saj ga boste morali posredovati ostalim uporabnikom, ki se bodo želeli pridružiti vašemu gospodinjstvu. Poleg tega vnesite še 7 svojih najljubših jedi, da bo generator zagotovo imel dovolj izbire vsaj za 1 teden :) .
<form action="/dodaj_gospodinjstvo" method="POST">
    <label for="ime_gospodinjstva">Ime gospodinjstva:</label>
    <input type="text" id="ime_gospodinjstva" name="ime_gospodinjstva"><br><br>
    <label for="geslo">Geslo:</label>
    <input type="password" id="geslo" name="geslo"><br><br>
    <label for="jed1">Jed 1:</label>
    <input type="text" id="jed1" name="jed1"><br><br>
    <label for="jed2">Jed 2:</label>
    <input type="text" id="jed2" name="jed2"><br><br>
    <label for="jed3">Jed 3:</label>
    <input type="text" id="jed3" name="jed3"><br><br>
    <label for="jed4">Jed 4:</label>
    <input type="text" id="jed4" name="jed4"><br><br>
    <label for="jed5">Jed 5:</label>
    <input type="text" id="jed5" name="jed5"><br><br>
    <label for="jed6">Jed 6:</label>
    <input type="text" id="jed6" name="jed6"><br><br>
    <label for="jed7">Jed 7:</label>
    <input type="text" id="jed7" name="jed7"><br><br>
    <input type="submit" value="Ustvarite svoje gospodinjstvo!">
</form>
</body>

</html>