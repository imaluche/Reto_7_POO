import json
from funciones import *        
if __name__ == "__main__": 
   print("bienvenido a tu futuro restaurante")
   ceo = Manager(input("ingresa tu nombre"), float(input("ingresa el capital inicial para el negocio (es recomendable tener al menos 600000)")))
   print("este es su menu")
   print(ceo.ver_menu())
   if (input("¿desea añadir mas productos? (si/no)")) == "si":
      nu = float(input("¿cuantos productos desea añadir?"))
      ceo.añadir_productos(nu)
   final_menu = ceo.menu
   print("ahora es necesario contratar empleados")
   ceo.contratar()
   trabajadores = ceo.empleados
   print("tus trabajadores son:")
   for i in trabajadores:
      print(i)
   print("ahora empezemos a trabajar?")
   comensales = random.randint(1,10)
   flag = 0
   ordenes_tomadas = []
   medios_de_pago = []
   for i in trabajadores:
         if isinstance(i,mesero):
             while flag < comensales:
               ran_num = random.randint(0,100)
               if ran_num < 50:
                  medio_comensal_random = Efectivo(random.randint(10000,1000000))
               elif ran_num >= 50:
                  medio_comensal_random = Tarjeta(random.randint(10000, 1000000), random.randbytes(7))
               i.añadir_orden(final_menu[0],final_menu[1],final_menu[2],final_menu[3],final_menu[4])
               flag = flag +1
               ordenes_tomadas.append(i)
               medios_de_pago.append(medio_comensal_random)
         if isinstance(i, cajero):
            cont = 0
            for j in ordenes_tomadas:
               i.cuentas(j,medios_de_pago[cont])
               cont=cont +1 

   #print(jsonmenu["ensaladas"][0])
   #listadef = convertidor(lectura_menu)
 
   #menu = producto("menu", 0)
   #tarjeta = Tarjeta(100000000, "1234-87345", "2504")
   #billetera = Efectivo(50000)
   #mesero1= mesero("Juan", Queue())
   #mesero1.añadir_orden(listadef[0], listadef[1], listadef[2], listadef[3], listadef[4])
   #cajero1= cajero("carlos")
   #cajero1.cuentas(mesero1, tarjeta)
   #cuenta1.total()
   #dueño = Manager(input("ingresa tu nombre"),0)
   #dueño.ver_menu(listadef)