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


    def __str__(self):
        """
        Retorna uma representação textual do objeto Calc_Bateria.

        Returns:
            str: Um resumo dos atributos da classe.
        """
        return (
            f'*** Sistema FV Off-Grid: ***\n\n'
            f'- **Energia consumida diária:** {self.eCD:.2f} Wh/dia\n'
            f'- **Autonomia:** {self.autonomia} dias\n'
            f'- **Profundidade de descarga:** {self.prof_descarga:.2%}\n'
            f'- **Voltagem nominal:** {self.voltagem} V\n'
            f'- **Tensão da bateria:** {self.tensao_bateria} V\n'
            f'- **Capacidade de descaregamento por horas (Ah):** {self.Capacidade_descarga_hora} Ah => tabela fabricante\n\n'
            f'- **Número de baterias em série:** {self.numero_bateria_Seria()}\n'
            f'- **Número de baterias em paralelo:** {self.numero_bateria_paralelo()}\n'
            f'- **Número total de baterias:** {self.numero_total_Baterias()}\n'
        )

    def __repr__(self) -> str:
        """
        Retorna uma representação canônica do objeto Calc_Bateria.

        Returns:
            str: Uma string que pode ser usada para recriar o objeto.
        """
        return (
            f'Calc_Bateria(eCD={self.eCD}, autonomia={self.autonomia}, '
            f'prof_descarga={self.prof_descarga}, voltagem={self.voltagem}, '
            f'tensao_bateria={self.tensao_bateria}, Capacidade_descarga_hora={self.Capacidade_descarga_hora})'
        )


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
