from faker import Faker
fake = Faker()

def get_students_data():
    return {
        "name": fake.name(),
        "address" : fake.address(),
        "email"   : fake.email(),
        "create_at" : fake.year()
    }

if __name__ == "__main__":
    print(get_students_data())