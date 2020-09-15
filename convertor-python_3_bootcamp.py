def converter():
    
    time_dic = {'s':1, 'min':1/60, 'h':1/3600, 'day':1/86400, 'year':1/31536000 }
    len_dic = {'m':1, 'cm':100, 'mm':1000, 'km':1E-3, 'ft':3.2808, 'inch':39.3701,
               'yard':1.0936, 'mile':6.2137E-4, 'n mile':5.3996E-4}
    mass_dic = {'g':1, 'kg':1E-3, 'mg':1000, 'oz':3.5274E-2, 'lb':2.2046E-3}
    
    area_dic = {'m2':1, 'cm2':len_dic['cm']**2, 'mm2':len_dic['mm']**2, 'km2':len_dic['km']**2 ,
               'ft2':len_dic['ft']**2, 'inch2':len_dic['inch']**2, 'yard2':len_dic['yard']**2,
                'mile2':len_dic['mile']**2, 'acre':2.47105E-4}
    volume_dic = {'m3':1, 'cm3':len_dic['cm']**3, 'mm3':len_dic['mm']**3, 'km3':len_dic['km']**3 ,
                'ft3':len_dic['ft']**3, 'inch3':len_dic['inch']**3, 'yard3':len_dic['yard']**3,
                'mile3':len_dic['mile']**3, 'liter':1000, 'usgal':2641.7, 'ukgal':2199.7}
    
    def get_attr(attr):
        #Numbers in the nested list are the powers of M, L and T respectively in the attribute's dimension
        attr_dic = {
                    'temperature':['T',None], 'currency':['cur',None], 'length':['L',[0,1,0]], 'area':['L2',[0,2,0]],
                    'volume':['L3',[0,3,0]], 'time':['t',[0,0,1]], 'mass':['m',[1,0,0]], 'weight':['w',None],
                    'velocity':['v',[0,1,-1]], 'acceleration':['a',[0,1,-2]], 'density':['d',[1,-3,0]],
                    'angle': ['angle',None], 'force':['F',None], 'pressure':['p',[1,-2,-2]], 'torque':['T',[1,2,-2]],
                    'power':['P',[1,2,-3]]
                   }
        

        return attr_dic[attr.lower()][0], attr_dic[attr.lower()][1]

    
    print("temperature, currency, length, area, volume, time, mass, weight, velocity",
          "acceleration, density, angle, force, pressure, torque, power")
    
    attr,powers_list = get_attr(str(input("What are you converting?")))
    value,unit_from,unit_to = input("Enter: the value,'unit from','unit to':").split(',')
    value = float(value)
        
    if attr == 't':
        conv_factor = time_dic[unit_to]/time_dic[unit_from]
    
    elif attr == 'm':
        conv_factor = mass_dic[unit_to]/mass_dic[unit_from]
        
    elif attr == 'L':
        conv_factor = len_dic[unit_to]/len_dic[unit_from]
    
    elif attr == 'L2':
        conv_factor = area_dic[unit_to]/area_dic[unit_from]
        
    elif attr == 'L3':
        conv_factor = volume_dic[unit_to]/volume_dic[unit_from]
        
    elif attr == 'cur':
        import requests
        import json
        
        #def jprint(obj):
            # create a formatted string of the Python JSON object
            #text = json.dumps(obj, sort_keys=True, indent=2)
            #print(text)
        
        query = {"function" : "CURRENCY_EXCHANGE_RATE" ,"from_currency" : unit_from,
                 "to_currency" : unit_to , "apikey" : "CURRENCY_EXCHANGE_RATE",
                 "x-rapidapi-host": "alpha-vantage.p.rapidapi.com",
                 "x-rapidapi-key": "7a4e9ac94dmshc7bfd4733b5cf5dp136273jsnef36331218a2"}
        
        response = requests.get("https://www.alphavantage.co/query?" , params = query)
        conv_factor = float(response.json()["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        #jprint(response.json())
        
    elif attr == 'temp':
        pass
    
    
        
    print(f"{value} {unit_from} is equal to {value*conv_factor} {unit_to}")
    
    return None