import pandas as pd
import socket, os, time, sys

class Servidor:
#frase = "Hola 5458"
    def contador(self,frase): #self solo cuando hay una clase
        frase_minusculas = frase.lower().replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
        prueba = pd.Series(list(frase_minusculas)).value_counts()
        prueba = prueba.to_string() #convertir el pandas en string
        print (type(prueba)) #ver tipo de dato
        return (prueba)
    
#print(contador(frase))

    def serv(self): #self para test
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

        s.bind(("localhost",5091))
        s.listen(1)

       
        while True:
            print("esperando que se conecte un cliente...")
            fecha_fichero_hijo, direccion_cli = s.accept()

            try:
                hijo=os.fork()
                if hijo == 0:

                    print("conexión establecida con el cliente", direccion_cli)

                    while True:
                        datos = fecha_fichero_hijo.recv(1024)#recibe el nombre fichero
                        #print(datos)

                        if not datos:# ctrl c
                            break

                        try: # se encuentra el fichero
                            analizar = self.contador(datos.decode("utf8")) #función Ponemos self.contador de la misma clase ya que no está definido en ningun sitio
                            print(type (analizar))
                            fecha_fichero_hijo.send(analizar.encode("utf8"))

                        except: #no se encuentra el fichero
                            error = "error de fichero!!!"
                            fecha_fichero_hijo.send(error.encode("utf8"))
                            raise #lanze excepción
            
            except KeyboardInterrupt: #se cierra el servidor
                salir = "servidor cerrado"
                fecha_fichero_hijo.send(salir.encode("utf8"))
                print(salir)
                sys.exit(0) #cierre el programa bien 

            finally:
                fecha_fichero_hijo.close()

    #serv() quitar cuando meto los test


if __name__=="__main__":
    servidor = Servidor()
    servidor.serv()
