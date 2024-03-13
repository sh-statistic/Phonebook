import random
import peewee

from database_manager import DatabaseManager

import local_settings

database_manager = DatabaseManager(
    database_name=local_settings.DATABASE['name'],
    user=local_settings.DATABASE['user'],
    password=local_settings.DATABASE['password'],
    host=local_settings.DATABASE['host'],
    port=local_settings.DATABASE['port'],
)


class Information(peewee.Model):
    first_name = peewee.CharField(max_length=255, null=False, verbose_name='first_name')
    last_name = peewee.CharField(max_length=255, null=False, verbose_name='last_name')
    address = peewee.CharField(max_length=255, null=False, verbose_name='address')

    class Meta:
        database = database_manager.db


class Phone(peewee.Model):
    phone_number = peewee.CharField(max_length=255, null=False, verbose_name='Title')
    information = peewee.ForeignKeyField(model=Information, null=False, verbose_name='information')

    class Meta:
        database = database_manager.db


if __name__ == "__main__":
    try:
        database_manager.create_tables(models=[Information, Phone])

        # Generate random data and insert into the database
        for _ in range(10):  # Insert 10 random records
            first_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 10)))
            last_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 10)))
            address = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=random.randint(10, 20)))
            phone_number = ''.join(random.choices('1234567890', k=random.randint(7, 12)))

            info = Information.create(first_name=first_name, last_name=last_name, address=address)
            Phone.create(phone_number=phone_number, information=info)

    except Exception as error:
        print("Error", error)
    finally:
        # closing database connection.
        if database_manager.db:
            database_manager.db.close()
            print("Database connection is closed")
