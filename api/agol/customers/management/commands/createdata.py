from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from operations.models import SafetyChecklistQuestion
from customers.models import Order, BulkOrder, Customer, Vehicle, CustomerTrailer, CustomerDriver, CustomerTruck, Driver
import random

class Command(BaseCommand):
    help="Command information"

    def handle(self, *args, **kwargs):
        
        fake = Faker()

        print("We are IN")

        # print(fake.address())
        # for _ in range(1000):
        #     name =  fake.company()
        #     phone = random.randint(22155541, 554544541)
        #     email = fake.email()
        #     location = 'KSM'
        #     bulk_customer = random.randint(0, 1)
        #     Customer.objects.create(name=name, phone=phone, email=email, location=location, bulk_customer=bulk_customer)

        # for _ in range(3000):
        #     registration = fake.license_plate()
        #     transporter = fake.company()
        #     epra_no = fake.license_plate()
        #     Vehicle.objects.create(registration=registration, transporter=transporter, epra_no=epra_no)

        
        # for _ in range(1000):
        #     name = fake.name()
        #     national_id = random.randint(22155541, 554544541)
        #     epra_no = random.randint(2215, 554544)
        #     Driver.objects.create(name=name, national_id=national_id, epra_no=epra_no)
        #     print("Drivers Created")


        # for _ in range(2000):
        #     customer = Customer.objects.get(pk=random.randint(1, 1000))    
        #     destination = 'KSM'    
        #     order_quantity = random.randint(25000, 30000)  
            
        #     driver = Driver.objects.get(id=random.randint(1, 510))
        #     truck = Vehicle.objects.get(id=random.randint(1, 1000))
        #     trailer = Vehicle.objects.get(id=random.randint(1, 1000)) 
        #     Order.objects.create(customer=customer, destination=destination, order_quantity=order_quantity, driver=driver, truck=truck, trailer=trailer)
        #     print("Orders Created")

        
        # for _ in range(130):
        #     customer = Customer.objects.get(pk=random.randint(1, 50))
        #     quantity = random.randint(2215, 554544)
        #     BulkOrder.objects.create(customer=customer, quantity=quantity)
        
        # for _ in range(8):
        #     question_desc = fake.sentence()
        #     SafetyChecklistQuestion.objects.create(question_desc=question_desc)

        # for _ in range(20):
        #     customer = Customer.objects.get(pk=random.randint(1, 100))
        #     registration = fake.license_plate()
        #     trailer = Vehicle.objects.get(pk=random.randint(1, 300))
        #     CustomerTrailer.objects.create(registration=registration, customer=customer, trailer=trailer)

        # for _ in range(50):
        #     customer = Customer.objects.get(pk=random.randint(1, 100))
        #     registration = fake.license_plate()
        #     truck = Vehicle.objects.get(pk=random.randint(1, 300))
        #     CustomerTruck.objects.create(registration=registration, customer=customer, truck=truck)

        for _ in range(50):
            customer = Customer.objects.get(pk=1)
            name = fake.name()
            driver = Driver.objects.get(pk=random.randint(1, 200))
            CustomerDriver.objects.create(customer=customer, name=name, driver=driver)
            print('we here')

