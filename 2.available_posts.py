#!/usr/bin/env python
# -*- coding:utf-8 -*-

def get_available_posts(posts):
    """docstring for available_posts"""
    result = posts[::]
    for post in posts:
        for r in result:
            if post[0]<r[0] and post[1]<r[1]:
                result.remove(post)
                break
    return result
    
def main():
    raw_input('请输入所有post数量: ')
    input = ""
    while 1:
        temp = raw_input("请输入每个post的技术分和语言分，比如4 1（直接回车结束）: ")
        if temp == '':
            break
        else:
            input += temp + "\n"
    input = input.split("\n")
    input.pop()
    posts = [[int(m) for m in x.split(' ')] for x in input]
    # posts = [(4,1), (4,2), (4,3), (3,3), (2,2)]
    available_posts = get_available_posts(posts)
    print "可以容纳%d贴" %(len(available_posts))
    
if __name__ == '__main__':
    main()