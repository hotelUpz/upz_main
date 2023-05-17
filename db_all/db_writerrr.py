def db_wrtr(total):
    import mysql.connector
    from mysql.connector import connect, Error 
    from . import config_real
    print('hello db_writerr')

    config = {
        'user': config_real.user,
        'password': config_real.password,
        'host': config_real.host,
        'port': config_real.port,
        'database': config_real.database,      
    }

    try:
        conn = mysql.connector.connect(**config)      
        print("Writerr connection established2")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    try:
        cursor = conn.cursor() 
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    print(len(total))
    # print(total)
    resPhoto = []
    resDescription = []
    resFacilities = []
    resRooms = []
    resRoomsBlock = []

    try:
        for t in total:
            try:
                resPhoto += t[0][0]
            except:
                continue 
        try:
            resPhoto = list(filter(None, resPhoto))
            resPhoto = list(filter("", resPhoto)) 
        except:
            pass
        try:
            query1 = "INSERT INTO result_photos_test1 (hotelid, photo_id, tags, url_square60, url_max) VALUES (%s, %s, %s, %s, %s)"

            for item in resPhoto:
                try:
                    values = (item["hotelid"], item["photo_id"], item["tags"], item["url_square60"], item["url_max"])
                    cursor.execute(query1, values)
                except:
                    continue
            conn.commit()
        except:
            pass
        for t in total:
            try:
                resDescription.append(t[0][1])
            except Exception as ex:
                # print(f"writerr__str30__{ex}")
                continue 
        try:
            resDescription = list(filter(None, resDescription))
            resDescription = list(filter("", resDescription)) 
        except:
            pass
        try:
            query2 = "INSERT INTO result_description_test1 (hotelid, enusname) VALUES (%s, %s)"
            # query = "UPDATE result_description_test1 SET hotelid = %s, enusname = %s"
            for item in resDescription:
                try:        
                    values = (item["hotelid"], item["enusname"])
                    cursor.execute(query2, values)
                except Exception as ex:
                    print(ex)
                    continue
            conn.commit()
        except:
            pass

        for t in total:
            try:
               resFacilities += t[0][2]
            except:
                continue 
        try:
            resFacilities = list(filter(None, resFacilities))
            resFacilities = list(filter("", resFacilities)) 
        except:
            pass
        try: 
            query3 = "INSERT INTO result_facilities_test1 (hotelid, facilitytype_id, name, facilitytype_name, hotelfacilitytype_id, uniq) VALUES (%s, %s, %s, %s, %s, %s)"

            for item in resFacilities:
                try:
                    values = (item["hotelid"], item["facilitytype_id"], item["name"], item["facilitytype_name"], item["hotelfacilitytype_id"], item["uniq"])
                    cursor.execute(query3, values)
                except:
                    continue
            conn.commit() 
        except:
            pass

        for t in total:
            try:
               resRooms += t[0][3]
            except:
                continue 
        try:
            resRooms = list(filter(None, resRooms))
            resRooms = list(filter("", resRooms)) 
        except:
            pass
        try: 
            query4 = "INSERT INTO result_room_test1 (hotelid, roomid, endescription, allow_children, photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo10, private_bathroom_highlight, bed_configurations) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            for item in resRooms:
                try:
                    values = (item["hotelid"], item["roomid"], item["endescription"], item["allow_children"], item["photo1"], item["photo2"], item["photo3"], item["photo4"], item["photo5"], item["photo6"], item["photo7"], item["photo8"], item["photo9"], item["photo10"], item["private_bathroom_highlight"], item["bed_configurations"])
                    cursor.execute(query4, values)
                except:
                    continue
            conn.commit() 
        except:
            pass
        for t in total:
            try:
               resRoomsBlock += t[0][4]
            except:
                continue 
        try:
            resRoomsBlock = list(filter(None, resRoomsBlock))
            resRoomsBlock = list(filter("", resRoomsBlock)) 
        except:
            pass
        try: 
            query5 = "INSERT INTO result_room_block_test1 (hotelid, room_id, gross_price, currency, room_name, nr_children, max_occupancy, mealplan, room_surface_in_m2, nr_adults, all_inclusive) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            for item in resRoomsBlock:
                try:
                    values = (item["hotelid"], item["room_id"], item["gross_price"], item["currency"], item["room_name"], item["nr_children"], item["max_occupancy"], item["mealplan"], item["room_surface_in_m2"], item["nr_adults"], item["all_inclusive"])
                    cursor.execute(query5, values)
                except Exception as ex:
                    print(ex)
                    continue
            conn.commit() 
        except Exception as ex:
            print(ex)


    except Exception as ex:
        print(ex)
        pass


    try:
        cursor.close()
        conn.close()
    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    return 

# total = None
# db_opener(total)

# python db_writerrr.py



# resRoomHighlights = []
# with open('result_description__interval_0__1120__Items_982.json', 'r') as f:
#     data_result_descript = json.load(f)
# with open('photos__12_05_2023__16_32__443.json', 'r') as f:
#     resPhoto = json.load(f) 
# with open('facilities__12_05_2023__16_32__1030.json', 'r') as f:
#     resFacilities = json.load(f) 
# with open('room__12_05_2023__16_31__62.json', 'r') as f:
#     resRooms = json.load(f) 
# with open('room_block__12_05_2023__16_31__62.json', 'r') as f:
#     resRoomsBlock = json.load(f)
    # print(resRoomsBlock)
