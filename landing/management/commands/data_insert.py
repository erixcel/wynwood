from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from landing.models import Country, State, City, Property, PropertyPhoto, Reservation

class Command(BaseCommand):
    help = 'Borra todos los datos existentes e inserta datos iniciales en la base de datos'

    def handle(self, *args, **kwargs):
        self.stdout.write("Eliminando todos los datos existentes...")
        User = get_user_model()

        Reservation.objects.all().delete()
        PropertyPhoto.objects.all().delete()
        Property.objects.all().delete()
        City.objects.all().delete()
        State.objects.all().delete()
        Country.objects.all().delete()
        User.objects.all().delete()

        self.stdout.write(self.style.WARNING("Datos eliminados."))
        self.stdout.write("Creando nuevos datos...")

        # Crear países
        spain = Country.objects.create(name="España")
        peru = Country.objects.create(name="Perú")

        # Crear estados
        catalonia = State.objects.create(name="Catalonia", country=spain)
        madrid_state = State.objects.create(name="Madrid", country=spain)
        andalusia = State.objects.create(name="Andalusia", country=spain)
        lima_state = State.objects.create(name="Lima", country=peru)
        cusco_state = State.objects.create(name="Cusco", country=peru)
        arequipa_state = State.objects.create(name="Arequipa", country=peru)

        # Crear ciudades
        barcelona = City.objects.create(name="Barcelona", state=catalonia)
        madrid_city = City.objects.create(name="Madrid", state=madrid_state)
        seville = City.objects.create(name="Seville", state=andalusia)
        miraflores = City.objects.create(name="Miraflores", state=lima_state)
        urubamba = City.objects.create(name="Urubamba", state=cusco_state)
        arequipa_city = City.objects.create(name="Arequipa Centro", state=arequipa_state)

        # Crear Propiedades en España
        property01 = Property.objects.create(
            name="Apartamento Moderno en la Marina",
            address="Carrer de la Marina, 123",
            city=barcelona,
            cost_per_night=120.00,
            capacity=4,
            beds=2,
            stars=4.8,
            features="Cerca de la playa, WiFi gratis, Aire acondicionado, Cocina equipada",
            status="available"
        )
        property02 = Property.objects.create(
            name="Piso Histórico en el Barrio Gótico",
            address="Carrer del Paradís, 45",
            city=barcelona,
            cost_per_night=150.00,
            capacity=3,
            beds=2,
            stars=4,
            features="Vista al casco antiguo, Decoración rústica, WiFi",
            status="available"
        )
        property03 = Property.objects.create(
            name="Apartamento con Balcón en la Plaza Mayor",
            address="Plaza Mayor, 45",
            city=madrid_city,
            cost_per_night=180.00,
            capacity=2,
            beds=1,
            stars=3,
            features="Balcón con vistas, Cerca de restaurantes y tiendas, WiFi rápido",
            status="available"
        )
        property04 = Property.objects.create(
            name="Loft Espacioso en el Centro",
            address="Calle de Alcalá, 56",
            city=madrid_city,
            cost_per_night=200.00,
            capacity=5,
            beds=3,
            stars=4.2,
            features="Diseño moderno, Smart TV, Cocina equipada, Mascotas permitidas",
            status="available"
        )
        property05 = Property.objects.create(
            name="Casa Tradicional Andaluza",
            address="Avenida de la Constitución, 123",
            city=seville,
            cost_per_night=110.00,
            capacity=6,
            beds=3,
            stars=3.9,
            features="Patio privado, Cocina completa, Excelente ubicación en el centro",
            status="available"
        )
        property06 = Property.objects.create(
            name="Ático con Terraza en Plaza Nueva",
            address="Plaza Nueva, 15",
            city=seville,
            cost_per_night=250.00,
            capacity=4,
            beds=2,
            stars=4.6,
            features="Terraza amplia, Jacuzzi, Vista a la catedral, WiFi incluido",
            status="available"
        )

        # Crear Propiedades en Perú
        property07 = Property.objects.create(
            name="Departamento con Vista al Mar",
            address="Av. Larco, 789",
            city=miraflores,
            cost_per_night=100.00,
            capacity=3,
            beds=2,
            stars=5,
            features="Vista al océano, Cocina equipada, WiFi gratuito, Cerca de Larcomar",
            status="available"
        )
        property08 = Property.objects.create(
            name="Apartamento en el Malecón",
            address="Malecón Cisneros, 321",
            city=miraflores,
            cost_per_night=120.00,
            capacity=4,
            beds=2,
            stars=4,
            features="Acceso al malecón, Ideal para familias, Estacionamiento privado",
            status="available"
        )
        property09 = Property.objects.create(
            name="Lodge Rústico en el Valle Sagrado",
            address="Camino Inca, Km 12",
            city=urubamba,
            cost_per_night=90.00,
            capacity=2,
            beds=1,
            stars=4.2,
            features="Cerca de ruinas incas, Ambiente tranquilo, Rodeado de naturaleza",
            status="available"
        )
        property10 = Property.objects.create(
            name="Casa de Campo en Urubamba",
            address="Av. Principal, 99",
            city=urubamba,
            cost_per_night=80.00,
            capacity=6,
            beds=4,
            stars=4.2,
            features="Amplio jardín, Zona de parrilla, Ideal para grupos grandes",
            status="available"
        )
        property11 = Property.objects.create(
            name="Apartamento Céntrico en Arequipa",
            address="Calle Mercaderes, 45",
            city=arequipa_city,
            cost_per_night=70.00,
            capacity=2,
            beds=1,
            stars=4,
            features="Ubicación estratégica, Decoración moderna, Cerca de la Plaza de Armas",
            status="available"
        )
        property12 = Property.objects.create(
            name="Estudio Moderno en Avenida Arequipa",
            address="Av. Arequipa, 222",
            city=arequipa_city,
            cost_per_night=60.00,
            capacity=1,
            beds=1,
            stars=4.3,
            features="Económico, Ideal para viajeros solos, Cocina básica",
            status="available"
        )

        # Setear imagenes de propiedades

        PropertyPhoto.objects.create(property=property01, photo="destacado_02.png")
        PropertyPhoto.objects.create(property=property01, photo="destacado_01.png")
        PropertyPhoto.objects.create(property=property01, photo="destacado_03.png")
        PropertyPhoto.objects.create(property=property01, photo="destacado_04.png")
        PropertyPhoto.objects.create(property=property01, photo="destacado_05.png")
        PropertyPhoto.objects.create(property=property01, photo="destacado_06.png")

        PropertyPhoto.objects.create(property=property02, photo="destacado_02.png")
        PropertyPhoto.objects.create(property=property02, photo="destacado_01.png")
        PropertyPhoto.objects.create(property=property02, photo="destacado_04.png")
        PropertyPhoto.objects.create(property=property02, photo="destacado_03.png")
        PropertyPhoto.objects.create(property=property02, photo="destacado_05.png")
        PropertyPhoto.objects.create(property=property02, photo="destacado_06.png")

        PropertyPhoto.objects.create(property=property03, photo="destacado_03.png")
        PropertyPhoto.objects.create(property=property03, photo="destacado_02.png")
        PropertyPhoto.objects.create(property=property03, photo="destacado_01.png")
        PropertyPhoto.objects.create(property=property03, photo="destacado_04.png")
        PropertyPhoto.objects.create(property=property03, photo="destacado_05.png")
        PropertyPhoto.objects.create(property=property03, photo="destacado_06.png")

        PropertyPhoto.objects.create(property=property04, photo="destacado_03.png")
        PropertyPhoto.objects.create(property=property04, photo="destacado_04.png")
        PropertyPhoto.objects.create(property=property04, photo="destacado_02.png")
        PropertyPhoto.objects.create(property=property04, photo="destacado_05.png")
        PropertyPhoto.objects.create(property=property04, photo="destacado_01.png")
        PropertyPhoto.objects.create(property=property04, photo="destacado_06.png")

        PropertyPhoto.objects.create(property=property05, photo="destacado_04.png")
        PropertyPhoto.objects.create(property=property05, photo="destacado_05.png")
        PropertyPhoto.objects.create(property=property05, photo="destacado_02.png")
        PropertyPhoto.objects.create(property=property05, photo="destacado_03.png")
        PropertyPhoto.objects.create(property=property05, photo="destacado_06.png")
        PropertyPhoto.objects.create(property=property05, photo="destacado_01.png")

        PropertyPhoto.objects.create(property=property06, photo="destacado_03.png")
        PropertyPhoto.objects.create(property=property06, photo="destacado_02.png")
        PropertyPhoto.objects.create(property=property06, photo="destacado_04.png")
        PropertyPhoto.objects.create(property=property06, photo="destacado_05.png")
        PropertyPhoto.objects.create(property=property06, photo="destacado_01.png")
        PropertyPhoto.objects.create(property=property06, photo="destacado_06.png")

        PropertyPhoto.objects.create(property=property07, photo="destacado_01.png")
        PropertyPhoto.objects.create(property=property07, photo="destacado_04.png")
        PropertyPhoto.objects.create(property=property07, photo="destacado_03.png")
        PropertyPhoto.objects.create(property=property07, photo="destacado_06.png")
        PropertyPhoto.objects.create(property=property07, photo="destacado_05.png")
        PropertyPhoto.objects.create(property=property07, photo="destacado_02.png")

        PropertyPhoto.objects.create(property=property08, photo="destacado_02.png")
        PropertyPhoto.objects.create(property=property08, photo="destacado_03.png")
        PropertyPhoto.objects.create(property=property08, photo="destacado_01.png")
        PropertyPhoto.objects.create(property=property08, photo="destacado_04.png")
        PropertyPhoto.objects.create(property=property08, photo="destacado_05.png")
        PropertyPhoto.objects.create(property=property08, photo="destacado_06.png")

        PropertyPhoto.objects.create(property=property09, photo="destacado_03.png")
        PropertyPhoto.objects.create(property=property09, photo="destacado_02.png")
        PropertyPhoto.objects.create(property=property09, photo="destacado_01.png")
        PropertyPhoto.objects.create(property=property09, photo="destacado_04.png")
        PropertyPhoto.objects.create(property=property09, photo="destacado_05.png")
        PropertyPhoto.objects.create(property=property09, photo="destacado_06.png")

        PropertyPhoto.objects.create(property=property10, photo="destacado_01.png")
        PropertyPhoto.objects.create(property=property10, photo="destacado_02.png")
        PropertyPhoto.objects.create(property=property10, photo="destacado_04.png")
        PropertyPhoto.objects.create(property=property10, photo="destacado_03.png")
        PropertyPhoto.objects.create(property=property10, photo="destacado_06.png")
        PropertyPhoto.objects.create(property=property10, photo="destacado_05.png")

        PropertyPhoto.objects.create(property=property11, photo="destacado_04.png")
        PropertyPhoto.objects.create(property=property11, photo="destacado_02.png")
        PropertyPhoto.objects.create(property=property11, photo="destacado_01.png")
        PropertyPhoto.objects.create(property=property11, photo="destacado_03.png")
        PropertyPhoto.objects.create(property=property11, photo="destacado_05.png")
        PropertyPhoto.objects.create(property=property11, photo="destacado_06.png")

        PropertyPhoto.objects.create(property=property12, photo="destacado_06.png")
        PropertyPhoto.objects.create(property=property12, photo="destacado_01.png")
        PropertyPhoto.objects.create(property=property12, photo="destacado_02.png")
        PropertyPhoto.objects.create(property=property12, photo="destacado_03.png")
        PropertyPhoto.objects.create(property=property12, photo="destacado_04.png")
        PropertyPhoto.objects.create(property=property12, photo="destacado_05.png")

        # Crear usuarios
        user1 = User.objects.create_user(username='alice', email='alice@example.com', password='password123')
        user2 = User.objects.create_user(username='bob', email='bob@example.com', password='password123')

        # Crear reservas
        from datetime import date, timedelta

        Reservation.objects.create(
            property=property01,
            user=user1,
            check_in=date.today(),
            check_out=date.today() + timedelta(days=3),
            total_cost=450.00
        )

        Reservation.objects.create(
            property=property07,
            user=user2,
            check_in=date.today() + timedelta(days=5),
            check_out=date.today() + timedelta(days=8),
            total_cost=360.00
        )

        self.stdout.write(self.style.SUCCESS("Datos insertados correctamente."))


