import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="My IP Address and Location", page_icon=":guardsman:", layout="wide")

response = requests.get("https://ipapi.co/json/").json()

try:
    # {'error': True, 'reason': 'RateLimited', 'message': 'Visit https://ipapi.co/ratelimited/ for details'}

    if response["error"]:
        st.error("Error: " + response["reason"])
        st.error(response["message"])
        st.stop()
except KeyError:
    pass

print(response)

# response = response.json()

st.title("IP address: " + response["ip"])

st.subheader("Location Information")

st.markdown("City: **" + response["city"] + "**")
st.markdown("Region: **" + response["region"] + "**")
st.markdown("Country: **" + response["country_name"] + "**")
st.markdown("Country Code: **" + response["country"] + "**")
st.markdown("Postal Code: **" + response["postal"] + "**")
st.markdown("Timezone: **" + response["timezone"] + "**")
st.markdown("Latitude: **" + str(response["latitude"]) + "**")
st.markdown("Longitude: **" + str(response["longitude"]) + "**")
st.markdown("ASN: **" + response["asn"] + "**")
st.markdown("Organization: **" + response["org"] + "**")

st.subheader("Map Location")
map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={response['latitude']},{response['longitude']}&size=800x800&zoom=14"
map_img = Image.open(requests.get(map_url, stream=True).raw)
st.image(map_img, use_column_width=True)

st.subheader("Country Flag")
flag_url = f"https://www.countryflags.io/{response['country_code']}/flat/64.png"
flag_img = Image.open(requests.get(flag_url, stream=True).raw)
st.image(flag_img, use_column_width=False)

st.subheader("Additional information")

st.markdown("Continent Code: **" + response["continent_code"] + "**")
st.markdown("Currency: **" + response["currency"] + "**")
st.markdown("Country Population: **" + str(response["country_population"]) + "**")
st.markdown("Country Area: **" + str(response["country_area"]) + "**")
