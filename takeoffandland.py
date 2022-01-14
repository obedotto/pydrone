from udacidrone import Drone
from udacidrone.connection import MavlinkConnection
import time

conn = MavlinkConnection('tcp:127.0.0.1:5760', threaded=True)
drone = Drone(conn)
drone.start()
time.sleep(5)

drone.take_control()
drone.arm()
drone.takeoff(3)

time.sleep(10)

drone.land()
drone.disarm()
drone.release_control()
drone.stop()