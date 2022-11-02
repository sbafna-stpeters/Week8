#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 23:16:51 2022

@author: shantanubafna
"""
def prime_or_not(number):
    for i in range(2, int(number**0.5)):
        if number % i == 0:
            return False
    return True
        
def prime_factor_list(num):
    list_prime_factors = []
    for j in range(2, int(num**0.5)):
        if num % j == 0:
            if prime_or_not(j):
                list_prime_factors.append(j)
            if prime_or_not(num/j):
                list_prime_factors.append(num/j)
    largest = int(max(list_prime_factors))
    print("The largest prime factor is", largest)
    
prime_factor_list(600851475143)
    