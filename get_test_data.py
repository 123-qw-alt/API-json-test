import json
import ssl
from urllib.request import urlopen


def get_api_json():
    data_1 = []
    data_2 = []
    # Cancel SSL certificate verification
    context = ssl._create_unverified_context()
    # visit url
    f = urlopen("https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false", context=context)
    # Write the contents of the url to the json file
    j = json.load(f)
    file = open("data.json", "w", encoding="utf8")
    json.dump(j["Promotions"], file, ensure_ascii=False)
    file.close()
    # Extract the part of the dictionary that key is Promotions
    # Store the key and value in data_1 and data_b respectively and return it
    for dic in j["Promotions"]:
        data_list = []
        expect_list = []
        for key, value in dic.items():
            data_list.append(key)
            expect_list.append(value)
        data_1.append(data_list)
        data_2.append(expect_list)
    return data_1, data_2



#test