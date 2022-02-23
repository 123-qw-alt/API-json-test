import json

from json_file import get_api_json

# open data.json file
f = get_api_json()
file = open("data.json", "r", encoding="utf8")
data = json.load(file)

# Create test cases
class Test:
    def test_item(self):
        for i in range(len(f[0])):
            for j in range(len(f[0][i])):
                assert data[i][f[0][i][j]] == f[1][i][j]
