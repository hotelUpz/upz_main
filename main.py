import requests
from fake_useragent import UserAgent
import random 
from random import choice
import time
import math
import re
import atexit
import shutil
import tempfile
import sys

from joblib import Parallel, delayed
from multiprocessing import cpu_count
from utilsss import b_filter_func as b
from scrapers_funcs import photos_func, description_func, faciclities_func, rooms_func, rooms_block_func
from db_all import db_reader, db_writerrr, bl_writerr
# from utils import b_filter_func
import psutil
import threading

uagent = UserAgent()

# def monitor_cpu(interval, stop_event):
#     while not stop_event.is_set():
#         cpu_percent = psutil.cpu_percent(interval=interval)
#         print(f"CPU Usage: {cpu_percent}%")
#         time.sleep(interval)

# # Создаем объект Event для контроля состояния мониторинга
# stop_event = threading.Event()

# # Запуск мониторинга CPU в отдельном потоке
# monitor_thread = threading.Thread(target=monitor_cpu, args=(1, stop_event))
# monitor_thread.start()

# //////////////spart headers start///////////////////////////////

def random_headers():
    
    desktop_accept = [
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',     
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',                
        ]
    device_memoryHelper = [2,4,8,16,32]
    sett = set()
    finHeaders = []    
    finfinH = {} 
    
 
    headFront = [{
            'authority': 'www.booking.com',
            'accept': choice(desktop_accept), 
            'User-Agent': uagent.random,  
            'accept-language': 'en-US,en;q=0.8',
            # 'accept-language': 'ru-RU,ru;q=0.9',         
            # 'accept-language': f"'en-US,en;q=0.8', 'ru-RU,ru;q=0.9', 'uk-Uk,uk;q=0.5'",       
            'origin': 'https://www.booking.com/',
            'device-memory': f'{choice(device_memoryHelper)}'                  
            }
    ]

    headersHelper = [       
            {"sec-fetch-dest": "empty"},
            {"sec-fetch-mode": "cors"},
            {"sec-fetch-site": "same-origin"},
            {"accept-ch": "sec-ch-ua-model,sec-ch-ua-platform-version,sec-ch-ua-full-version"},
            {'cache-control': 'no-cache'},
            {'content-type': 'application/json'},
            {'rtt': '200'},
            {"ect": "4g"},
            {'sec-fetch-user': '?1'},
            {"viewport-width": "386"},            
            {'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"'},
            {'upgrade-insecure-requests': '1'}
    ]
    headersHelperFormated = []
    strr = ''
    for i in headersHelper[0:len(headersHelper)-random.randrange(0,len(headersHelper))]:
        strr += ((str(choice(headersHelper)))[1:-1]).strip() + ',' + ' '  
         
    sett.add(strr)    
    headersHelperFormated = list(sett)    
    finHeaders = headFront + headersHelperFormated
    finHeaders[1] = eval("{" + finHeaders[1] + "}")    
    finfinH.update(finHeaders[0])
    finfinH.update(finHeaders[1])   
    return finfinH

# //////////////smart headers start///////////////////////////////

# ////////// grendMather_controller block/////////////////////////////////////

