async function getIPLocation() {
  const response = await fetch("https://ipapi.co/json/");
  const data = await response.json();

  // Display IP address
  document.getElementById("ip").innerHTML = data.ip;

  // Display location information
  document.getElementById("city").innerHTML = data.city;
  document.getElementById("region").innerHTML = data.region;
  document.getElementById("country").innerHTML = data.country_name;
  document.getElementById("country-code").innerHTML = data.country;
  document.getElementById("postal").innerHTML = data.postal;
  document.getElementById("timezone").innerHTML = data.timezone;
  document.getElementById("latitude").innerHTML = data.latitude;
  document.getElementById("longitude").innerHTML = data.longitude;
  document.getElementById("asn").innerHTML = data.asn;
  document.getElementById("org").innerHTML = data.org;

  // Display additional information
  document.getElementById("continent-code").innerHTML = data.continent_code;
  document.getElementById("currency").innerHTML = data.currency;
  document.getElementById("country-population").innerHTML =
    data.country_population;
  document.getElementById("country-area").innerHTML = data.country_area;

  // Display country flag
  const flagImg = document.getElementById("flag-img");
  {
    /* <img
  src="https://flagcdn.com/144x108/za.png"
  width="144"
  height="108"
  alt="South Africa"> */
  }
  i = "https://flagcdn.com/192x144/" + data.country_code.toLowerCase() + ".png";

  flagImg.src = i;
  // flagImg.width = "144";
  // flagImg.height = "108";
  flagImg.alt = data.country_name;

  // give height and width to the   <div class="flag-section">

  const flagSection = document.getElementsByClassName("flag-section")[0];
  flagSection.style.height = "144px";
  flagSection.style.width = "192px";



  // Display map location
  const mapUrl = `https://www.google.com/maps/place/${data.latitude},${data.longitude}`;
  document.getElementById("map-link").href = mapUrl;
  const mapIframe = document.getElementById("map-iframe");
  mapIframe.src = `https://www.openstreetmap.org/export/embed.html?bbox=${
    data.longitude - 0.01
  },${data.latitude - 0.01},${data.longitude + 0.01},${
    data.latitude + 0.01
  }&layer=mapnik&marker=${data.latitude},${data.longitude}`;
}

getIPLocation();
