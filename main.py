from paquete.sistema import Sistema

sistema = Sistema()

while True:

    sistema.mostrar_menu()

    opcion = input("Seleccione una opcion (1-6): ")

    if opcion == "1":
        sistema.ver_transacciones()
    elif opcion == "2":
        sistema.agregar_transaccion()
    elif opcion == "3":
        sistema.validar_transacciones()
    elif opcion == "4":
        print("Saliendo del sistema. Gracias por utilizar nuestro servicio!")
        break
    elif opcion == "5":
        ruta= input("Ingrese la ruta del archivo CSV: ")
        sistema.importar_csv(ruta)
    elif opcion == "6":
        ruta = input("Ingrese una ruta donde guardar el CSV: ")
        sistema.exportar_csv(ruta)
    else:
        print("Opción no válida. Intente nuevamente.") 

# Este es un comentario para probar nueva rama