def grendMather_controller(data):
    # print('hello controler')
    flagCount = 0
    # flagTest = True
    flag_photo = True
    flag_description = True 
    flag_facilities = True 
    flag_room = True 
    flag_room_block = True    
    black_list = []
    photoInd = 0
    descriptionInd = 0
    facilityInd = 0
    roomInd = 0
    room_blockInd = 0
    try:
        data_upz_hotels_item = data.split('SamsonovNik')[1]
    except Exception as ex:
        # print(f"48____{ex}")
        pass

    try:
        data_upz_hotels_item_dict = eval(data_upz_hotels_item)
    except Exception as ex:
        # print(f"53____{ex}")
        data_upz_hotels_item_dict = data_upz_hotels_item 
    try:
        hotelid = data_upz_hotels_item_dict["hotel_id"] 
    except Exception as ex:
        # print(f"61____{ex}")
        hotelid = 'not found'
    # print(hotelid)
    try:
        prLi_str = data.split('SamsonovNik')[0]
        try:
            prLi = eval(prLi_str)
        except Exception as ex:
            # print(f"str68___{ex}")
            prLi = prLi_str
            pass
    except Exception as ex:
        # print(f"str72___{ex}")
        pass 
    try:
        link = ''
        link = data_upz_hotels_item_dict["url"] 
        try:
            fixed_url = re.sub(r'\\/', '/', link)  
        except Exception as ex:
            # print(f"74____{ex}")
            fixed_url = data_upz_hotels_item_dict["url"]
    except Exception as ex:
        # print(f"str83___{ex}")
        try:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "fotos": 0,
                "description": 0,
                "facility": 0,
                "otziv": "?",
                "room": 0,
                "room_block": 0,
            })
        except Exception as ex:
            # print(f"91____{ex}")
            pass
        return [[None], black_list] 
    try:
        photoInd = data_upz_hotels_item_dict["fotos"]
    except:
        pass 
    try:
        descriptionInd = data_upz_hotels_item_dict["description"]
    except:
        pass 
    try:
        facilityInd = data_upz_hotels_item_dict["facility"] 
    except:
        pass
    try:
        roomInd = data_upz_hotels_item_dict["room"]
    except:
        pass
    try:
        room_blockInd = data_upz_hotels_item_dict["room_block"]
    except:
        room_blockInd = None     
    try:
        if photoInd == "1" or photoInd == 1:
            flag_photo = False
            flagCount += 1  
        if descriptionInd == "1" or descriptionInd == 1:
            flag_description = False
            flagCount += 1 
        if facilityInd == "1" or facilityInd == 1:
            flag_facilities = False
            flagCount += 1 
        if roomInd == "1" or roomInd == 1:
            flag_room = False
            flagCount += 1
        if room_blockInd == "1" or room_blockInd == 1:
            flag_room_block = False
    except:
        pass
    if flagCount == 4:  
        return [[None], black_list]     
    else:
        for _ in range(2):
            try:
                result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks = '', '', '', '', ''
          
                black_list = []
                proxy_item = {       
                    "https": f"http://{choice(prLi)}"          
                } 
                # print(proxy_item)
                # print(fixed_url)
                try:
                   headerss=random_headers()
                   
                except Exception as ex:
                    print(f"headers281____{ex}")
                # print(headerss)
                
                k = 2 / random.randrange(1, 5)
                m = 1 / random.randrange(1, 11)
                g = random.randrange(1, 5)
                n = round(g + k + m, 2) 
                time.sleep(n)  
                try:     
                    r = requests.get(fixed_url, headers=headerss, proxies=proxy_item)
                    # r.raise_for_status()
                    # print(r)
                    if r.status_code == 404: 
                        return None
                    if r.status_code == 200 and r.text is not None and r.text != '':
                        try:
                            if flag_photo == True:
                                try:
                                    result_photos_upz = photos_func.page_scraper_photos(r.text, hotelid)
                                except:
                                    result_photos_upz = None  
                            if flag_description == True:
                                try:                       
                                    result_description_upz = description_func.page_scraper_description(r.text, hotelid)                           
                                except:
                                    result_description_upz = None 
                                    # print(result_description_upz)
                            if flag_facilities == True:
                                try:
                                    result_facilities_upz = faciclities_func.page_scraper_facilities(r.text, hotelid)
                                except:
                                    result_facilities_upz = None

                            if flag_room == True:
                                try:
                                    result_rooms_upz = rooms_func.page_scraper_room(r.text, hotelid)
                                except:
                                    result_rooms_upz = None 

                            if flag_room_block == True:
                                try:
                                    upz_hotels_rooms_blocks = rooms_block_func.page_scraper_room_block(r.text, hotelid)
                                except:
                                    upz_hotels_rooms_blocks = None 
                            if result_photos_upz is None or result_description_upz is None  or result_facilities_upz is None or result_rooms_upz is None or upz_hotels_rooms_blocks is None:
                                continue                                                  
                        except Exception as ex:
                            # print(f"str225___{ex}")
                            # continue
                            pass
                        break
                    else:
                        continue
                except requests.exceptions.HTTPError as ex:
                    print(f"str44___HTTP error occurred: {ex}") 
                    continue

            except Exception as ex:
                # print(f"237____{ex}")
                continue
                # return [[None], black_list] 
        if flag_photo == True and result_photos_upz is None:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "fotos": 0,
            })
        if flag_description == True and result_description_upz is None:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "description": 0,
            })

        if flag_facilities == True and result_facilities_upz is None:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "facility": 0,
            }) 
        if flag_room == True and result_rooms_upz is None:
            # print("room condition")
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "room": 0,
            })

        if flag_room == True and upz_hotels_rooms_blocks is None:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "room_block": 0,
            })        
        try:
            # print(result_description_upz)
            return [[result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks], black_list] 
        
        except Exception as ex:
            # print(f"220____{ex}")
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "fotos": 0,
                "description": 0,
                "facility": 0,
                "otziv": "?",
                "room": 0,
                "room_block": 0,
            })
            return [[None], black_list] 
        
