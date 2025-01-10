import requests


def validate_breed(breed_name: str) -> tuple:

    response = requests.get(
        f"https://api.thecatapi.com/v1/breeds/search?q={breed_name}"
    )

    breeds = response.json()
    if not breeds or len(breeds) > 1:
        return False, f"Breed '{breed_name}' is not valid"

    if breeds[0]["name"] == breed_name:
        return True, breeds[0]["name"]
    else:
        return (
            False,
            f"Breed '{breed_name}' is not valid, but similar to '{breeds[0]['name']}'. Check the exact name",
        )
