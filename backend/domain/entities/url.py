from datetime import datetime
from typing import Union


class Url():
    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, title: Union[str, None] = None,
               url: Union[str, None] = None):
        """
        Atualiza o título e/ou a URL do link.
        - title: Novo título do link (opcional).
        - url: Nova URL do link (opcional).
        """
        if title is None and url is None:
            raise ValueError("At least one of title or url must be provided for update.")
        elif title is not None:
            self.title = title
        elif url is not None:
            self.url = url
        self.updated_at = datetime.now()