# ////////// grendMather_controller block end/////////////////////////////////////
#         
def proxy_reader():
    with open("proxy_booking.txt", encoding="utf-8") as f1:    
        prLi = ''.join(f1.readlines()).split('\n')
        prLi= list(i.strip() for i in prLi)
        prLi = list(filter(lambda item: item != '', prLi))
    return prLi


def father_multiprocessor(data_upz_hotels, cpu_count):
    print('hello multi')
    
    try:
        data_upz_hotels_new = eval(data_upz_hotels)
    except Exception as ex:
        data_upz_hotels_new = data_upz_hotels

    try:
        prLi = proxy_reader()
    except Exception as ex:
        pass

    try:
        data_upz_hotels_args = [f"{prLi}SamsonovNik{item}" for item in data_upz_hotels_new]
    except Exception as ex:
        pass

    def call_grendMather_controller(item):
        return grendMather_controller(item)

    try:
        finRes = Parallel(n_jobs=cpu_count, prefer="threads")(delayed(call_grendMather_controller)(item) for item in data_upz_hotels_args)
    except Exception as ex:
        print(f"Error: {ex}")
        return None

    return finRes



# def father_multiprocessor(data_upz_hotels, cpu_count):
#     print('hello multi')
#     from mpire import WorkerPool   
#     # n = multiprocessing.cpu_count() * 10  
#     try:
#         data_upz_hotels_new = eval(data_upz_hotels) 
#     except Exception as ex:
#         # print(f"277____{ex}")
#         data_upz_hotels_new = data_upz_hotels
#     try:
#         prLi = proxy_reader()
#     except Exception as ex:
#         # print(f"283____{ex}")
#         pass
#     try:        
#         data_upz_hotels_args = list(f"{prLi}SamsonovNik{item}" for item in data_upz_hotels_new)
#     except Exception as ex:
#         # print(f"288____{ex}")
#         pass
#     try:
#         with WorkerPool(n_jobs = cpu_count) as p2:
#             # print('hello multi')                                
#             finRes = p2.map(grendMather_controller, data_upz_hotels_args)
#     except Exception as ex:
#         print(f"295____{ex}")
#         pass
#     # writerr.writerr(finRes) 
#     try:  
#         return finRes
#     except Exception as ex:
#         # print(f"300____{ex}")
#         return None

def pattern_cycles(data, cpu_count):
    # print('helo pattern_cycles')
    finRes = []
    black_list = []
    try:
        finRes = father_multiprocessor(data, cpu_count)
    except Exception as ex:
        print(f"422____{ex}")
        pass
    # try:
    #     writerr.writerr(finRes)
    # except Exception as ex:
    #     # print(f"378____{ex}")
    #     pass
    try:
        db_writerrr.db_wrtr(finRes)
    except Exception as ex:
        # print(f"378____{ex}")
        pass
    try:
        black_list = b.black_filter(finRes) 
    except Exception as ex:
        # print(f"390____{ex}")
        pass
    try:
       return black_list
    except:
        return None

