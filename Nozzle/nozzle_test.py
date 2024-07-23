
def k_factor(k, orifice_num, x, y, z):
    for n in orifice_num:
        if n == k:
            return x * n ** 2 + y * n - z
    return None

def product_flow_rate(num_nozzles, sfor, operating_pressure, lsg):
    if sfor == "**":
        return "N/A"
    return num_nozzles * sfor * operating_pressure ** 0.5 / lsg ** 0.5

def flowrate(pfr, num_nozzles, operating_pressure):
    if pfr == "N/A":
        return "N/A"
    return pfr / num_nozzles * (69 / operating_pressure) ** 0.5

def spray_angle_1(pfr, fr, x):
    if pfr == "N/A":
        return "N/A"
    return 0.2641 * fr + x

def spray_angle_2(pfr, x, fr, y, z):
    if pfr == "N/A":
        return "N/A"
    return x * fr ** 2 + y * fr + z

def dropsize(spa, operating_pressure, k, x, y, z):
    if spa == "N/A":
        return "N/A"
    return x * (operating_pressure * 14.5) ** y * (k / 1000) ** z

def powder_flow_rate(pfr, lsg, lpcs, ppcm):
    if pfr == "N/A":
        return "N/A"
    return pfr * lsg * lpcs / 100 * (1 + ppcm / 100)

def screen_for_orifice_range(k, orifice_num, ranges):
    results = {}
    for low, high, value, key in ranges:
        if low <= k <= high:
            results[key] = value
        else:
            results[key] = "**"
    return results

def tdl():
    tdl_num_nozzles = int(input("Number of Nozzles: "))
    swirl_input = input("Enter swirl number (e.g., SW1, SW2, etc.): ")
    k = float(input("Orifice Number: "))
    tdl_operating_pressure = float(input("Operating Pressure: "))
    tdl_lsg = float(input("Liquid Specific Gravity: "))
    tdl_spa = input("Spray Angle: ")
    tdl_lpcs = float(input("Liquid Per Cent Solids: "))
    tdl_ppcm = float(input("Powder Per Cent Moisture: "))

    tdl_orifice_num = [18, 20, 22, 24, 27, 30, 33, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]

    k_values = {
        'k1': k_factor(k, tdl_orifice_num, -0.00312, -0.4741, -3.90283),
        'k2': k_factor(k, tdl_orifice_num, 0.00166, -0.24556, 0.36082),
        'k3': k_factor(k, tdl_orifice_num, -0.0214, -2.9143, -71.774),
        'k4': k_factor(k, tdl_orifice_num, 0.00938, 0.23464, 4.07737),
    }

    ranges = [
        (21, 32, k_values['k1'], 'sfor1'), (29, 60, k_values['k2'], 'sfor2'), (49, 59, k_values['k3'], 'sfor3'),
        (17, 28, k_values['k4'], 'sfor4')]

    sfor_values = screen_for_orifice_range(k, tdl_orifice_num, ranges)
    pfr_values = {key: product_flow_rate(tdl_num_nozzles, sfor_values[key], tdl_operating_pressure, tdl_lsg) for key in sfor_values}
    fr_values = {key: flowrate(pfr_values[key], tdl_num_nozzles, tdl_operating_pressure) for key in pfr_values}

    powder_flow_rates = {key: powder_flow_rate(pfr_values[key], tdl_lsg, tdl_lpcs, tdl_ppcm) for key in pfr_values}

    swirl_number = int(swirl_input[3:])

    swirl_key = f'sfor{swirl_number}'
    k_key = f'k{swirl_number}'

    response = {
        "Number of Nozzles": tdl_num_nozzles,
        "Swirl Number": swirl_input,
        "Orifice Number": k,
        "Operating Pressure": tdl_operating_pressure,
        "Liquid Specific Gravity": tdl_lsg,
        "Liquid Flow Rate": pfr_values.get(swirl_key),
        "Liquid Per Cent Solids": tdl_lpcs,
        "Powder Per Cent Moisture": tdl_ppcm,
        "Powder Flow Rate": powder_flow_rates.get(swirl_key),
        "K Factor": k_values.get(k_key),
        "Screen for Orifice Range": sfor_values.get(swirl_key),
        "Flow Rate at 1000 psi": fr_values.get(swirl_key)
    }

    return response

