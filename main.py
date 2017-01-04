#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# FROM ZERO TO PYTHON HERO series
# Script No#2: Bernoulli's and one-dimensional continuity equations for fluent flow excluding height of flow channel
# File created: 03.01.17
# File modified: 00.00.00
# Version: P.2.001-0 [P:Prototype, F:Final]

#   input method: [velocity_1, pressure_1, velocity_2, pressure_2, density]
#   one of them must be replaced by question mark, e.g: [velocity_1, ?, velocity_2, pressure_2, density]
#   all: velocity, pressure (gauge pressure!) and density values given adequately in: [m/s], [Pa], [kg/m^3]


import math

QM = chr(63) #ASCII question mark
VELOCITY = '[m/s]'
PRESSURE = '[Pa]'
DENSITY = '[kg/m^3]'
REFERENCE_PRESSURE = 101325

data = [10, 300, QM, 100, 1.113]

def check_marked_pos(param_list):
    check = [False, 0]
    if len(param_list) == 5 and QM in data:
        check = [True, data.index(QM)]
    return check

def calculate_parameter(searched):
    if searched == 0:
        res = math.sqrt(abs(data[2]**2+(data[3]-data[1])*2/data[4]))
        res = str(round(res, 2)) + VELOCITY
    elif searched == 1:
        res1 = data[4]/2*(data[2]**2-data[0]**2)+data[3]
        res2 = res1 + REFERENCE_PRESSURE
        res = str(round(res1, 2)) + PRESSURE + ' => ' + str(round(res2, 2)) + PRESSURE + ' of absolute pressure'
    elif searched == 2:
        res = math.sqrt(abs(data[0]**2+(data[1]-data[3])*2/data[4]))
        res = str(round(res, 2)) + VELOCITY
    elif searched == 3:
        res1 = data[4]/2*(data[0]**2-data[2]**2)+data[1]
        res2 = res1 + REFERENCE_PRESSURE
        res = str(round(res1, 2)) + PRESSURE + ' => ' + str(round(res2, 2)) + PRESSURE + ' of absolute pressure'
    elif searched == 4:
        res = 2*(data[3]-data[1])/(data[0]**2-data[2]**2)
        res = str(round(res, 2)) + DENSITY
    return res

def main(values):
    mark_pos = check_marked_pos(values)
    if mark_pos[0]:
        result = calculate_parameter(mark_pos[1])
        print (' Parameters of #1 channel:')
        print ('Flow speed: {0} {1}'.format(data[0], VELOCITY))
        print ('Flow pressure: {0} {1} (gauge pressure)'.format(data[1], PRESSURE))
        print (' Parameters of #2 channel:')
        print ('Flow speed: {0} {1}'.format(data[2], VELOCITY))
        print ('Flow pressure: {0} {1} (gauge pressure)'.format(data[3], PRESSURE))
        print (' Other parameters:')
        print ('Fluent density: {0} {1}'.format(data[4], DENSITY))
        print ('Reference pressure: {0} {1}'.format(REFERENCE_PRESSURE, PRESSURE))
        print ('#RESULT:')
        print ('# = {}'.format(result))
    else:
        print ('Wrong amount of parameters or no question mark!')

main(data)
