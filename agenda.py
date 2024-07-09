import json

class Agenda:
    def __init__(self, filename='agenda.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        contact = {
            'name': name,
            'phone': phone,
            'email': email
        }
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contacto {name} añadido con éxito.")

    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'] != name]
        self.save_contacts()
        print(f"Contacto {name} eliminado con éxito.")

    def show_contacts(self):
        if not self.contacts:
            print("No hay contactos en la agenda.")
        else:
            for contact in self.contacts:
                print(f"Nombre: {contact['name']}, Teléfono: {contact['phone']}, Email: {contact['email']}")

    def search_contact(self, name):
        found_contacts = [c for c in self.contacts if name.lower() in c['name'].lower()]
        if not found_contacts:
            print(f"No se encontraron contactos con el nombre {name}.")
        else:
            for contact in found_contacts:
                print(f"Nombre: {contact['name']}, Teléfono: {contact['phone']}, Email: {contact['email']}")

def main():
    agenda = Agenda()

    while True:
        print("\n--- Agenda ---")
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Mostrar contactos")
        print("4. Buscar contacto")
        print("5. Salir")

        option = input("Seleccione una opción: ")

        if option == '1':
            name = input("Nombre: ")
            phone = input("Teléfono: ")
            email = input("Email: ")
            agenda.add_contact(name, phone, email)
        elif option == '2':
            name = input("Nombre del contacto a eliminar: ")
            agenda.delete_contact(name)
        elif option == '3':
            agenda.show_contacts()
        elif option == '4':
            name = input("Nombre del contacto a buscar: ")
            agenda.search_contact(name)
        elif option == '5':
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()
