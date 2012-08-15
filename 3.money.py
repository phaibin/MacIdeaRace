#!/usr/bin/env python
# -*- coding:utf-8 -*-

def get_best_money_list(money_count, money_kind_count):
    """
    for max money_count, max money_kind_count kinds of money, return max continus money count
    money_count:3, money_kind_count:4
    return:
    {23: (1, 4, 7, 8)}
    """
    all_money_list = [(1,)+m for m in all_diff_num_groups(money_kind_count-1, [n+2 for n in range(50)])]
    max_money = 0
    best_money_list = []
    for money_list in all_money_list:
        sum_money_groups = sum_groups(money_count, money_list)
        allkeys = sum_money_groups.keys()
        allkeys.sort()
        temp = 1
        for i in range(len(allkeys)):
            if (i+1)<len(allkeys) and allkeys[i+1]==(allkeys[i]+1):
                temp = allkeys[i]
            else:
                break;
        if temp>max_money:
            max_money = temp
            best_money_list = money_list
    return {max_money:best_money_list}
    
def sum_groups(group_count, num_list):
    """
    group_count:3, num_list:[1,2,3]
    return:
    {1: [(1,)], 2: [(2,), (1, 1)], 3: [(3,), (1, 2), (1, 1, 1)], 4: [(1, 3), (2, 2), (1, 1, 2)], 5: [(2, 3), (1, 2, 2), (1, 1, 3)], 6: [(3, 3), (2, 2, 2), (1, 2, 3)], 7: [(2, 2, 3), (1, 3, 3)], 8: [(2, 3, 3)], 9: [(3, 3, 3)]}
    """
    all_groups = []
    result = {}
    for m in range(group_count):
        all_groups.extend(all_num_groups(m+1, num_list))
    for m in all_groups:
        result.setdefault(sum(m), []).append(m)
    return result
    
def all_num_groups(group_count, num_list):
    """
    group_count:3, num_list:[1,2,3]
    return:
    [(3, 3, 3), (2, 2, 2), (1, 2, 2), (2, 3, 3), (1, 2, 3), (1, 1, 3), (2, 2, 3), (1, 1, 2), (1, 1, 1), (1, 3, 3)]
    """
    if group_count==1:
        return set([(m,) for m in num_list])
    elif group_count==2:
        return set([tuple(sorted((m,n))) for m in num_list for n in num_list])
    else:
        return set([tuple(sorted(m+(n,))) for m in all_num_groups(group_count-1, num_list) for n in num_list])
        
def all_diff_num_groups(group_count, num_list):
    """
    group_count:3, num_list:[1,2,3,4]
    return:
    [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
    """
    return set([m for m in all_num_groups(group_count, num_list) if len(set(m))==len(m)])
    
def main():
    money_count = int(raw_input("请输入纸币的数量： "))
    money_kind_count = int(raw_input("请输入纸币的面额数： "))
    plan = get_best_money_list(3, 4)
    print "最大连续纸币数为：%d，最佳纸币面额为：%s" %(plan.items()[0][0], plan.items()[0][1])

    # sum_money_groups = sum_groups(3, (1, 2, 3))
    # print sum_money_groups    
    # 
    # sum_money_groups = sum_groups(3, (1, 4, 7, 8))
    # print sum_money_groups
    # print
    # sum_money_groups = sum_groups(3, (1, 3, 6, 10))
    # print sum_money_groups
    
if __name__ == '__main__':
    main()
