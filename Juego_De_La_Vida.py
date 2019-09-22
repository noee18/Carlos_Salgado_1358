Import Array2D

class JuegoVida:
    def __init__(self, rows, cols, generaciones, poblacion_inicial):
        self.__cuadro=Array2D(rows,cols)
        self.__filas = rows
        self.__columnas = cols
        self.__generaciones = generaciones 

        poblacion_inicial = [[1,3],[2,2],[2,3],[2,4]]

        self.__cuadro.clearing(0)

        for cell in poblacion_inicial:
            self.__cuadro.set_item(cell[0],cell[1],1)

    def to_string(self):
        self.__cuadro.to_string()

    def configure_next_generation(self, nueva_generacion):
        self.__cuadro.clearing(0)
        for cell in nueva_generacion:
            self.__cuadro.set_item(cell[0],cell[1],1)

    def set_cell_death(self,row,col):
        self.__cuadro.set_item(row, col, 0)

    def set_cell_live(self,row,col):
        self.__cuadro.set_item(row, col, 1)

    def is_live_cell(self,row, col):
        return self.__cuadro.get_item(col,row) == 1

    def get_num_live_neighbours(self, row, col):
        limites = self.calcula_vecinos(row,col)
        cont = 0
        for fila in range(limites[0], limites[2]+1,1):
            for cols in range(limites[1],limites[1]+1,1):
                if fila == row and cols == col:
                    pass
                else:
                    if self.is_live_cell(fila,cols):
                        cont += 1
        return cont

    def calcula_vecinos(self,x,y):
        vecinos = [y-1,x-1,y+1,x+1]
        if vecinos[0] == -1:
            vecinos[0] == 0
        if vecinos[1] == -1:
            vecinos[1] == 0
        if vecinos[2] == self.__filas:
            vecinos[2] = self.__filas-1
        if vecinos[3] == self.__columnas:
            vecinos[3] = self.__columnas

def main(self):
    inicial = [[1,2],[2,1],[2,2],[2,3]]
    juego = JuegoVida(5,5,4,inicial)
    juego.to_string()
    for r in range(5):
        for c in range(5):
            print(f"[{r}][{c}]={juego.get_num_live_neighbours(r,c)}")

main()
