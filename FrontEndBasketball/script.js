function getYear(boolean) {
  let year = document.querySelector('.dropdown').value;
  alert(year);
  return year;
}

function displayData(yearDate) {

  /* passed in year */

  fetch("display-data.json")
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
          <td>${player.mvp}</td>
        </tr>
    `;
  }
  placeholder.innerHTML = out;
})

}

