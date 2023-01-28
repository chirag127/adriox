$(document).ready(function () {
  // client_response_json function here
  function client_response_json() {
    $.getJSON("https://ipapi.co/json/", function (response) {
      if (response.error) {
        $("#error-message").text("Error: " + response.reason);
        $("#error-message").append("<br>" + response.message);
        $("#error-message").show();
        return;
      }
      $("#ip-address").text(response.ip);
      $("#city").text(response.city);
      $("#region").text(response.region);
      $("#country-name").text(response.country_name);
      $("#country-code").text(response.country);
      $("#postal-code").text(response.postal);
      $("#timezone").text(response.timezone);
      $("#latitude").text(response.latitude);
      $("#longitude").text(response.longitude);
      $("#asn").text(response.asn);
      $("#organization").text(response.org);
      $("#continent-code").text(response.continent_code);
      $("#currency").text(response.currency);
      $("#country-population").text(response.country_population);
      $("#country-area").text(response.country_area);
      var flagImg = new Image();
      flagImg.src =
        "https://flagpedia.net/data/flags/normal/" +
        response.country.toLowerCase() +
        ".png";
      $("#flag-img").append(flagImg);
      var mapUrl =
        "https://www.google.com/maps/place/" +
        response.latitude +
        "," +
        response.longitude;
      $("#map-link").attr("href", mapUrl);
    });
  }
  // call the function on page load
  client_response_json();
});
