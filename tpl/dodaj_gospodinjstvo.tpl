<!DOCTYPE html>
<html>
<head>
    <title>Jedilnik</title>
</head>
<body>
<h1> Novo gospodinjstvo </h1>
Da ustvarite svoje gospodinjstvo, vnesite njegovo ime in željeno geslo, ki si ga nujno zapomnite, saj ga boste morali posredovati ostalim uporabnikom, ki se bodo želeli pridružiti vašemu gospodinjstvu.
<form action="/dodaj_gospodinjstvo" method="POST">
    <label for="ime_gospodinjstva">Ime gospodinjstva:</label>
    <input type="text" id="ime_gospodinjstva" name="ime_gospodinjstva"><br><br>
    <label for="geslo">Geslo:</label>
    <input type="password" id="geslo" name="geslo"><br><br>
    <input type="submit" value="Ustvarite svoje gospodinjstvo!">
</form>
</body>

</html>