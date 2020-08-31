from Classificadores.Filmes import Filmes
from Classificadores.Tutorial import Tutorial
from Classificadores.ClassificadorVagas import ClassificadorVagas
class Program:

    def main():
        objetoTutorial = Tutorial()
        objetoTutorial.classificador()
        #objetoClassificador = ClassificadorVagas()
        #objetoClassificador.classificador()
        print("Finalizando.......")


    
    if __name__ == "__main__":
        main()