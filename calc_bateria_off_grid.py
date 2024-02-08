class Calc_Bateria_off_grid:

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

    def energia_Consumida(self) -> float:
 
        return self.eCD * self.autonomia

    def energia_armazenada(self) -> float:

        return self.energia_Consumida() / self.prof_descarga

    def capacidade_banco_baterias(self) -> float:

        return self.energia_armazenada() / self.voltagem

    def numero_bateria_Seria(self) -> int:
 
        return int(self.voltagem / self.tensao_bateria)

    def numero_bateria_paralelo(self) -> int:

        return int(round(self.capacidade_banco_baterias() / self.Capacidade_descarga_hora))

    def numero_total_Baterias(self) -> int:
        return self.numero_bateria_Seria() * self.numero_bateria_paralelo()
