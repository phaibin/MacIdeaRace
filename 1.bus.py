#!/usr/bin/env python
# -*- coding:utf-8 -*-

def path_list(begin, end, bus_list):
    """docstring for path_list"""
    result = []
    if begin==end:
        return result;
    for bus in bus_list:
        if begin in bus:
            last_buses = bus_list[::]
            last_buses.remove(bus)
            last_stops = bus[bus.index(begin)+1::]
            for next_stop in last_stops:
                if next_stop==end:
                    result.append([bus[bus.index(begin):bus.index(next_stop)+1:]])
                else:
                    next_plans = path_list(next_stop, end, last_buses)
                    if next_plans!=[]:
                        for plan in next_plans:
                            plan.insert(0,bus[bus.index(begin):bus.index(next_stop)+1:])
                            result.append(plan)
    return result
    
def transfer_count(begin, end, bus_list):
    """docstring for transfer_count"""
    plans = path_list(begin, end, bus_list)
    if len(plans)==0:
        return -1
    else:
        bus_count = len(plans[0])
        for plan in plans:
            if len(plan)< bus_count:
                bus_count = len(plan)
        return bus_count-1
    
def main():
    raw_input('请输入公交数和站点数: ')
    input = ""
    while 1:
        temp = raw_input("请输入每条公交的站点，比如6 7（直接回车结束）: ")
        if temp == '':
            break
        else:
            input += temp + "\n"
    input = input.split("\n")
    input.pop()
    bus_list = [[int(m) for m in x.split(' ')] for x in input]
    
    begin = int(raw_input('请输入起点站: '))
    end = int(raw_input('请输入终点站: '))
    # bus_list = [[6,7], [4,7,3,6], [2,1,3,5]]
    plan = path_list(begin, end, bus_list)
    print "换乘次数：%d" %(transfer_count(begin, end, bus_list))
    
if __name__ == '__main__':
    main()