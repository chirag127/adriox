from time import sleep
import streamlit as st
import requests
from PIL import Image
import flagpy as fp
from streamlit_javascript import st_javascript

st.set_page_config(page_title="My IP Address and Location", page_icon=":guardsman:", layout="wide")
proxyUrl  = False
def client_response_json():

    url = 'https://ipapi.co/json/'

    script = (f'await fetch("{url}").then('
                'function(response) {'
                    'return response.json();'
                '})')

    try:
        result = st_javascript(script)
        if isinstance(result, dict):
            parsed_json = result


            return parsed_json

        return result

    except:
        pass


response = client_response_json()

print(response)

try:

    if response["error"]:
        st.error("Error: " + response["reason"])
        st.error(response["message"])
        st.stop()
except KeyError:
    pass
except TypeError:
    pass


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

st.subheader("Additional information")

st.markdown("Continent Code: **" + response["continent_code"] + "**")
st.markdown("Currency: **" + response["currency"] + "**")
st.markdown("Country Population: **" + str(response["country_population"]) + "**")
st.markdown("Country Area: **" + str(response["country_area"]) + "**")



st.subheader("Country Flag")
img = fp.get_flag_img(response["country_name"])
st.image(img, use_column_width=False)



st.subheader("Map Location")
map_url = f"https://www.google.com/maps/place/{response['latitude']},{response['longitude']}"

# make a link to go to the map
st.markdown(f"[Open in Google Maps]({map_url})")

# show the image of the map using openstreetmap
