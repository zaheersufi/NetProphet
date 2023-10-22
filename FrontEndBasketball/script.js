function getYear(boolean) {
  let year = document.querySelector('.dropdown').value;
  alert(year);
}

function displayData() {
 
}

fetch("data.json")
.then(function(response) {
  return response.json();
})
.then(function(players) {
  let placeholder = document.querySelector("#data-output");
  let out = "";
  for (let player of players) {
    out += `
        <tr>
          <td>${player.name}</td>
          <td>${player.name}</td>
          <td>${player.name}</td>
          <td>${player.name}</td>
        </tr>
    `;
  }
  placeholder.innerHTML = out;
})

