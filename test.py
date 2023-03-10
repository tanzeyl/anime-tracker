import http.client
import json

# conn = http.client.HTTPSConnection("anime-db.p.rapidapi.com")
# headers = {
#     'X-RapidAPI-Key': "afb343f435msh201413b2885819ep1b98fdjsn17ca616f6885",
#     'X-RapidAPI-Host': "anime-db.p.rapidapi.com"
#     }

# conn.request("GET", "/anime?page=1&size=10&search=demon%20slayer&sortBy=ranking&sortOrder=desc", headers=headers)
# res = conn.getresponse()
# data = res.read()
# res = json.loads(data.decode("utf-8"))

# allInfo = []
# for i in range(len(res["data"])):
#   current = {}
#   current["name"] = res["data"][i]["title"]
#   current["genres"] = res["data"][i]["genres"]
#   current["image"] = res["data"][i]["image"]
#   current["type"] = res["data"][i]["type"]
#   allInfo.append(current)

# for anime in allInfo:
#   print(f"Name: {anime['name']}")
#   print(f"genres: {anime['genres']}")
#   print(f"Image Link: {anime['image']}")
#   print(f"Type: {anime['type']}")
#   print("\n")

query = "adcd slknf"
s = query.split()
q = ""
for word in s:
  q += word + "%20"
  # q = q[:-3]
print(q[:-3])
