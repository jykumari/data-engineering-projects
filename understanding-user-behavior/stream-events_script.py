#!/usr/bin/env python

import os
import random
import time

min_user = 1
max_user = 5

events = ["level_up", "add_coins", "destroy_base"]

while True:
    curr_user = "\"Host: user" + str(random.randint(min_user, max_user)) + ".gameshop.com\""
    curr_event = events[random.randint(0, len(events) - 1)]
    command = "docker-compose exec mids ab -n 10 -H " + curr_user + " http://localhost:5000/" + curr_event 
    #print(f"Sending event print: {curr_event} to Host: {curr_user}")
    os.system(command)
    time.sleep(10)

