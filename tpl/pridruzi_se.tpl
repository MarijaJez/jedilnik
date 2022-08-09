<!DOCTYPE html>
<html>
<head>
    <title>Jedilnik</title>
</head>
<body>
<h1> Pridruži se že obsoječemu gospodinjstvu! </h1>
Prosi skrbnika gospodinjstva, da ti zaupa ime gospodinjstva in geslo in se pridruži gospodinjstvu!
<form action="/pridruzi_se" method="POST">
    <label for="ime_gospodinjstva">Ime gospodinjstva:</label>
    <input type="text" id="ime_gospodinjstva" name="ime_gospodinjstva"><br><br>
    <label for="geslo">Geslo:</label>
    <input type="password" id="geslo" name="geslo"><br><br>
    <input type="submit" value="Pridruži se!">
</form>
</body>

</html>