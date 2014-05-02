#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()
# DEBUG = True

# import sys
# import logging
import threading
import time
import libardrone.libardrone as ard


class flight_log(threading.Thread):
    def __init__(self, drone):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.org_time = time.time()
        self.fname = "navdata.log"
        self.drone = drone

    def delta_time(self):
        return time.time() - self.org_time

    def record(self):
        r_time = self.delta_time()
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\n"\
            % (str(r_time),
               str(self.navdata[0]["ctrl_state"]),
               str(self.navdata[0]["battery"]),
               str(self.navdata[0]["theta"]),
               str(self.navdata[0]["phi"]),
               str(self.navdata[0]["psi"]),
               str(self.navdata[0]["altitude"]),
               str(self.navdata[0]["vx"]),
               str(self.navdata[0]["vy"]),
               str(self.navdata[0]["vz"]),
               str(self.navdata[0]["num_frames"]))

    def recorder(self):
        f = open(self.fname, "a+")
        f.write(self.record())
        f.close()

    def run(self):
        print "Recorder Started."
        while True:
            # time.sleep(0.01)
            self.recorder()


def main():
    drone = ard.ARDrone(is_ar_drone_2=True)

    # flight logger thread start
    th = flight_log(drone)
    th.setDaemon(True)
    th.start()

    # take off
    print "Takeing off"
    drone.takeoff()

    # maneuvering
    print "Maneuvering"
    for i in range(10):
        for j in range(60):
            drone.turn_left()
            time.sleep(0.005)
        for k in range(60):
            drone.turn_right()
            time.sleep(0.005)

    # landing
    print "Landing"
    drone.land()
    time.sleeop(1)
    print "Halting"
    drone.halt()


if __name__ == "__main__":
    main()
