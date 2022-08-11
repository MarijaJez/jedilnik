<!DOCTYPE html>
<html>
<head>
    <title>Jedilnik</title>
</head>
<body>
<h1>Zamenjaj geslo</h1>
<form action="/zamenjaj_geslo" method="POST">
    <label for="geslo">Sedanje geslo:</label>
    <input type="password" id="geslo" name="geslo"><br><br>
    <label for="novo_geslo">Novo geslo:</label>
    <input type="password" id="novo_geslo" name="novo_geslo"><br><br>
    <label for="potrditev">Potrdite novo geslo:</label>
    <input type="password" id="potrditev" name="potrditev"><br><br>
    <input type="submit" value="Zamenjaj geslo">
</form>
</body>

</html>