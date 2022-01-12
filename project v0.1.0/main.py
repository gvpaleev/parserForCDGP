
import profile
from Class.MainClass import Main
from multiprocessing import Process

if __name__ == '__main__':
    print('main')
    
    procs = []

    

    for i in range(1):
        main = Main()

        pathData ='/home/admins/Документы/parserForCDGP/project v0.1.0/data1'

        main.main(pathData)


    print('end main')
