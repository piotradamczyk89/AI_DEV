from langchain_core.documents import Document
import requests


def document_from_json(data: dict) -> Document:
    """
    Create a Document object from a JSON representation.

    Args:
        data: A dictionary representing the JSON of a Document.

    Returns:
        A Document object.
    """
    return Document(page_content=data['kwargs']['page_content'], metadata=data['kwargs'].get('metadata', {}))


def get_data(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")


