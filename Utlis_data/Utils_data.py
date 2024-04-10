from langchain_core.documents import Document


def document_from_json(data: dict) -> Document:
    """
    Create a Document object from a JSON representation.

    Args:
        data: A dictionary representing the JSON of a Document.

    Returns:
        A Document object.
    """
    return Document(page_content=data['kwargs']['page_content'], metadata=data['kwargs'].get('metadata', {}))
