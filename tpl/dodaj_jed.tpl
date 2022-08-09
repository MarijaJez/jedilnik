<!DOCTYPE html>
<html>
<head>
    <title>Jedilnik</title>
    <meta charset='utf8'>
</head>
<body>
<h1> Dodaj jed! </h1>
<form action="/dodaj_jed/{{ime_gospodinjstva}}" method="POST">
    <label for="ime_jedi">Ime jedi:</label>
    <input type="text" id="ime_jedi" name="ime_jedi"><br><br>
    <input type="submit" value="Dodaj!">
</form>
</body>

</html>