# import main
from bs4 import BeautifulSoup
import re

def page_scraper_photos(resHtml, hotelid):
    result_photos_upz = []

    try:
        soup1 = BeautifulSoup(resHtml, "lxml")       
    except Exception as ex:
        # print(f"str102___{ex}") 
        # pass
        return None 

    try:
        preview_list_photo = []
        imgBlock1 = soup1.find_all('a', attrs={'class': 'bh-photo-grid-item', 'class': 'bh-photo-grid-side-photo', 'class': 'active-image' }) 
        imgBlock2 = soup1.find('div', attrs={'id': 'hotel_main_content'}).find_all('div', class_='bh-photo-grid-thumb-cell')
        try:
            for src in imgBlock1:
                try:
                    photo_item_id = src.get('data-id')
                except:
                    pass
                try:
                    photo_item_title = src.find('img').get('alt')

                except:
                    pass 
                preview_list_photo.append({
                    'photo_item_id': photo_item_id,
                    'photo_item_title': photo_item_title,
                }) 
        except Exception as ex:
            # print(f"str65__{ex}") 
            pass

        try:
            for src in imgBlock2:
                if src.find('a').find('img').get('src') != None:

                    try:
                        photo_item_id = src.find('a').get('data-id')
                    except:
                        pass 

                    try:
                        photo_item_title = src.find('a').find('img').get('alt')
                    except:
                        pass

                    preview_list_photo.append({
                        'photo_item_id': photo_item_id,
                        'photo_item_title': photo_item_title,
                    }) 
        except Exception as ex:
            # print(f"str94__{ex}")
            pass
    except Exception as ex:
        # print(f"str94__{ex}")
        pass

    try:
        clean_links_set_max1280x900 = set()
        clean_links_list_max1280x900 = []
        words = resHtml.split()
        links = set()
        for word in words:
            if re.search(r"https://cf\.bstatic\.com/xdata/images/hotel.*", word):
                links.add(word)
        dirty_links = list(links)
        for link in dirty_links:
            match = re.search(r"https://cf\.bstatic\.com/xdata/images/hotel/max1280x900.*?&hp=1", link)
            if match:
                clean_links_set_max1280x900.add(match.group(0))
        clean_links_list_max1280x900 = list(clean_links_set_max1280x900)
        for url_max in clean_links_list_max1280x900:
            try:
                photo_id = url_max.split('/')[-1].split('.')[0].strip()
            except:
                try:
                    match = re.search(r"/(\d{9})\.", url_max)
                    if match:
                        photo_id = match.group(1)
                except:
                    photo_id = 'not found'
            try:      
                url_square60 = re.sub(r'max1280x900', 'square60', url_max)
            except:
                url_square60 = 'not found' 
            
            result_photos_upz.append({
                "hotelid": hotelid,
                'photo_id': photo_id,
                "tags": '',
                'url_max': url_max,
                'url_square60': url_square60                  
            })
        try:
            for all_photo_item in result_photos_upz:
                for prev_photo_item in preview_list_photo:
                    if all_photo_item["photo_id"] == prev_photo_item["photo_item_id"]:
                       all_photo_item["tags"] = prev_photo_item["photo_item_title"]
            result_photos_upz.sort(key=lambda hotel: hotel['tags'] == '')
        except Exception as ex:
            print(f"str124__{ex}")                
        
    except Exception as ex:
        # print(f"str105__{ex}") 
        # pass
        return None 

    try:

        return result_photos_upz   
    except:
        return None
    


    
# page_scraper_photos()




    # import requests
    # result_photos_upz = []
    # hotelid = 92498244
    # # print('hello photos!')
    # url = 'https://www.booking.com/hotel/uz/hilton-tashkent-city.html'
    # r = requests.get(url, timeout=(9.15, 30.15))
    # # soup = BeautifulSoup(r.content, "html.parser")
    # resHtml = r.text
# with open("responsePhotos_1.html", "w") as f:
#     f.write(resHtml)

# try:
#     with open(f'test_photo1.json', "w", encoding="utf-8") as file: 
#         json.dump(result_photos_upz, file, indent=4, ensure_ascii=False)
# except Exception as ex:
#     print(f"str348__{ex}")
    
