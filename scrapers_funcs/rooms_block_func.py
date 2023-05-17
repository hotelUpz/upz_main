from bs4 import BeautifulSoup
import re
from . import facilities_data

def page_scraper_room_block(resHtml, hotelid):
    meal_facilities_const = [1, 166, 167, 168, 169, 170, 171, 217, 218, 219, 220]
    result_room_block_upz = []
    # print('hello room block')

    try:   
        soup1 = BeautifulSoup(resHtml, "lxml")      
    except Exception as ex:
        # print(f"str102___{ex}") 
        return None 

    try:
        all_sripts_list = []
        scripts_fraction_list = []
        all_scripts_str = ''
        all_sripts_list = soup1.find_all('script')
        for fr in all_sripts_list:
            all_scripts_str += str(fr) + '\n'
        scripts_fraction_list = all_scripts_str.split('{}')           
        section = soup1.find('section', class_='roomstable')
        list_elements = section.find_all('div', recursive=False)
        for i, item in enumerate(list_elements):
            room_id = ''
            name_room = ''
            gross_price = 'api info'
            currency = 'api info'
            max_occupancy = ''
            nr_children = ''
            nr_adults = ''
            mealplan = ''
            all_inclusive = 'not found'
            room_surface_in_m2 = 'not found' 
            # all_facilities_of_room = ''            
            try:
                room_id_pre = item.find('a').get('href')            
                room_id = re.findall('\d+', room_id_pre)[0]                
            except:
                room_id = 'not found'
                continue
  
            try:
                name_room_pre = item.find('a')
                name_room = name_room_pre.get_text(strip=True, separator="\n")
            except:
                name_room = 'not found'
                continue 

            try:
                for element in item.find_all(True):
                    aria_label = element.get('aria-label')
                    if aria_label:
                        max_occupancy = aria_label.strip()                     
                        break
            except:
                max_occupancy = 'not found'

            try:            
                pattern1 = f'"roomId":{room_id}.*__typename":"RTRoomCard".*"description".*"hasRoomInventory".*' 
                # pattern_meal = r'(?:"mealPlans"::\[[^]]*?\]|"mealPlans":^\[\s*\]$)'
                pattern_meal = f'"facilities":\[[^]]*?\]'
                for fr in scripts_fraction_list:
                    match1 = re.search(pattern1, fr)                                   
                    if match1:
                        match_general_block = match1.group()

                        try:
                            match_allow_children = re.search(r'"maxChildren":\d', match_general_block)
                            nr_children = match_allow_children.group().split(':')[1].strip() 
                        except:
                            nr_children = 'not found'
                        try:
                            match_nr_adults = re.search(r'"maxPersons":\d', match_general_block)
                            nr_adults = match_nr_adults.group().split(':')[1].strip() 
                        except:
                            nr_adults = 'not found'
                        try:
                            match2 = re.findall(pattern_meal, str(match_general_block))
                            list_fs_meal = []
                            meal_facilities_set_list = []
                            if match2:
                                for mf in match2:
                                    list_fs_meal += eval(mf.split(':')[1].strip())
                            meal_facilities_set_list = list(set(list_fs_meal))
                            common_facilities_items = [item for item in meal_facilities_const if item in meal_facilities_set_list]
                            if common_facilities_items:
                                for fs in common_facilities_items:
                                    mealplan += facilities_data.roomfacility[str(fs)] +'\n' 
                            else:
                                mealplan = "not found"
                        except:
                            mealplan = "not found"
                        
                        # try:
                        #     for fs in meal_facilities_set_list:
                        #         all_facilities_of_room += facilities_data.roomfacility[str(fs)] +'\n'
                        # except:
                        #     all_facilities_of_room = "not found"                
            except:
                try:
                    max_occupancy2 = max_occupancy             
                    nr_children = max_occupancy.split(',')[1].strip()                    
                except: 
                    nr_children = 'not found'                
                try:
                    nr_adults = max_occupancy2.split(',')[0].strip()
                except:
                    nr_adults = 'not found'           
            try:
                result_room_block_upz.append({
                    "hotelid": hotelid,
                    'room_id': str(room_id),                    
                    'gross_price': str(gross_price), 
                    'currency': str(currency),  
                    'room_name': str(name_room),                  
                    'nr_children': str(nr_children),
                    'max_occupancy': str(max_occupancy),
                    'mealplan': str(mealplan),
                    'room_surface_in_m2': str(room_surface_in_m2),
                    'nr_adults': str(nr_adults),
                    'all_inclusive': str(all_inclusive),
                    # 'all_facilities_of_room': str(all_facilities_of_room),
                })
            except Exception as ex:
                # print(f"150____{ex}") 
                # pass
                return None 
    except Exception as ex:
        # print(f"154____{ex}")
        # pass
        return None
    try:
        # print(result_room_block_upz)
        return result_room_block_upz
    except:
        return None

# python rooms_block_func.py