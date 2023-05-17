def black_filter(finRes):
    d_lackList = []
    sorted_blackList = []
    refactor_blackList = []
    print('hello b_filter_func')
    # try:
    #     resBlackList = eval(finRes)
    # except Exception as ex:
    #     print(f"308____{ex}")
    #     resBlackList = finRes

    for t in finRes:
        try:
           d_lackList.append(t[1])
        except:
            continue
    try:
        d_lackList = list(filter(None, d_lackList))                
        d_lackList = list(filter([], d_lackList))
    except Exception as ex:
        print(f"315____{ex}")
    try:
        for lst in d_lackList:
            merged_dict = {}
            for dct in lst:
                hotel_id = dct["hotel_id"]
                url = dct["url"]
                if hotel_id not in merged_dict:
                    merged_dict[hotel_id] = {"hotel_id": hotel_id, "url": url}
                merged_dict[hotel_id][list(dct.keys())[2]] = dct[list(dct.keys())[2]]
            sorted_blackList.append(list(merged_dict.values()))
        for item in sorted_blackList:
            refactor_blackList += item

        for rfi in refactor_blackList:            
            if "fotos" not in rfi:
                rfi.setdefault("fotos", 1)
            if "description" not in rfi:
                rfi.setdefault("description", 1)
            if "facility" not in rfi:
                rfi.setdefault("facility", 1)
            if "otziv" not in rfi:
                rfi.setdefault("otziv", '?')
            if "room" not in rfi:
                rfi.setdefault("room", 1)
            if "room_block" not in rfi:
                rfi.setdefault("room_block", 1)

    except Exception as ex:
        # print(f"327____{ex}")
        pass
    try:
        print(f"refactor_blackList___53str__len__{len(refactor_blackList)}")
        return refactor_blackList
    except Exception as ex:
        # print(f"331____{ex}")
        return None

