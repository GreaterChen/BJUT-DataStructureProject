import requests

places_all = []

buildings = [
    # 1号楼
    "北京工业大学学生公寓-2号楼",
    "天天餐厅(工业大学店)",
    "北京工业大学学生公寓-3号楼",
    # 4号楼
    "北京工业大学校医院",
    "北京工业大学公共浴室",
    "北京工业大学金工楼",
    # 西门
    # 一教
    "北京工业大学第二教学楼",
    "北京工业大学材料楼",
    "北京工业大学教育部科技普查工作站",  # 旧图
    "北京工业大学棋牌俱乐部",  # 礼堂
    "北京工业大学数理楼",
    "北京工业大学游泳馆",
    # 10、11号楼
    "北京工业大学运动场",
    # 13、14号楼
    # 东门
    "北京工业大学能源楼",
    "北京工业大学计算机学院",  # 信息楼
    "北京工业大学逸夫图书馆",
    "北京工业大学教学楼3",
    "北京工业大学知新园",
    "北京工业大学-后勤服务集团",  # 9号楼
    "北京工业大学美食园",
    "北京工业大学宿舍7号楼",
    # 8号楼
    "北京工业大学学生宿舍-12号楼",
    "北京工业大学京客隆便利店(奥运餐厅店)",
    "北京工业大学-第二田径场",
    "北京工业大学第四教学楼",
    "北京工业大学超显微学中心",  # 理科楼
    "北京工业大学艺术设计学院",
    "北京工业大学经管楼",
    "北京工业大学日新广场",  # 科学楼
    # 5号楼
    # 6号楼
    "北京工业大学-档案馆",  # 人文楼
    # 南门
    "东方启明星(北工大校区)",  # 奥运场馆
    # 月亮湖
    "北京工业大学-实训楼",
    "北京工业大学交通楼",
    "北京工业大学软件楼",
    # 北门

]


def geocoding(address, currentkey):
    """
    address convert lat and lng
    :param address: address
    :param currentkey: AK
    :return: places_ll
    """
    url = 'http://api.map.baidu.com/geocoding/v3/?'
    params = {
        "address": address,
        "city": '北京市',
        "output": 'json',
        "ak": currentkey,
    }
    response = requests.get(url, params=params)
    answer = response.json()
    if answer['status'] == 0:
        tmpList = answer['result']
        coordString = tmpList['location']
        coordList = [coordString['lng'], coordString['lat']]
        places_all.append([currentkey, float(coordList[0]), float(coordList[1])])
    else:
        return -1


def GetRes():
    for build in buildings:
        geocoding(build, "5681U75p2vTVenUqtzsP1OTLUXFdFXx1")

    places_all.insert(0, ["北京工业大学1号楼", 116.485502, 39.884971])
    places_all.insert(4, ["北京工业大学4号楼", 116.487886, 39.884593])
    places_all.insert(8, ["北京工业大学西门", 116.484252, 39.883195])
    places_all.insert(9, ["北京工业大学一教", 116.485393, 39.883735])
    places_all.insert(16, ["北京工业大学10、11号楼", 116.489089, 39.884065])
    places_all.insert(18, ["北京工业大学13、14号楼", 116.490382, 39.883445])
    places_all.insert(19, ["北京工业大学东门", 116.49059, 39.883832])
    places_all.insert(28, ["北京工业大学8号楼", 116.488276, 39.880504])
    places_all.insert(37, ["北京工业大学5号楼", 116.487786, 39.879219])
    places_all.insert(38, ["北京工业大学6号楼", 116.487781, 39.878838])
    places_all.insert(40, ["北京工业大学南门", 116.486377, 39.877523])
    places_all.insert(42, ["北京工业大学月亮湖", 116.492168, 39.879689])
    places_all.insert(46, ["北京工业大学北门", 116.488447, 39.88523])

    f = open("address.txt", "w")
    for i, item in enumerate(places_all):
        f.write(str(i))
        f.write(' ')
        f.write(str(item[0]))
        f.write(' ')
        f.write(str(item[2]))
        f.write(',')
        f.write(str(item[1]))
        f.write('\n')
    f.close()
    # 116.48815658167098, 39.881251063643404
