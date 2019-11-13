# Code by Wilko Grunefeld.
# licensed under AGPLv3
# See https://github.com/yetanothercarbot/qld_fire_finder

# Build command (windows):
# py -3 -m PyInstaller --onefile .\fire_finder.py --distpath out

import math, requests
from bs4 import BeautifulSoup

# Check if location has already been entered
print("\n\n##########################")
print("#   Fire Finder v1.0.3   #")
print("##########################\n\n")
try:
    f = open('location.txt', 'r')
    home_pos = f.readline().split()
    f.close()
    print("You have run this program before, so I am using the same location as last")
    print("time. If you wish to use a different location, please delete the location")
    print("file that is in the same folder as this program, and restart this software.")
except FileNotFoundError:
    print("Please insert latitude and longitude of your position. This can be")
    print("found using Google Maps - find your position, right-click and select")
    print("\"What's Here?\". Click on the coordinates shown in the bottom, and")
    print("then copy and paste the coordinates in the search box here. It should")
    print("look similar to this: -27.484932, 152.959432")
    given_input = input("> ").replace(",", "")
    print("\nThank you. I will save this for when you rerun the software later.")
    f = open('location.txt', 'w')
    f.write(given_input + '\n')
    f.close()
    home_pos = given_input.split()

home_pos = [float(x) for x in home_pos]

def calculate_distance(pos1, pos2):
    lat1, lon1 = pos1
    lat2, lon2 = pos2
    R = 6371e3; # metres
    φ1 = lat1 * math.pi/180
    φ2 = lat2 * math.pi/180
    Δφ = (lat2-lat1) * math.pi/180
    Δλ = (lon2-lon1) * math.pi/180

    a = math.sin(Δφ/2) * math.sin(Δφ/2) + \
        math.cos(φ1)  *  math.cos(φ2) * \
        math.sin(Δλ/2) * math.sin(Δλ/2);
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));

    d = R * c;
    return round(d*1)/1000

closest_fire = {"name": None, "distance": 0, "location": None, "info": None}

print("---\nPLEASE NOTE: Software is susceptible to bugs, and this is no\n"
      +"different. Do not rely on Fire Finder to always give correct information\n"
      +"and please stay safe during fire season. We are not responsible for\n"
      +"injuries, property losses, or other damages due to use of this software.\n"
      +"For more information on what to do during bushfires, please see QFES:\n"
      +"https://www.ruralfire.qld.gov.au/BushFire_Safety/Pages/default.aspx")
input("\nPress enter to continue.")
print("---\nLoading fire data...")
response = requests.get("https://www.qfes.qld.gov.au/data/alerts/bushfireAlert.xml")
if not response:
    print("Failed to fetch bushfire data.")
else:
    # data = BeautifulSoup(response.text, features="xml")
    data = BeautifulSoup(response.text, features="lxml")
    for index, item in enumerate(data.find_all('georss:point')):
        fire_pos = item.string.split()
        fire_pos = (float(fire_pos[0]), float(fire_pos[1]))

        fire_distance = calculate_distance(home_pos, fire_pos)
        if closest_fire["name"] is None or fire_distance < closest_fire["distance"]:
            closest_fire["name"] = data.find_all('title')[index+1].string
            closest_fire["info"] = data.find_all('content')[index].string
            closest_fire["location"] = item.string
            closest_fire["distance"] = fire_distance
    print(f"---\nThe closest fire is {closest_fire['distance']}km away, at {closest_fire['name']}")
    print(closest_fire["info"])
input("---\nPress enter to quit.") # Show regardless if request failed or not.
