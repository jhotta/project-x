#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()
DEBUG = True
RECORD = True

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
        try:
            navdata = self.drone.get_navdata()
            return "%s, %s, %s, %s, %s, %s, %s, %s\n"\
                % (str(self.delta_time()),
                   str(navdata[0]["theta"]),
                   str(navdata[0]["phi"]),
                   str(navdata[0]["psi"]),
                   str(navdata[0]["altitude"]),
                   str(navdata[0]["vx"]),
                   str(navdata[0]["vy"]),
                   str(navdata[0]["vz"]))
        except:
            pass

    def recorder(self):
        f = open(self.fname, "a+")
        f.write(self.record())
        f.close()

    def run(self):
        if DEBUG:
            print "Recorder Started."
        while True:
            # time.sleep(0.01)
            self.recorder()


def main():
    drone = ard.ARDrone(is_ar_drone_2=True)

    if RECORD:
        # flight recorder thread start
        th = flight_log(drone)
        th.setDaemon(True)
        th.start()
        time.sleep(0.01)

    # take off
    if DEBUG:
        print "Takeing off"
    drone.takeoff()

    # maneuvering
    drone.set_speed(0.1)
    if DEBUG:
        print "setting speed"
    try:
        drone.at_config("control:altitude_max", 500)
        print "setting altitude_max."
    except:
        pass

    if DEBUG:
        print "Maneuvering"
    for i in range(10):
        for j in range(60):
            drone.turn_left()
            try:
                m_navdata = drone.get_navdata()
                if DEBUG:
                    print "altitude: %s" % m_navdata[0]["altitude"]
                    print "psi: %s" % m_navdata[0]["psi"]
            except:
                pass
            time.sleep(0.005)
        for k in range(60):
            drone.turn_right()
            try:
                m_navdata = drone.get_navdata()
                if DEBUG:
                    print "altitude: %s" % m_navdata[0]["altitude"]
                    print "psi: %s" % m_navdata[0]["psi"]
            except:
                pass
            time.sleep(0.005)

    # landing
    if DEBUG:
        print "Landing"
    drone.land()

    # halting
    time.sleep(0.5)
    if DEBUG:
        print "Halting"
    drone.halt()


if __name__ == "__main__":
    main()
