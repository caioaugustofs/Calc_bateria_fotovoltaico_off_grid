from calc_bateria_off_grid import Calc_Bateria_off_grid


eCD = 2325.93
Cbat = 220

bateria = Calc_Bateria_off_grid(eCD=eCD, Capacidade_descarga_hora=Cbat)

print('\n' * 2)
print(bateria.__str__())

print(bateria.__repr__())
print('\n' * 2)