def cycles_worker(**args_cycles):   
    black_list = []
    ex_list = []

    exceptions_data = args_cycles["exceptions_data"]
    # print(type(exceptions_data))
    # return
    try:
        
        n1=int(args_cycles["n1"])
        # print(type(n1))
        n2=int(args_cycles["n2"])
        interval=int(args_cycles["interval"])
        from_item=int(args_cycles["from_item"])
        len_items=int(args_cycles["len_items"])
        counter=int(args_cycles["counter"])
        flag_end_cycles=args_cycles["flag_end_cycles"]
        cpu_count = int(args_cycles["cpu_count"])
    except Exception as ex:
        print(f"441____{ex}")


    try:
        for item in exceptions_data:
            ex_list += item
    except:
        pass
    try:
        if flag_end_cycles == True:
            print('hello end_flag_cycles')
            try:
                black_list = pattern_cycles(ex_list, cpu_count)
                try:
                   bl_writerr.bl_db_wrtr(black_list)
                except Exception as ex:
                   print(f"355____{ex}")
                cleanup_cache()               
            except Exception as ex:
                print(f"358____{ex}")
            return print('Finish')
        else:            
            try:
                counter +=1
                n1 = (counter * interval) - interval + 1 + from_item
                n2 = (counter * interval) + from_item
                # print(n1)
                # print(n2)
                # print(type(flag_end_cycles))
                # return

                interval_chekcer = len_items - n2
                if interval_chekcer <= interval:
                    n2 = len_items
                    flag_end_cycles = True
                else:
                    pass

                    # print(f"362___{n2}")
            except Exception as ex:
                # print(f"343____{ex}")
                pass
            # print(f"348___{n1, n2}")

            if len(ex_list) != interval and len(ex_list) < interval:
                try:       
                    # const_data = json_reader_test.data_upz_hotels_func()    
                    const_data = db_reader.db_opener(n1, n2)
                    # print(const_data)
                except Exception as ex:
                    print(f"443____{ex}")
                try:
                    black_list = pattern_cycles(const_data, cpu_count)
                except:
                    pass
                try:
                    exceptions_data.append(black_list)
                except Exception as ex:
                    # print(f"398____{ex}")
                    pass
                cleanup_cache()
                args_cycles = {
                    'exceptions_data': exceptions_data,
                    'n1': n1,
                    'n2': n2,
                    'interval': interval,
                    'from_item': from_item,
                    'len_items': len_items,
                    'counter': counter,
                    'flag_end_cycles': flag_end_cycles,
                    'cpu_count': cpu_count
                }
                try:
                    cycles_worker(**args_cycles) 
                except Exception as ex:
                    # print(f"408____{ex}")
                    pass
            elif len(ex_list) == interval or len(ex_list) > interval:
                # print('hello exlist')
                exceptions_data = []
                black_list = pattern_cycles(ex_list, cpu_count)   
                try:
                    bl_writerr.bl_db_wrtr(black_list)
                except Exception as ex:
                    print(f"412____{ex}") 
                # bl_db_wrtr(black_list)
                args_cycles = {
                    'exceptions_data': exceptions_data,
                    'n1': n1,
                    'n2': n2,
                    'interval': interval,
                    'from_item': from_item,
                    'len_items': len_items,
                    'counter': counter,
                    'flag_end_cycles': flag_end_cycles,
                    'cpu_count': cpu_count
                }

                try:
                    cycles_worker(**args_cycles) 
                except Exception as ex:
                    # print(f"408____{ex}")
                    pass

    except Exception as ex:
        # print(f"334____{ex}")
        pass

def cleanup_cache():
    try:
        import os
        try:
            cache_dir = tempfile.mkdtemp()
        except Exception as ex:
            # print(f"386____{ex}")
            pass    
        try:
            if os.path.exists("__pycache__"):
                shutil.rmtree("__pycache__")
        except Exception as ex:
            # print(f"392____{ex}")
            pass  
        try:
            if os.path.exists("./utilsss/__pycache__"):
                shutil.rmtree("./utilsss/__pycache__")
        except Exception as ex:
            print(f"445____{ex}")
            pass 
        try:
            if os.path.exists("./scrapers_funcs/__pycache__"):
                shutil.rmtree("./scrapers_funcs/__pycache__")
        except Exception as ex:
            print(f"451____{ex}")
            pass 
        try:
            if os.path.exists("./db_all/__pycache__"):
                shutil.rmtree("./db_all/__pycache__")
        except Exception as ex:
            print(f"457____{ex}")
            pass  
        # secondary_funcs  
        try:
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)
        except Exception as ex:
            # print(f"396____{ex}")
            pass
    except Exception as ex:
        print(f"551____{ex}")
    

  
def main():
    args_cycles = {
        'exceptions_data': [],
        'n1': 0,
        'n2': 0,
        'interval': 1000,
        'from_item': 5000,
        'len_items': 5100,
        'counter': 0,
        'flag_end_cycles': False,
        'cpu_count': 22
    }

    try:
        cycles_worker(**args_cycles)
    except Exception as ex:
        print(f"454____{ex}")

if __name__ == "__main__":
    try:
        atexit.register(cleanup_cache)
    except Exception as ex:
        print(f"461____{ex}")
    start_time = time.time() 
    main() 
    finish_time = time.time() - start_time
    print(f"Total time:  {math.ceil(finish_time)} сек")
    # stop_event.set()
    # monitor_thread.join()
    try:
        sys.exit()
    except Exception as ex:
        print(f"467______{ex}")
  




# u9FSEvF3:igzQ94p1@45.132.207.81:62036
# u9FSEvF3:igzQ94p1@154.7.205.72:64700
# u9FSEvF3:igzQ94p1@154.7.207.155:63732



# u9FSEvF3:igzQ94p1@185.97.76.249:62362
