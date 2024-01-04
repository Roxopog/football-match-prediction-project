import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

Date = datetime(2021, 5, 5, 5, 15)
location ="Ankara"
def get_weather_data(date,location): 
    def generate_url(date, location):
    
        sehirler = {'Adana': {'havalimani': 'LTAF', 'ilce': 'seyhan'}, 'Adıyaman': {'havalimani': 'LTCP', 'ilce': 'adıyaman'}, 'Afyonkarahisar': {'havalimani': 'LTBZ', 'ilce': 'altıntaş'}, 'Ağrı': {'havalimani': 'LTCO', 'ilce': 'hamur'}, 'Aksaray': {'havalimani': 'LTAZ', 'ilce': 'gülşehir'}, 'Amasya': {'havalimani': 'LTAP', 'ilce': 'merzifon'}, 'Ankara': {'havalimani': 'LTAC', 'ilce': 'çubuk'}, 'Antalya': {'havalimani': 'LTAI', 'ilce': 'muratpaşa'}, 'Ardahan': {'havalimani': 'LTCF', 'ilce': 'kars'}, 'Artvin': {'havalimani': 'UGSB', 'ilce': 'adlia'}, 'Aydın': {'havalimani': 'LTBD', 'ilce': 'aydın'}, 'Balıkesir': {'havalimani': 'LTFD', 'ilce': 'edremit'}, 'Bartın': {'havalimani': 'LTAS', 'ilce': 'saltukova'}, 'Batman': {'havalimani': 'LTCJ', 'ilce': 'batman'}, 'Bayburt': {'havalimani': 'LTCD', 'ilce': 'erzincan'}, 'Bilecik': {'havalimani': 'LTBR', 'ilce': 'yenisehir'}, 'Bingöl': {'havalimani': 'LTCU', 'ilce': 'bingöl'}, 'Bitlis': {'havalimani': 'LTCL', 'ilce': 'siirt'}, 'Bolu': {'havalimani': 'LTAC', 'ilce': 'çubuk'}, 'Burdur': {'havalimani': 'LTCU', 'ilce': 'bingöl'}, 'Bursa': {'havalimani': 'LTBR', 'ilce': 'yenisehir'}, 'Çanakkale': {'havalimani': 'LTBH', 'ilce': 'çanakkale'}, 'Çankırı': {'havalimani': 'LTAC', 'ilce': 'çubuk'}, 'Çorum': {'havalimani': 'LTAP', 'ilce': 'merzifon'}, 'Denizli': {'havalimani': 'LTAY', 'ilce': 'çardak'}, 'Diyarbakır': {'havalimani': 'LTCC', 'ilce': 'baglar'}, 'Düzce': {'havalimani': 'LTBY', 'ilce': 'muttalip'}, 'Edirne': {'havalimani': 'LGAL', 'ilce': 'alexandroupoli'}, 'Elazığ': {'havalimani': 'LTCA', 'ilce': 'elazığ'}, 'Erzincan': {'havalimani': 'LTCD', 'ilce': 'erzincan'}, 'Erzurum': {'havalimani': 'LTCE', 'ilce': 'erzurum'}, 'Eskişehir': {'havalimani': 'LTBY', 'ilce': 'muttalip'}, 'Gaziantep': {'havalimani': 'LTAJ', 'ilce': 'oğuzeli'}, 'Giresun': {'havalimani': 'LTCB', 'ilce': 'trabzon'}, 'Gümüşhane': {'havalimani': 'LTCG', 'ilce': 'trabzon'}, 'Hakkari': {'havalimani': 'LTCW', 'ilce': 'yüksekova'}, 'Hatay': {'havalimani': 'LTDA', 'ilce': 'hatay-province'}, 'Iğdır': {'havalimani': 'LTCT', 'ilce': 'iğdır'}, 'Isparta': {'havalimani': 'LTFC', 'ilce': 'gönen'}, 'İstanbul': {'havalimani': 'LTBA', 'ilce': 'istanbul'}, 'İzmir': {'havalimani': 'LTBJ', 'ilce': 'gaziemir'}, 'Kahramanmaraş': {'havalimani': 'LTCN', 'ilce': 'marash'}, 'Karabük': {'havalimani': 'LTAL', 'ilce': 'kastamonu'}, 'Karaman': {'havalimani': 'LTAN', 'ilce': 'konya'}, 'Kars': {'havalimani': 'LTCF', 'ilce': 'kars'}, 'Kastamonu': {'havalimani': 'LTAL', 'ilce': 'kastamonu'}, 'Kayseri': {'havalimani': 'LTAU', 'ilce': 'kayseri'}, 'Kırıkkale': {'havalimani': 'LTAC', 'ilce': 'çubuk'}, 'Kırklareli': {'havalimani': 'LTBU', 'ilce': 'çorlu'}, 'Kırşehir': {'havalimani': 'LTAZ', 'ilce': 'gülşehir'}, 'Kilis': {'havalimani': 'LTAJ', 'ilce': 'oğuzeli'}, 'Kocaeli': {'havalimani': 'LTBQ', 'ilce': 'uzunçiftlik'}, 'Konya': {'havalimani': 'LTAN', 'ilce': 'konya'}, 'Kütahya': {'havalimani': 'LTBZ', 'ilce': 'altıntaş'}, 'Malatya': {'havalimani': 'LTAT', 'ilce': 'akçadağ'}, 'Manisa': {'havalimani': 'LTBT', 'ilce': 'akhisar'}, 'Mardin': {'havalimani': 'LTCR', 'ilce': 'kızıltepe'}, 'Mersin': {'havalimani': 'LTAF', 'ilce': 'seyhan'}, 'Muğla': {'havalimani': 'LTFE', 'ilce': 'milas'}, 'Muş': {'havalimani': 'LTCK', 'ilce': 'muş'}, 'Nevşehir': {'havalimani': 'LTAZ', 'ilce': 'gülşehir'}, 'Niğde': {'havalimani': 'LTAZ', 'ilce': 'gülşehir'}, 'Ordu': {'havalimani': 'LTCB', 'ilce': 'trabzon'}, 'Osmaniye': {'havalimani': 'LTDA', 'ilce': 'hatay-province'}, 'Rize': {'havalimani': 'LTFO', 'ilce': 'trabzon'}, 'Sakarya': {'havalimani': 'LTBQ', 'ilce': 'uzunçiftlik'}, 'Samsun': {'havalimani': 'LTFH', 'ilce': 'çarşamba'}, 'Siirt': {'havalimani': 'LTCL', 'ilce': 'siirt'}, 'Sinop': {'havalimani': 'LTCM', 'ilce': 'sinop'}, 'Sivas': {'havalimani': 'LTAR', 'ilce': 'sivas'}, 'Şanlıurfa': {'havalimani': 'LTCS', 'ilce': 'karaköprü'}, 'Şırnak': {'havalimani': 'LTCV', 'ilce': 'cizre'}, 'Tekirdağ': {'havalimani': 'LTBU', 'ilce': 'çorlu'}, 'Tokat': {'havalimani': 'LTAW', 'ilce': 'tokat'}, 'Trabzon': {'havalimani': 'LTCG', 'ilce': 'trabzon'}, 'Tunceli': {'havalimani': 'LTCA', 'ilce': 'elazığ'}, 'Uşak': {'havalimani': 'LTBO', 'ilce': 'uşak'}, 'Van': {'havalimani': 'LTCI', 'ilce': 'van'}, 'Yalova': {'havalimani': 'LTFJ', 'ilce': 'istanbul'}, 'Yozgat': {'havalimani': 'LTAZ', 'ilce': 'gülşehir'}, 'Zonguldak': {'havalimani': 'LTAS', 'ilce': 'saltukova'}}

        ilce = sehirler[location]['ilce']
        havalimani = sehirler[location]['havalimani']
        if location not in sehirler:
            return "City not found"
        url = f'https://www.wunderground.com/history/daily/tr/{ilce}/{havalimani}/date/{date}'
        return url

    url = generate_url(date, location)
    def get_datas(url):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        wait = WebDriverWait(driver, 7)

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'mat-cell')))

        data = driver.page_source
        driver.quit()
        return data
    data = get_datas(url)
    def get_hours_data(data):
        soup = BeautifulSoup(data, 'html.parser')
        td_elements = soup.find_all('td', {'class': 'mat-cell cdk-cell cdk-column-dateString mat-column-dateString ng-star-inserted'})
        hours = []
        for td in td_elements:
            span_elements = td.find_all('span', {'class': 'ng-star-inserted'})
            for span in span_elements:
                hours.append(span.text.strip())
        return hours
    weather_hours = get_hours_data(data)
    def get_closest_time_data(date, weather_hours):
        smallest_difference = float('inf')
        closest_time = ''

        date_time_12 = date.strftime('%I:%M %p')

        for time in weather_hours:
            time_12 = datetime.strptime(time, '%I:%M %p').strftime('%I:%M %p')

            difference = abs((datetime.strptime(time_12, '%I:%M %p') - datetime.strptime(date_time_12, '%I:%M %p')).total_seconds())

            if difference < smallest_difference:
                smallest_difference = difference
                closest_time = time
            
        return closest_time
    def getweatherdatafr(date, weather_hours):

        soup = BeautifulSoup(data, 'html.parser')

        # Belirli class'a sahip tr etiketlerini seç
        tr_elements = soup.find_all('tr', {'class': 'mat-row cdk-row ng-star-inserted'})

        closest_time = get_closest_time_data(date, weather_hours)
        #print(f"En yakın saat: {closest_time}")

        found_data = []

        for tr in tr_elements:
            row_content = tr.text

            if closest_time in row_content:
                found_data.append(row_content)
                break

        return found_data

    output_array = getweatherdatafr(date, weather_hours)
    def extract_weather_data(data_array):
        extracted_data = []

        for data in data_array:
            separated_data = data.split()

            # İlk Fahrenheit bilgisini al
            fahrenheit = separated_data[1].replace('\xa0°F', '')

            # Rüzgar hızını al
            wind_speed_full = separated_data[4].replace('\xa0°mph', '')  # Tüm rüzgar hızı verisini al

            # Sadece rakamları almak için bir filtreleme işlemi uygula
            wind_speed = ''.join(filter(str.isdigit, wind_speed_full))

            # Koşulu al (önceki yöntemden farklı olarak)
            condition = ' '.join(separated_data[8:])  # Tüm kalan veriyi birleştiriyoruz

            condition_parts = condition.split('°in', 1)  # Yalnızca ilk '°in' ifadesine göre ayır

            if len(condition_parts) > 1:  # Eğer veri '°in' içeriyorsa
                condition = condition_parts[1]  # İkinci parçayı al

            extracted_data.append([fahrenheit, wind_speed, condition])

            print(f"Fahrenheit: {fahrenheit}, Wind Speed: {wind_speed}, Condition: {condition}")

        return extracted_data
    extracted_info = extract_weather_data(output_array)
    result = [[item for item in sublist if not ('PM' in item or '°in' in item)] for sublist in extracted_info]
    data = extracted_info[0][0][2:], extracted_info[0][1], extracted_info[0][2]
    def fahrenheit_to_celsius(fahrenheit):
        fahrenheit_float = float(fahrenheit)  # Son karakter olan ° işaretini kaldırıp float'a çevir
        celsius = (fahrenheit_float - 32) * 5 / 9
        return str(celsius)  # Sonucu string olarak döndür

    converted_fahrenheit = fahrenheit_to_celsius(data[0])
    updated_data = (converted_fahrenheit,) + data[1:]  # Yeni tuple oluştur, ilk elemanı değiştir
    return updated_data

anan = get_weather_data(Date,location)
print(anan)