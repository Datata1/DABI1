import csv
from sqlalchemy.exc import SQLAlchemyError
from custom_types.db_models import (
    Order, 
    Product, 
    Aisle, 
    Einkaufskorb, 
    Department
)

def insert_data_from_csv(csv_path, session, model_class, field_mapping, batch_size=1000):
    """
    csv_path: Pfad zur CSV-Datei
    session: Die SQLAlchemy-Sitzung
    model_class: Die SQLAlchemy Modellklasse (z.B. Order, Aisle, Product)
    field_mapping: Ein Dictionary, das die Spaltennamen der CSV-Datei auf die Modelldaten abbildet
    batch_size: Anzahl der Zeilen, die in einem Batch eingefügt werden sollen
    """
    try:
        with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            batch = []

            for row in reader:
                row = {key: (value if value != '' else None) for key, value in row.items()}
                
                data = {field: row[column] for field, column in field_mapping.items()}
                batch.append(data)

                if len(batch) >= batch_size:
                    session.bulk_insert_mappings(model_class, batch)
                    session.commit()
                    batch = []

            if batch:
                session.bulk_insert_mappings(model_class, batch)
                session.commit()

            print(f"Daten für {model_class.__tablename__} wurden erfolgreich eingefügt.")
    except SQLAlchemyError as e:
        print(f"Fehler beim Einfügen in die {model_class.__tablename__} Datenbank:", e)
        session.rollback()



def insert_aisle_data(csv_path, session):
    field_mapping = {
        'aisle_id': 'aisle_id',
        'aisle_name': 'aisle'  
    }
    insert_data_from_csv(csv_path, session, Aisle, field_mapping)


def insert_departments_data(csv_path, session):
    field_mapping = {
        'department_id': 'department_id',
        'department_name': 'department'  
    }
    insert_data_from_csv(csv_path, session, Department, field_mapping)


def insert_product_data(csv_path, session):
    field_mapping = {
        'product_id': 'product_id',
        'product_name': 'product_name',
        'aisle_id': 'aisle_id',
        'department_id': 'department_id'
    }
    insert_data_from_csv(csv_path, session, Product, field_mapping)


def insert_einkaufskorb_data(csv_path, session):
    field_mapping = {
        'order_id': 'order_id',
        'product_id': 'product_id',
        'add_to_cart_order': 'add_to_cart_order'
    }
    insert_data_from_csv(csv_path, session, Einkaufskorb, field_mapping)

def insert_order_data(csv_path, session):
    field_mapping = {
        'order_id': 'order_id',
        'user_id': 'user_id',
        'order_number': 'order_number',
        'day_of_the_week': 'order_dow',  
        'hour_of_day': 'order_hour_of_day',  
        'days_since_prior_order': 'days_since_prior_order'
    }
    insert_data_from_csv(csv_path, session, Order, field_mapping)


def insert_tip_bools(csv_data, session):
    pass
