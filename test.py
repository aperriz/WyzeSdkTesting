import threading
import time
from wyze_sdk import Client
from wyze_sdk.api.devices.bulbs import MeshBulb

def brighten_light(bulb):
    if(isinstance(bulb, MeshBulb)):
        print(bulb.nickname);
        #client.bulbs.turn_on(device_mac=bulb.mac, device_model=bulb.product.model);
        time.sleep(25);
        client.bulbs.set_brightness(device_mac=bulb.mac, device_model=device.product.model, brightness=10);
        print("threaded " + bulb.nickname + "\n");
        time.sleep(5);
        client.bulbs.set_brightness(device_mac=bulb.mac, device_model=device.product.model, brightness=1);
        #client.bulbs.turn_off(device_mac=bulb.mac, device_model=bulb.product.model);

client = Client(email="daniel.sara.noah@gmail.com", password="DSAMbmo2021!", key_id="a2f5340c-e711-41cc-923f-dafcf7349818", 
                api_key="fhRTRpvg5mf314sCsSiPU5QxhCbPXzfXi31tviyptzLEgRrEslxZU1VazPjM");
print(client.devices_list)
bulbs = list();
devices = client.devices_list();

threads = list();

for device in devices:
    #print(device.nickname + "\n");
    if "Living Room Lamp" in device.nickname:
        #print(device.nickname);
        bulbs.append(device);
        #print(client.bulbs.info(device_mac=device.mac))

for bulb in bulbs:
    assert isinstance(bulb,MeshBulb);
    #bulb.brightness = 1;
    newt = threading.Thread(target=brighten_light, args=[bulb]);
    threads.append(newt);
for t in threads:
    assert isinstance(t, threading.Thread);
    t.start();