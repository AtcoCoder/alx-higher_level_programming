$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, status) {
    let characterName = data.name;
    $('DIV#character').text(characterName);
})