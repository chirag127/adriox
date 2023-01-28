fetch('https://ipapi.co/json/')
  .then(response => response.json())
  .then(data => {
    let ipInfo = document.getElementById('ip-info');
    for (let key in data) {
      let card = document.createElement('div');
      card.classList.add('ip-info-card');
      let heading = document.createElement('h2');
      heading.textContent = key;
      let paragraph = document.createElement('p');
      paragraph.textContent = data[key];
      card.appendChild(heading);
      card.appendChild(paragraph);
      ipInfo.appendChild(card);
    }
  })
  .catch(error => console.error(error));
