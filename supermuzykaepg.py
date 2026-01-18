from datetime import datetime, timedelta

TZ = " +0100"

def fmt(dt):
    # zamiana datetime -> 'YYYYMMDDHHMMSS +0000'
    return dt.strftime("%Y%m%d%H%M%S") + TZ

# Dzisiaj (data)
today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
# Jutro (potrzebne do nocy)
tomorrow = today + timedelta(days=1)

# Godziny ramówki
t0600 = today.replace(hour=6)
t1000 = today.replace(hour=10)
t1200 = today.replace(hour=12)
t1600 = today.replace(hour=16)
t1700 = today.replace(hour=17)
t1800 = today.replace(hour=18)
t2300 = today.replace(hour=23)
t_next_0400 = tomorrow.replace(hour=4)
t_next_0500 = tomorrow.replace(hour=5)
t_next_0600 = tomorrow.replace(hour=6)

xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<tv>
  <channel id="super_muzyka">
    <display-name>Super Muzyka</display-name>
    <icon src="https://static.wixstatic.com/media/f287cb_9ea90c5c4b554da2b0a334dc707559b3~mv2.png"/>
  </channel>

  <programme start="{fmt(t0600)}" stop="{fmt(t1000)}" channel="super_muzyka">
    <title>Poranek z muzyką</title>
    <desc>Halo halo, pobudka wstajemy i gramy dla was!</desc>
    <category lang="pl">Program muzyczny</category>
    <icon src="https://static.wixstatic.com/media/f287cb_8212a8c5f96e4052a62e6cc88e174d7b~mv2.png"/>
  </programme>

  <programme start="{fmt(t1000)}" stop="{fmt(t1200)}" channel="super_muzyka">
    <title>Przed 12</title>
    <desc>Jeszcze niewybudzeni? Gramy dla was jeszcze przed 12:00</desc>
    <category lang="pl">Program muzyczny</category>
    <icon src="https://static.wixstatic.com/media/f287cb_8212a8c5f96e4052a62e6cc88e174d7b~mv2.png"/>
  </programme>

  <programme start="{fmt(t1200)}" stop="{fmt(t1600)}" channel="super_muzyka">
    <title>W ciągu dnia</title>
    <desc>Najlepsza muzyka w ciągu dnia!</desc>
    <category lang="pl">Program muzyczny</category>
    <icon src="https://static.wixstatic.com/media/f287cb_27d58d1fa3ac465eb588398e9d7b2330~mv2.png"/>
  </programme>

  <programme start="{fmt(t1600)}" stop="{fmt(t1700)}" channel="super_muzyka">
    <title>Piosenki w Programie 1</title>
    <desc>Piosenki w Programie 1 to program autorski Super Grupy, tam gdzie posłuchasz najlepsze piosenki z lat 80, 90 i 2000 w T1</desc>
    <category lang="pl">Program muzyczny</category>
    <icon src="https://static.wixstatic.com/media/f287cb_94ca5a2f37534268b762160f91a9e6d5~mv2.png"/>
  </programme>

  <programme start="{fmt(t1700)}" stop="{fmt(t1800)}" channel="super_muzyka">
    <title>Piosenki w Programie 1</title>
    <desc>Piosenki w Programie 1 to program autorski Super Grupy, tam gdzie posłuchasz najlepsze piosenki z lat 80, 90 i 2000 w T1</desc>
    <category lang="pl">Program muzyczny</category>
    <icon src="https://static.wixstatic.com/media/f287cb_94ca5a2f37534268b762160f91a9e6d5~mv2.png"/>
  </programme>

  <programme start="{fmt(t1800)}" stop="{fmt(t2300)}" channel="super_muzyka">
    <title>M jak muzyka</title>
    <desc>Żyjecie? gramy jeszcze najlepsze klasyki wieczorem!</desc>
    <category lang="pl">Program muzyczny</category>
    <icon src="https://static.wixstatic.com/media/f287cb_3d2c435f332446eda5f41e0daecb67a7~mv2.png"/>
  </programme>

  <programme start="{fmt(t2300)}" stop="{fmt(t_next_0400)}" channel="super_muzyka">
    <title>Nocna zmiana</title>
    <desc>Grzeczna muzyka? O tej porze możesz zapomnieć! Bez cenzury i dobrej zabawy!</desc>
    <category lang="pl">Program muzyczny</category>
    <icon src="https://static.wixstatic.com/media/f287cb_658db068e9134a1a8afb591fab43760c~mv2.png"/>
  </programme>

  <programme start="{fmt(t_next_0400)}" stop="{fmt(t_next_0500)}" channel="super_muzyka">
    <title>Piosenki w Programie 1</title>
    <desc>Piosenki w Programie 1 to program autorski Super Grupy, tam gdzie posłuchasz najlepsze piosenki z lat 80, 90 i 2000 w T1</desc>
    <category lang="pl">Program muzyczny</category>
    <icon src="https://static.wixstatic.com/media/f287cb_94ca5a2f37534268b762160f91a9e6d5~mv2.png"/>
  </programme>

  <programme start="{fmt(t_next_0500)}" stop="{fmt(t_next_0600)}" channel="super_muzyka">
    <title>Piosenki w Programie 1</title>
    <desc>Piosenki w Programie 1 to program autorski Super Grupy, tam gdzie posłuchasz najlepsze piosenki z lat 80, 90 i 2000 w T1</desc>
    <category lang="pl">Program muzyczny</category>
    <icon src="https://static.wixstatic.com/media/f287cb_94ca5a2f37534268b762160f91a9e6d5~mv2.png"/>
  </programme>

</tv>
'''

with open("supergrupamuzyczna.xml", "w", encoding="utf-8") as f:
    f.write(xml)


