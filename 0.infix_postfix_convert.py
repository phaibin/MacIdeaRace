#!/usr/bin/env python
# -*- coding:utf-8 -*-

def infix_to_postfix(input):
    """docstring for infix_to_postfix"""
    output = []
    ops = {'+':1, '-':1, '*':2, '/':2, '^':3, '%':3, '(':0, '@':0}
    opsarr = ['@']
    for c in input:
        # print c
        if c=='(':
            opsarr.append(c)
        elif c==')':
            while opsarr[-1]!='(':
                output.append(opsarr.pop())
            opsarr.pop()
        elif c=='+' or c=='-' or c=='*' or c=='/' or c=='^' or c=='%':
            while ops[opsarr[-1]] >= ops[c]:
                output.append(opsarr.pop())
            opsarr.append(c)
        else:
            output.append(c)

    output.extend(reversed(opsarr))
    output.pop()

    return ''.join(output)

def postfix_to_infix(input):
    """docstring for postfix_to_infix"""
    PREC = {'+':0, '-':0, '*':1, '/':1, '%':1, '^':2}
    stack = []
    for x in input:
        if x in ['+', '-', '*', '/', '^']:
            op2 = stack.pop()
            op1 = stack.pop()
            if len(op2)>1 and ((PREC[op2[1]] < PREC[x]) or (PREC[op2[1]] == PREC[x] and op2[1] != x)):
                op2 = "(%s)" % op2[0]
            else:
                op2 = op2[0]

            if len(op1)>1 and PREC[op1[1]] < PREC[x]:
                op1 = "(%s)" % op1[0]
            else:
                op1 = op1[0]

            stack.append(["%s%s%s" % (op1, x, op2), x])
        else:
            stack.append([x])
    return stack.pop()[0]
    
def main():
    # input = '((a+b)*f)-(i/j)'
    input = raw_input('请输入一个表达式: ').strip()
    a = infix_to_postfix(input)
    b = postfix_to_infix(a)
    print '优化后的表达式是: ' + b
    
if __name__ == '__main__':
    main()