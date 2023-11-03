import requests
import random
import time
first_sensor_timer=20
second_sensor_timer=30
third_sensor_timer=50
start_counter=int(time.time())
while True:
    iteration_counter=int(time.time())
    if((iteration_counter-start_counter)%first_sensor_timer==0):
        requests.post('http://localhost:5000/addData', json={"value": random.randint(0, 200), "timestamp": time.strftime("%H%M%S", time.localtime()), "device_id": 1})
        print("1")

    if((iteration_counter-start_counter)%second_sensor_timer==0):
        requests.post('http://localhost:5000/addData', json={"value": random.randint(0, 200), "timestamp": time.strftime("%H%M%S", time.localtime()), "device_id": 2})
        print("2")
        
    if((iteration_counter-start_counter)%third_sensor_timer==0):
        requests.post('http://localhost:5000/addData', json={"value": random.randint(0, 200),"timestamp": time.strftime("%H%M%S", time.localtime()), "device_id": 3})
        print("3")
    
    print(iteration_counter)
    print(iteration_counter-start_counter)
    time.sleep(1)
