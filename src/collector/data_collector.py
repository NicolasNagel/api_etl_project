from abc import ABC, abstractmethod
from typing import Optional, Any, Union

class DataCollector(ABC):
    """
    Classe de contrato para criação de coletores de Dados. 
    """

    @abstractmethod
    def collect(self) -> Union[Optional[Any], None]:
        """
        Método de contrato para a coleta de dados, cabe ao próximo Engenheiro de Dados
        definir o retorno da função quando criar a classe Coletora.

        Returns:
            Union(Optional[Any], None): Retorno definido pelo próximo Engenheiro de Dados.
        """
        raise NotImplementedError('Método ainda não implementado.')