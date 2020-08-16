import requests
import json
API_URL = "https://api.unsplash.com/"


def get_images(search_term, color_value, page):
    query = "{}search/photos".format(API_URL)
    payload = {
        "query": search_term,
        "page": page,
        "per_page": 50
    }
    if color_value:
        payload.update({"color": color_value})

    response = requests.get(
        query,
        headers={
            "Authorization": "Client-ID hc4D8P7i5iXjF_gyOjDo8dxyQPFAUapNJlSVbUnPECU"
        },
        params=payload
    )
    results = response.json()
    print(response)
    images = []
    for item in results["results"]:
        images.append({
            "url": item["urls"]["regular"],
            "caption": item["description"],
            "author": item["user"]["username"],
            "unsplashed": item["links"]["html"]
        })

    return images


if __name__ == "__main__":
    print(get_images())
