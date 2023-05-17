def create_tables():
    import mysql.connector
    from mysql.connector import connect, Error 
    from . import config_real

    config = {
        'user': config_real.user,
        'password': config_real.password,
        'host': config_real.host,
        'port': config_real.port,
        'database': config_real.database,      
    }

    try:
        conn = mysql.connector.connect(**config)      
        print("Connection2 established")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    try:
        cursor = conn.cursor() 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    try:
       cursor.execute("DROP TABLE result_photos_test1")
    except:
        pass 

    try:
        cursor.execute("DROP TABLE result_description_test1")
    except:
        pass 

    try:
       cursor.execute("DROP TABLE result_facilities_test1")
    except:
        pass 
    try:
       cursor.execute("DROP TABLE result_room_test1")
    except:
        pass 
    try:
       cursor.execute("DROP TABLE result_room_block_test1")
    except:
        pass
    try:
       cursor.execute("DROP TABLE black_list_test1")
    except:
        pass

    create_table_query1 = '''
    CREATE TABLE result_photos_test1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hotelid VARCHAR(20),
        photo_id VARCHAR(20),
        tags TEXT,
        url_square60 TEXT,
        url_max TEXT
    )
    '''

    create_table_query2 = '''
    CREATE TABLE result_description_test1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hotelid VARCHAR(20),
        enusname TEXT
    )
    '''

    create_table_query3 = '''
    CREATE TABLE result_facilities_test1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hotelid VARCHAR(20),
        facilitytype_id TEXT,
        name TEXT,
        facilitytype_name TEXT,
        hotelfacilitytype_id TEXT,
        uniq TEXT        
    )
    '''
    create_table_query4 = '''
    CREATE TABLE result_room_test1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hotelid VARCHAR(20),
        roomid VARCHAR(20),
        endescription TEXT,
        allow_children VARCHAR(15),
        photo1 TEXT,
        photo2 TEXT,
        photo3 TEXT,
        photo4 TEXT,
        photo5 TEXT,
        photo6 TEXT,
        photo7 TEXT,
        photo8 TEXT,
        photo9 TEXT,
        photo10 TEXT,
        private_bathroom_highlight TEXT,
        bed_configurations TEXT        
    )
    '''
    create_table_query5 = '''
        CREATE TABLE result_room_block_test1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hotelid VARCHAR(20),
        room_id VARCHAR(20),
        gross_price TEXT,
        currency TEXT,
        room_name TEXT,
        nr_children VARCHAR(15),
        max_occupancy TEXT,
        mealplan TEXT,
        room_surface_in_m2 TEXT,
        nr_adults VARCHAR(15),
        all_inclusive TEXT        
    )
    '''

    create_table_query6 = '''
    CREATE TABLE black_list_test1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hotelid VARCHAR(20),
        url TEXT,
        fotos INT,
        description INT,
        facility INT,
        otziv VARCHAR(4),
        room INT,
        room_block INT

    )
    '''
    cursor.execute(create_table_query1)
    cursor.execute(create_table_query2)
    cursor.execute(create_table_query3)
    cursor.execute(create_table_query4)
    cursor.execute(create_table_query5)
    cursor.execute(create_table_query6)

    cursor.close()
    conn.close()
    
    return print("the tables was created successfully")


create_tables()


# python create_tables_db.py
# python -m db_all.create_tables_db


# sudo mysql -u root -p

# CREATE USER 'sonnik12'@'localhost' IDENTIFIED BY '6687vono';
# CREATE DATABASE upz_hotels_copy1;
# GRANT ALL PRIVILEGES ON upz_hotels_copy1.* TO 'sonnik12'@'localhost';

# FLUSH PRIVILEGES;
# EXIT;
