from bs4 import BeautifulSoup
import requests

base_url = "https://www.transfermarkt.com"
super_lig_url = "https://www.transfermarkt.com/super-lig/daten/wettbewerb/TR1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

page = requests.get(super_lig_url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Takım bağlantılarını içeren td etiketlerini seçelim
team_cells = soup.find_all("td", class_="zentriert no-border-rechts")

# Her td elemanının içindeki a etiketlerinden bağlantıları alalım
for cell in team_cells:
    team_link = cell.find("a")
    if team_link:
        href = team_link.get("href")
        team_name = team_link.get("title")
        
        # Takım sayfasına istek gönderelim
        team_page = requests.get(base_url + href, headers=headers)
        team_soup = BeautifulSoup(team_page.content, 'html.parser')
        
        # Takım değeri
        team_value = team_soup.find("div", class_="data-header__box--small").text.strip()
        
        # Yaş ortalaması, milli takımdaki oyuncu sayısı, stadyum ve kadro boyutu
        labels = team_soup.find_all(class_="data-header__label")
        for label in labels:
            label_name = label.text.strip()
            if label_name.startswith("Average age"):
                average_age = label.find_next(class_="data-header__content").text.strip()
            elif label_name.startswith("National team players"):
                national_players = label.find_next(class_="data-header__content").text.strip().split()[0]
            elif label_name.startswith("Stadium"):
                stadium_info = label.find_next(class_="data-header__content").text.strip()
                stadium_seat = ''
                if 'seat' in stadium_info.lower():
                    seat_index = stadium_info.lower().find('seat')
                    stadium_seat = stadium_info[:seat_index].strip().split()[-1]

            elif label_name.startswith("Squad size"):
                squad_size = label.find_next(class_="data-header__content").text.strip()

        print("Takım Adı:", team_name)
        print("Takım Değeri:", team_value.split(' ')[0])
        print("Yaş Ortalaması:", average_age)
        print("Milli Takımdaki Oyuncu Sayısı:", national_players)
        print("Stadyum Koltuk Sayısı:", stadium_seat)
        print("Kadro Boyutu:", squad_size)
        print("----------------------------------------")
