contactos = {}

# Imagina que contactos es como una agenda de teléfono
# Es como una caja vacía donde guardas nombres con sus teléfonos y emails
# Las {} son como una caja vacía

def agregar_contacto(nombre, telefono, email):
    # guarda el contacto en el diccionario
    # Es como escribir en tu agenda: "Juan" -> Teléfono: 555-1234, Email: juan@correo.com
    contactos[nombre] = {"telefono": telefono, "email": email}
    

# Para guardar una persona real, usa:
# agregar_contacto("Juan", "555-1234", "juan@correo.com")

def buscar_contacto(nombre):
    # retorna el contacto si existe
    return contactos.get(nombre)

def listar_contactos():
    # muestra todos los contactos
    for nombre, info in contactos.items():
        print(f"Nombre: {nombre}, Teléfono: {info['telefono']}, Email: {info['email']}")
    

def eliminar_contacto(nombre):
    # elimina si existe
    if nombre in contactos:
        del contactos[nombre]

agregar_contacto("Juan", "555-1234", "juan@correo.com")
agregar_contacto("María", "555-5678", "maria@correo.com")
listar_contactos()
print(buscar_contacto("Juan"))
eliminar_contacto("Juan")
listar_contactos()

# Ejemplo de cómo usar:
# opción 1: agregar un contacto directo
#agregar_contacto("Juan", "555-1234", "juan@correo.com")

# opción 2: pedir datos al usuario
# nombre = input("Nombre: ")
# telefono = input("Teléfono: ")
# email = input("Email: ")
# agregar_contacto(nombre, telefono, email)

# Ver todos los contactos
#listar_contactos()

# ==========================================
# CÓMO GUARDAR UNA PERSONA REAL
# ==========================================

# Forma 1: Directo (escribir los datos tú mismo)
#agregar_contacto("Juan", "555-1234", "juan@correo.com")

# Forma 2: Pidiendo al usuario (el programa pregunta)
# Descomenta estas líneas si quieres que te pregunte:
# nombre = input("Nombre: ")
# telefono = input("Teléfono: ")
# email = input("Email: ")
# agregar_contacto(nombre, telefono, email)

# Para ver todos los contactos guardados:
#listar_contactos()

def menu():
    while True:
        print("\n--- GESTOR DE CONTACTOS ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar contactos")
        print("4. Eliminar contacto")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agregar_contacto(nombre, telefono, email)
            print("✅ Contacto agregado")
        elif opcion == "2":
            nombre = input("Nombre a buscar: ")
            resultado = buscar_contacto(nombre)
            if resultado:
                print(f"📞 {resultado}")
            else:
                print("❌ Contacto no encontrado")
        elif opcion == "3":
            listar_contactos()
        elif opcion == "4":
            nombre = input("Nombre a eliminar: ")
            eliminar_contacto(nombre)
            print("🗑️ Eliminado")
        elif opcion == "5":
            break
        else:
          print("❌ Opción inválida, elige entre 1 y 5")
menu()