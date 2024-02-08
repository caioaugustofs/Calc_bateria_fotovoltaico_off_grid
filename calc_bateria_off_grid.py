class Calc_Bateria_off_grid:
    """
    Classe para calcular o número de baterias necessárias para um sistema fotovoltaico off-grid.

    Args:
        eCD (float): Energia consumida diariamente (Wh/dia).
        autonomia (int, opcional): Autonomia do sistema (dias). Padrão: 2.
        prof_descarga (float, opcional): Profundidade de descarga das baterias. Padrão: 0.3.
        voltagem (int, opcional): Voltagem nominal do bateria (V). Padrão: 24.
        tensao_bateria (int, opcional): Tensão nominal de uma bateria (V). Padrão: 12.
        Capacidade_descarga_hora (int): Capacidade de descaregamento por horas  (Ah). => tabela fabricante.


    Raises:
        ValueError: Se algum parâmetro de entrada for inválido.
    """

    def __init__(
        self,
        eCD: float = None,
        autonomia: int = 2,
        prof_descarga: float = 0.3,
        voltagem: int = 24,
        tensao_bateria: int = 12,
        Capacidade_descarga_hora: int = None,
    ) -> None:
        self.eCD = eCD
        self.autonomia = autonomia
        self.prof_descarga = prof_descarga
        self.voltagem = voltagem
        self.tensao_bateria = tensao_bateria
        self.Capacidade_descarga_hora = Capacidade_descarga_hora


    def __str__(self):...

    def __repr__(self) -> str: ...

    def energia_Consumida(self) -> float:
        """
        Calcula a energia consumida total pelo sistema.

        Returns:
            float: Energia consumida em Wh.
        """
 
        return self.eCD * self.autonomia

    def energia_armazenada(self) -> float:
        """
        Calcula a energia armazenada no banco de baterias.

        Returns:
            float: Energia armazenada em Wh.
        """
        return self.energia_Consumida() / self.prof_descarga

    def capacidade_banco_baterias(self) -> float:
        """
        Calcula a capacidade total do banco de baterias.

        Returns:
            float: Capacidade do banco de baterias em Ah.
        """
        return self.energia_armazenada() / self.voltagem

    def numero_bateria_Seria(self) -> int:
        """
        Calcula o número de baterias necessárias em série.

        Returns:
            int: Número de baterias em série.
        """
        return int(self.voltagem / self.tensao_bateria)

    def numero_bateria_paralelo(self) -> int:
        """
        Calcula o número de baterias necessárias em paralelo.

        Returns:
            int: Número de baterias em paralelo.
        """
        return int(round(self.capacidade_banco_baterias() / self.Capacidade_descarga_hora))

    def numero_total_Baterias(self) -> int:
        """
        Calcula o número total de baterias necessárias.

        Returns:
            int: Número total de baterias.
        """
        return self.numero_bateria_Seria() * self.numero_bateria_paralelo()
