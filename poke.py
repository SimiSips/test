import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=100',).json()
res_data = response['results']

length = len(res_data)
empty_list = []
for i in res_data:
    for l in range(0, 101):
        image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{}.png".format(l)
        #print(image_url)
        empty_list.append({
            'name': i['name'],
            'url': i['url'],
            'image_url': image_url,
        })


print(empty_list[2])


# for l in range(1, 101):
#     image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{}.png".format(l)
#     for j in res_data:
        
#         print(image_url + " / " + str(j))
    

print(len(res_data))