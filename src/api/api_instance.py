from typing import Union

from requests.adapters import HTTPAdapter
from requests.sessions import Session
from requests.exceptions import HTTPError, RequestException

from urllib3.util.retry import Retry


class APISession:
    """
    Classe para gerenciar sessões de requisições HTTP com suporte a retries e tratamento de erros.

    Atributtes:
        session (Session): A sessão de requisições HTTP.
    """
    def __init__(self) -> None:
        self.session = Session()

        self.retry = Retry(
            connect=1,
            total=5,
            backoff_factor=0.5,
            respect_retry_after_header=True,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=['GET', 'POST', 'PUT', 'DELETE']
        )

        self.adapters = HTTPAdapter(max_retries=self.retry)

        self.session.mount('http://', self.adapters)
        self.session.mount('https://', self.adapters)

    def get(self) -> Union[Session, None]:
        """
        Retorna a sessão URL
        """
        return self.session