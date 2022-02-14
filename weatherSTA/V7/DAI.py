import time, DAN, requests, weatherSTA

ServerURL = 'http://IP:9999'
Reg_addr = 'None'

DAN.profile['dm_name']='WeatherSTA'
DAN.profile['df_list']=['HumidityID-I', 'RainID-I', 'TemperatureID-I', 'WindSpeedID-I']
DAN.profile['d_name']= 'GovSTA'

DAN.device_registration_with_retry(ServerURL, Reg_addr)

while True:
    try:
        weather_list = weatherSTA.fetch_data()
        
        for item in weather_list:
            DAN.push ('TemperatureID-I', item[1],item[0])    
            print(item[1],item[0])
            DAN.push ('HumidityID-I'   , item[2],item[0])    
            print(item[2],item[0])
            DAN.push ('RainID-I'       , item[3],item[0])    
            print(item[3],item[0])
            DAN.push ('WindSpeedID-I'  , item[4],item[0])    
            print(item[4],item[0])
            time.sleep(5)

    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

    time.sleep(5)

