

```python
paciente_1 = {"nombre":"Adrian", "apellido":"Cedillo", "edad":23, "ciudad":"Mexico", "sintoma":"resfriado"}
paciente_2 = {"nombre":"Alberto", "apellido":"Rodriguez", "edad":22, "ciudad":"Mexico", "sintoma":"dolor de estomago"}
paciente_3 = {"nombre":"Diana", "apellido":"Carbajal", "edad":23, "ciudad":"Mexico", "sintoma":"diarrea"}
paciente_4 = {"nombre":"Adriana", "apellido":"Cordero", "edad":21, "ciudad":"Mexico", "sintoma":"dolor de espalda"}

pacientes = [paciente_1, paciente_2, paciente_3, paciente_4]
```


```python
def menu():
    print("*******************************")
    print(" Bienvenido a nuestro hospital ")
    print("******************************* \n")
    print("\t Menu de opciones \n")
    print("1) Agregar a un paciente")
    print("2) Buscar un paciente por nombre")
    print("3) Listado de pacientes en el hospital")
    print("4) Salir del menu \n")
```


```python
def new_patient():
    new_person = len(pacientes) + 1
    new_person = "paciente_"+str(new_person)
    new_person = {}
    print("*************************")
    print("Nuevo paciente")
    print("*************************")
    nombre = input("Ingrese el nombre del paciente: ")
    apellido = input("Ingrese el apellido del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    ciudad = input("Ingrese la ciudad donde vive el paciente: ")
    sintoma = input("Ingrese el sintoma del paciente: ")
    new_person["nombre"] = nombre
    new_person["apellido"] = apellido
    new_person["edad"] = edad
    new_person["ciudad"] = ciudad
    new_person["sintoma"] = sintoma
    print("\n")
    pacientes.append(new_person)
    for llave, valor in new_person.items():
        print(llave, ":", valor)
    print("\n")
```


```python
def find_person(person_to_find):
    for x in range(len(pacientes)):
        for llave, valor in pacientes[x].items():
            if valor == person_to_find:
                for llave, valor in pacientes[x].items():                    
                    print(llave, ":", valor)
    if valor != person_to_find:
        print("La persona no ha sido encontrada en la lista de pacientes ")
    print("\n")
```


```python
def list_of_persons():
    for x in range(len(pacientes)):
        for llave, valor in pacientes[x].items():
            print(llave, ":", valor)
        print("\n")
```


```python
def opciones(menu_option):
    if(menu_option == '1'):
        new_patient()
        general()
    elif(menu_option == '2'):
        print("*************************")
        print("Buscar persona")
        print("*************************")
        person_to_find = input("Ingrese el nombre de la persona a buscar: ")
        print("\n")
        find_person(person_to_find)
        general()
    elif(menu_option == '3'):
        print("*************************")
        print("Listado de pacientes")
        print("*************************")
        list_of_persons()
        general()
    elif(menu_option == '4'):
        print("Gracias por su busqueda")
        return;
```


```python
def general():
    menu()
    menu_option = input("Operacion a realizar: ")
    if menu_option != '1' and menu_option != '2' and menu_option != '3' and menu_option != '4':
        print("La opcion no esta disponible")
    else:
        print("\n")
        opciones(menu_option)
```


```python
general()
```

    *******************************
     Bienvenido a nuestro hospital 
    ******************************* 
    
    	 Menu de opciones 
    
    1) Agregar a un paciente
    2) Buscar un paciente por nombre
    3) Listado de pacientes en el hospital
    4) Salir del menu 
    
    Operacion a realizar: 3
    
    
    *************************
    Listado de pacientes
    *************************
    nombre : Adrian
    apellido : Cedillo
    edad : 23
    ciudad : Mexico
    sintoma : resfriado
    
    
    nombre : Alberto
    apellido : Rodriguez
    edad : 22
    ciudad : Mexico
    sintoma : dolor de estomago
    
    
    nombre : Diana
    apellido : Carbajal
    edad : 23
    ciudad : Mexico
    sintoma : diarrea
    
    
    nombre : Adriana
    apellido : Cordero
    edad : 21
    ciudad : Mexico
    sintoma : dolor de espalda
    
    
    *******************************
     Bienvenido a nuestro hospital 
    ******************************* 
    
    	 Menu de opciones 
    
    1) Agregar a un paciente
    2) Buscar un paciente por nombre
    3) Listado de pacientes en el hospital
    4) Salir del menu 
    



```python

```
