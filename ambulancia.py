# El sistema recibe una llamada.
# Al recibir la llamada deben ocurrir las siguientes cosas:
#  * El sistema chequea que haya ambulancias disponibles.
#  * Si hay una disponible, la envía y la marca como en transito.
#  * Caso contrario, envía un error.

class Ambulancia(object):
    def __init__(self, estado=None):
        if estado is None:
            estado = EstadoDisponible()
        self.estado = estado

    def esta_disponible(self):
        return self.estado.disponible()

    def __repr__(self):
        return "<Ambulancia estado='{0}'>".format(self.estado)

class EstadoAmbulancia(object):
    def disponible(self):
        return False

    def __repr__(self):
        return "<Estado>"

class EstadoDisponible(EstadoAmbulancia):
    def disponible(self):
        return True

    def __repr__(self):
        return "<Disponible>"

class EstadoEnTransito(EstadoAmbulancia):
    def __repr__(self):
        return "<EnTransito>"

class Despachador(object):
    def __init__(self, ambulancias):
        self.ambulancias = ambulancias

    def llamar(self):
        for ambulancia in self.ambulancias:
            if ambulancia.esta_disponible():
                ambulancia.estado = EstadoEnTransito()
                return ambulancia
        raise Exception('No hay ambulancia disponible.')

if __name__ == '__main__':
    try:
        ambulancias = [
          Ambulancia(EstadoEnTransito()),
          Ambulancia(EstadoEnTransito()),
          Ambulancia()
        ]
        despachador = Despachador(ambulancias)

        print(ambulancias)
        despachador.llamar()
        print(ambulancias)

        print('Fuiste salvado! :)')
    except Exception:
        print('No hay ambulancias! Perdon :(')
        exit(-1)
    finally:
        print('Chaus')