def td():
    td_num_nozzles = int(input("Number of Nozzles: "))
    swirl_input = input("Enter swirl number (e.g., SW1, SW2, etc.): ")
    k = float(input("Orifice Number: "))
    td_operating_pressure = float(input("Operating Pressure: "))
    td_lsg = float(input("Liquid Specific Gravity: "))
    td_lpcs = float(input("Liquid Per Cent Solids: "))
    td_ppcm = float(input("Powder Per Cent Moisture: "))

    td_orifice_num = [34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 62, 64, 66, 67, 68, 70, 73, 75,
                      76, 80, 82, 85, 86, 88, 90, 91, 94, 97, 100, 103, 106, 109, 112, 115, 118,
                      121, 127, 133, 136, 142, 145, 148, 151, 154, 157]

    k_values = {
        'k1': 0.19 * k + 2.09,
        'k2': 0.38 * k - 3.8,
        'k3': k_factor(k, td_orifice_num, -0.000698, 0.513778, 5.602094),
        'k4': k_factor(k, td_orifice_num, 0.00187, 0.32312, -0.68223),
        'k5': k_factor(k, td_orifice_num, 0.0002403, 0.6758402, 7.503516),
        'k6': k_factor(k, td_orifice_num, 0.001007, 0.812664, 11.694463),
        'k7': k_factor(k, td_orifice_num, 0.000865, 1.128301, 21.295354),
        'k8': k_factor(k, td_orifice_num, 0.0014, 1.4509, 34.78843),
        'k9': k_factor(k, td_orifice_num, 0.0029, 1.5332, 34.527),
        'k10': k_factor(k, td_orifice_num, 0.00162, 2.16933, 62.616)
    }

    ranges = [
        (34, 60, k_values['k1'], 'sfor1'), (34, 82, k_values['k2'], 'sfor2'), (34, 105, k_values['k3'], 'sfor3'),
        (34, 137, k_values['k4'], 'sfor4'), (34, 145, k_values['k5'], 'sfor5'), (35, 153, k_values['k6'], 'sfor6'),
        (37, 153, k_values['k7'], 'sfor7'), (48, 160, k_values['k8'], 'sfor8'), (76, 160, k_values['k9'], 'sfor9'),
        (84, 160, k_values['k10'], 'sfor10')
    ]

    sfor_values = screen_for_orifice_range(k, td_orifice_num, ranges)
    pfr_values = {key: product_flow_rate(td_num_nozzles, sfor_values[key], td_operating_pressure, td_lsg) for key in sfor_values}
    fr_values = {key: flowrate(pfr_values[key], td_num_nozzles, td_operating_pressure) for key in pfr_values}
    spa_values = {
        'sfor1': spray_angle_1(pfr_values['sfor1'], fr_values['sfor1'], 60),
        'sfor2': spray_angle_1(pfr_values['sfor2'], fr_values['sfor2'], 50),
        'sfor3': spray_angle_2(pfr_values['sfor3'], -0.000284, fr_values['sfor3'], 0.187738, 52.394181),
        'sfor4': spray_angle_2(pfr_values['sfor4'], -0.000263, fr_values['sfor4'], 0.202401, 41.325448),
        'sfor5': spray_angle_2(pfr_values['sfor5'], -0.000129, fr_values['sfor5'], 0.14995, 35.403449),
        'sfor6': spray_angle_2(pfr_values['sfor6'], -0.0000376, fr_values['sfor6'], 0.0794284, 37.8196606),
        'sfor7': spray_angle_2(pfr_values['sfor7'], -0.0000173, fr_values['sfor7'], 0.0529205, 35.5265553),
        'sfor8': spray_angle_2(pfr_values['sfor8'], -0.00000774, fr_values['sfor8'], 0.03764802, 30.23508882),
        'sfor9': spray_angle_2(pfr_values['sfor9'], -0.000000423, fr_values['sfor9'], 0.015491835, 36.120970302),
        'sfor10': spray_angle_2(pfr_values['sfor10'], -0.000000776, fr_values['sfor10'], 0.014430671, 31.053166908)
    }

    ds_values = {
        'sfor1': dropsize(spa_values['sfor1'], td_operating_pressure, k, 618.3, -0.3102, 0.0627),
        'sfor2': dropsize(spa_values['sfor2'], td_operating_pressure, k, 1685.4, -0.3196, 0.3708),
        'sfor3': dropsize(spa_values['sfor3'], td_operating_pressure, k, 1020.1, -0.3484, 0.1493),
        'sfor4': dropsize(spa_values['sfor4'], td_operating_pressure, k, 727.6, -0.2587, 0.2122),
        'sfor5': dropsize(spa_values['sfor5'], td_operating_pressure, k, 837.3, -0.1845, 0.473),
        'sfor6': dropsize(spa_values['sfor6'], td_operating_pressure, k, 618.3, -0.3102, 0.0627),
        'sfor7': dropsize(spa_values['sfor7'], td_operating_pressure, k, 92.25, 0.006148, 0.132),
        'sfor8': dropsize(spa_values['sfor8'], td_operating_pressure, k, 535.5, -0.2293, 0.1268),
        'sfor9': dropsize(spa_values['sfor9'], td_operating_pressure, k, 530.6, -0.1126, 0.4453),
        'sfor10': dropsize(spa_values['sfor10'], td_operating_pressure, k, 618.3, -0.3102, 0.0627)
    }
    powder_flow_rates = {key: powder_flow_rate(pfr_values[key], td_lsg, td_lpcs, td_ppcm) for key in pfr_values}

    swirl_number = int(swirl_input[2:])

    swirl_key = f'sfor{swirl_number}'
    k_key = f'k{swirl_number}'

    response = {
        "Number of Nozzles": td_num_nozzles,
        "Swirl Number": swirl_input,
        "Orifice Number": k,
        "Operating Pressure": td_operating_pressure,
        "Liquid Specific Gravity": td_lsg,
        "Liquid Flow Rate": pfr_values.get(swirl_key),
        "Spray Angle at 69 bar": spa_values.get(swirl_key),
        "Droplet Size (Sauter Mean)": ds_values.get(swirl_key),
        "Liquid Per Cent Solids": td_lpcs,
        "Powder Per Cent Moisture": td_ppcm,
        "Powder Flow Rate": powder_flow_rates.get(swirl_key),
        "K Factor": k_values.get(k_key),
        "Screen for Orifice Range": sfor_values.get(swirl_key),
        "Flow Rate at 1000 psi": fr_values.get(swirl_key)
    }

    return response

tdl()