
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel #Widgets a utilizar
from Avance import SopaLetras

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.filas = 50
        self.columnas = 50
        self.palabras_a_buscar = []
        self.sopa_letras = []
        self.execute = SopaLetras
        self.centrar = QMainWindow()
        self.setWindowTitle("Sopa de letras - TrabajoFinal")


        aux = self.Cargar_Dataset()
        a = self.Mostrar_Sopa_Letras()
        an = self.Mostrar_Resultados()

        #LabelSopaletras
        self.Sopaletras_label = QLabel(a)
        #LabelDataSet
        self.Dataset_label = QLabel(aux)


        #LabelResultados
        self.Resultados_label = QLabel(an) 




        #Mostrar_resultado_button.clicked.connect(self.Mostrar_Resultados) 

        text_layout = QHBoxLayout()
        text_layout.addWidget(self.Sopaletras_label)
        text_layout.addWidget(self.Dataset_label)

        result_layout = QVBoxLayout()
        result_layout.addWidget(self.Resultados_label)

        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(text_layout)
        self.v_layout.addLayout(result_layout)
        



        self.setLayout(self.v_layout)
#Print 1
    def Cargar_Dataset(self): 
        string = ''
        self.palabras_a_buscar = self.execute.cargar_del_dataset()
        string = '\n'.join(self.palabras_a_buscar)
        return string

    def Mostrar_Sopa_Letras(self):
        self.sopa_letras = self.execute.generar_sopa_letras(self.filas, self.columnas)
        aux = ''
        for filas in self.sopa_letras:
            aux += ' '.join(filas)
            aux += '\n'
        return aux
    
    
    def Mostrar_Resultados(self):
        resultao = ''
        resultados = self.execute.encontrar_palabras(self.sopa_letras, self.palabras_a_buscar)
        for palabra, posicion in resultados.items():
            resultao += f'Palabra "{palabra}" encontrada en la posición {posicion}\n'
        return "Palabras encontradas: " + '\n' + resultao
    
