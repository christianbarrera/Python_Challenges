from bs4 import BeautifulSoup
import requests
import sched, time
import simpleaudio as sa


# Fake address below
sites = [
"https://www.teststore.com/site/nintendoswitch1",
"https://www.teststore.com/site/nintendoswitch2",
"https://www.teststore.com/site/nintendoswitch3"
]

s = sched.scheduler(time.time, time.sleep)

def search_html(sites):
    '''
    Searches each html for a clause that says 'Sold Out'. If it doesn't exist, that means
    Test Store has switches available for purchase. 

    Args:
        sites: a list of each Switch unique url. 
    Returns:
        None
    '''
    agent = {"User-Agent":"Mozilla/5.0"}

    for site in sites:
        content = requests.get(site, headers=agent).text
        soup = BeautifulSoup(content, 'html.parser')
        
        div = soup.find('div', {'class': 'fulfillment-add-to-cart-button'})
        result = div.find_all('button')[0].text
        print(result)
        print(div)
        if result == 'Sold Out' or result == 'Check Stores':
            continue
        else:
            filename= "/Users/ChristianBarrera/Downloads/Loud_Alarm_Clock_Buzzer-Muk1984-493547174.wav"
            wave_obj = sa.WaveObject.from_wave_file(filename)
            play_obj = wave_obj.play()
            play_obj.wait_done()
            return

    s.enter(60, 1, search_html, (sites,))

s.enter(1, 1, search_html, (sites,))
s.run()