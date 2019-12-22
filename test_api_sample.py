import requests
import json

base_url = "https://petstore.swagger.io/v2/pet"

pet_id = 1
pet_json = {
    "id": pet_id,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "qq1q",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}
headers = {'Content-type': 'application/json'}


def get_pet():
    return requests.get(f'{base_url}/{pet_id}')


def put_pet():
    return requests.put(base_url, json.dumps(pet_json), headers=headers)


def test_get_pet():
    response = get_pet()
    assert response.status_code == 200


def test_put_pet():
    response = put_pet()
    assert response.status_code == 200

