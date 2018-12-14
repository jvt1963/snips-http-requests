#!/usr/bin/env python2
from hermes_python.hermes import Hermes
import urllib2
from devices import device, deviceOn, deviceOff

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def intent_received(hermes, intent_message):
    sentence = 'You asked me '

    house_room_slot = intent_message.slots.house_room.first()

    for x in device:
      print(x)
      if x == house_room_slot.value:
         nx = device.index(x)
         break

    if intent_message.intent.intent_name == 'jaimevegas:turnOn':
        print('jaimevegas:turnOn')
        sentence += 'to turn on ' + house_room_slot.value
	rq = deviceOn[nx]
    elif intent_message.intent.intent_name == 'jaimevegas:turnOff':
        print('jaimevegas:turnOff')
        sentence += 'to turn off ' + house_room_slot.value
	rq = deviceOff[nx]
    else:
        return

    hermes.publish_end_session(intent_message.session_id, sentence)
    r = urllib2.urlopen(rq)

with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
