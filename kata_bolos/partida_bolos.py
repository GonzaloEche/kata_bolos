class Excepcion(Exception):
    pass

class Partida():
    def calcularResultado(self,ronda):
        suma = 0
        try:
            if len(ronda) <= 12:
                for i in range(0,len(ronda)):
                    if (sum(ronda[i]) <= 10): #si la suma de los lanzamientos es igual o menor que 10
                        if (i < 9):
                            if (ronda[i][0] == 10 and ronda[i+1][0] == 10): #encadenamos strikes seguidos
                               suma += ronda[i][0] + ronda[i+1][0] + ronda[i+2][0]
                            elif (ronda[i][0] == 10): #1 strike
                                suma += sum(ronda[i]) + sum(ronda[i+1])
                            elif (sum(ronda[i]) == 10 and ronda[i][0] != 10): #semipleno
                                suma += sum(ronda[i]) + ronda[i+1][0]
                            else:
                                suma += sum(ronda[i])

                        elif (i == 9):
                            suma += sum(ronda[i]) #la ronda 10 lo sume

                        else:
                            if (sum(ronda[9]) == 10 and ronda[9][0] != 10): #si la ronda 10 es un semipleno, solo sumará el primer bolo de la ronda 11
                                suma += ronda[9+1][0]
                            else:
                                suma += sum(ronda[i])
            return suma

        except:
            raise Excepcion
