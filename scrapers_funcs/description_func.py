from bs4 import BeautifulSoup

def page_scraper_description(resHtml, hotelid):
    # print('hello description!')
    result_description_upz = []
    try:
        soup1 = BeautifulSoup(resHtml, "lxml")  
        # print(soup1)
    except Exception as ex:
        # print(f"description____str19___{ex}") 
        # pass
        return None 

    try:
        description_block = soup1.find("div", attrs={"class": "hp_desc_main_content"})
        description = description_block.get_text(strip=True, separator="\n")

        result_description_upz.append({
            "id": "",
            "hotelid": hotelid,
            "enusname": description,
        })

    except Exception as ex:
        # print(f"description_func___str32___{ex}") 
        # pass
        return None 

    try:
        return result_description_upz[0] 
    except Exception as ex:
        # print(f"description_func___str39___{ex}") 
        return None 
