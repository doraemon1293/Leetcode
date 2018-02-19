# coding=utf-8
'''
Created on 2016�?11�?8�?

@author: Administrator
'''

import time


class Solution(object):

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(points)):
            distances = {}
            for j in range(len(points)):
                dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                distances.setdefault(dis, 0)
                distances[dis] += 1
            for x in distances.values():
                ans += x * (x - 1)
        return ans


start = time.time()
points = [[6685, 436], [910, -8106], [5336, 5260], [5246, 2939], [8124, -514], [6843, -9452], [5766, -3602], [1434, 499], [1213, -5984], [4971, 7728], [8164, -3594], [888, 5410], [5507, -8366], [8305, 5133], [6444, -5288], [3472, -519], [1500, -9265], [1376, 3188], [5995, 2974], [6127, 471], [2460, -677], [1020, 8226], [2073, -1194], [8725, 3286], [2822, -9951], [7366, -2662], [6455, -5394], [9100, -1686], [2592, 7405], [3447, -4611], [8469, -6728], [4870, -3679], [4007, -3754], [9509, 6354], [9220, -8011], [6825, 8032], [7664, 4197], [6259, 9737], [9355, -5016], [9375, -1471], [5033, 3093], [5867, -2160], [7699, 1320], [6155, -9708], [8725, 9602], [2033, -6453], [9226, 6903], [9868, -6767], [9502, -4270], [5939, 5074], [7719, 9117], [3107, 1735], [3314, -634], [1472, -978], [702, 7199], [7551, 2088], [292, -229], [9928, -2009], [1091, 2435], [4635, -3832], [2038, -3332], [9715, 1264], [3572, 5936], [850, 9426], [1666, -6859], [4500, -4263], [2258, -2393], [7472, 1925], [3325, -1056], [947, -5972], [6143, 4850], [6116, 6435], [4621, 2396], [778, -4288], [4832, -4586], [1881, 3222], [8434, 7948], [838, -1642], [3884, -1960], [7784, 1902], [1182, -7715], [7639, -208], [6244, 5111], [1717, 9570], [407, 9016], [3598, -7098], [3867, 6066], [5689, 4840], [4814, 6468], [553, -354], [8234, -1214], [9220, -3332], [3086, -9941], [5027, 3323], [4451, 9163], [5225, 5633], [1448, -7135], [5426, -2307], [7976, -6505], [7263, 8384], [8864, -2787], [7638, 2731], [3279, 3328], [7571, -5555], [9796, -5524], [444, -1970], [9614, -336], [1050, -947], [6075, -7571], [2376, 527], [1593, -6047], [2512, 9393], [6818, -5710], [7086, -8853], [7786, 701], [5883, -3350], [7914, 3521], [5733, 7545], [6849, 9656], [8343, 6645], [485, -1213], [1027, -3549], [8451, -1570], [5504, -9121], [7211, 4232], [7758, -1196], [8186, 270], [4550, -4996], [4561, 1636], [2503, 8699], [8690, 8386], [1701, 2956], [1908, 3786], [6854, 5109], [9794, -4803], [8107, 279], [3984, -4514], [3083, -1213], [3916, -5061], [6018, -8872], [9172, 3776], [6284, 7358], [4047, 834], [8714, 4960], [8823, 7570], [11, 3865], [5956, -1936], [6821, -5784], [8202, 27], [9326, -2004], [1576, -6215], [4628, -8088], [9271, -2289], [700, 9540], [9002, 3070], [7020, -1826], [6847, -6696], [1884, -2754], [491, 6951], [2206, -4334], [4521, -1431], [9531, -3171], [6633, -7296], [1046, 4835], [2732, -3276], [9183, -5692], [509, 3811], [6221, 6132], [7874, 3273], [5672, -3123], [6343, 2692], [1403, -458], [5997, 3288], [6788, -7160], [6591, 8994], [8506, -8888], [3915, -5611], [7941, -9452], [7093, 5339], [1735, 6177], [8415, 919], [486, -4724], [1082, -6941], [1409, 8957], [2684, 7081], [2186, 9027], [6126, 3589], [4922, 8475], [6877, -8290], [1315, 3468], [7057, -3827], [932, -9028], [562, 5226], [7873, 4007], [6917, -392], [185, -4667], [6879, -2977], [6961, 4314], [82, -1630], [3271, -7234], [1804, 1809], [8145, -2070], [5398, -6933], [6405, -1372], [4778, -5928], [8448, 8187], [245, -619], [9159, 7159], [959, 3384], [1166, -2124], [9345, -8649], [3209, 6224], [8374, -9829], [538, 8456], [4893, -9839], [7574, -6951], [1970, 2072], [979, 3721], [1491, 3736], [2349, 2621], [7808, -9203], [808, -5595], [6530, -32], [1564, -2511], [3352, 2731], [5366, -7303], [4082, -5073], [5274, 8809], [1450, -7836], [3617, -7304], [8678, 1192], [5745, -3000], [9616, 6725], [721, 1107], [6813, 9422], [3729, -9026], [220, 4537], [5379, -6898], [857, -6704], [592, -9438], [6027, -4042], [3259, -3539], [7237, 4885], [5270, -1312], [3402, 5240], [1384, 2080], [6432, 7129], [9080, -7600], [206, 6154], [3507, 3372], [5576, 7236], [4346, 2148], [1774, 6077], [5251, 2631], [9373, -7805], [3193, 5400], [4505, 2805], [8214, 1742], [4042, 9836], [6782, 7444], [5076, -5482], [9524, 7860], [8000, -5043], [260, -1794], [1111, 3768], [7930, 3039], [7356, 2276], [5188, 9130], [8354, 6791], [8114, -2273], [5338, 7659], [9480, 9843], [6816, 4046], [1585, 859], [3882, -5280], [8303, -4689], [9238, 4180], [3171, -2762], [5489, 9784], [1797, 6600], [9904, -273], [5991, 7260], [2004, -2469], [6391, -3290], [674, -9143], [789, 6012], [8516, 269], [5855, -8315], [4315, -6207], [2544, 4550], [8513, 7199], [9861, 4103], [7731, -6968], [1342, -6780], [9168, -509], [6172, -928], [9218, 8516], [6333, 7574], [6047, 9076], [636, -3278], [9933, 1426], [2734, 4801], [1695, 4942], [6486, -7637], [5087, -4618], [6913, -6400], [8934, 6774], [4055, -6983], [6158, 1749], [6238, 5327], [1240, 8762], [751, -9541], [7278, -2916], [4385, 9678], [6160, 5022], [6400, -7555], [6448, -4514], [7247, -5505], [6780, 85], [6858, 1867], [1820, -9877], [1819, -2894], [6897, -4125], [123, -592], [7624, 2713], [1087, 8865], [1476, -8162], [5676, -4894], [8923, -3587], [4784, 1435], [1435, -2464], [3881, -5765], [9375, -2520], [8731, -3845], [3917, 1941], [8023, -4263], [2065, -3806], [9195, -1038], [2069, 9319], [4722, -3954], [2032, 5809], [1263, 9860], [7648, 6939], [4967, -7077], [3352, -3897], [4358, -8860], [3640, -1761], [5375, 9367], [5719, 4106], [5522, -363], [6048, 9897], [1726, 4465], [2444, -9078], [3427, 4513], [6593, 4502], [6911, -1375], [311, 8174], [4838, -5689], [5113, -3843], [7234, 4818], [8612, -8407], [2310, 8604], [6184, 7685], [7971, 8256], [8144, 9846], [7893, 544], [9743, 5971], [5009, 8539], [3245, -5212], [3053, -162], [9290, -36], [4816, -4046], [4491, 9654], [265, 9604], [2163, 7500], [774, 775], [5445, -6916], [9380, -8371], [7122, -2649], [9885, -4734], [7197, -5870], [2162, -6707], [6454, 7171], [1832, -301], [8311, 1237], [9538, 7602], [7554, 706], [9908, -7955], [6712, 173], [8001, -1125], [4025, -4872], [6002, 9470], [4564, -4618], [1100, -8314], [9086, 7337], [3304, 2635], [1468, 5466], [2280, 7922], [8989, 465], [3973, -2699], [8054, 9863], [1255, 5608], [569, -8837], [4005, 7281], [7688, -1641], [2508, 1714], [9839, 4863], [1184, 4403], [245, -1364], [6090, -4317], [5974, 5746], [4671, -6206], [1213, -3049], [8068, 6554], [3768, 8393], [3855, 1823], [8257, -8538], [3783, -4822], [8977, 4141], [8812, -3334], [2500, -8680], [8380, 2339], [6183, -4084], [3094, 2781], [905, 9184], [4816, 6879], [4931, -513], [7025, -7504], [2791, 1445], [9050, -3441], [9838, 9258], [8382, -1905], [7072, -7834], [3274, 6050], [6307, 2086], [9068, 5159], [9758, 3800], [3850, -7706], [9716, -3056], [1427, -3027], [2481, -3757], [3852, 3764], [5731, 7229], [2612, -1478], [8674, 1662], [5081, 8513], [7272, -184], [6608, -5655], [8334, 6234], [6747, -9007], [4672, 5815], [6152, 4431], [9615, 6354], [3077, -4317], [3298, -5496], [2657, -7869], [747, 2861], [5895, -7170], [91, -5141], [7704, 5117], [6522, 9138], [3630, -9854], [8954, 6591], [843, 3640], [9177, 7590], [4633, 3850], [3405, -2863], [4633, 9372], [3491, 7710], [1408, -6859], [8566, 417], [1625, -4335], [9630, 3872], [8496, -3927], [8732, 6200], [1191, 1606], [1690, 1173], [1752, 6996], [7764, 2596], [636, 3294], [186, -4731], [7144, 9944], [2406, -1871], [5668, 2249], [5839, 3428], [1743, -5595], [3845, 3368], [70, 9828], [3592, 4918], [5901, -7676], [7471, -2908], [3930, 9161], [4618, -4317], [6158, 8734], [4631, -3206], [2028, -5183], [8416, 9172], [1113, 7174], [3653, 3134], [5776, -508]]
print Solution().numberOfBoomerangs(points)
print time.time() - start

