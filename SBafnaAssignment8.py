#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 22:29:14 2022

@author: shantanubafna
"""
class University:
    def __init__(self, university_name:str,location:str,undergraduate_students:int,graduate_students:int):
        self.university_name = university_name
        self.location = location
        self.undergraduate_students = undergraduate_students
        self.graduate_students = graduate_students
        
    def print_university_size(self):
        sum =  self.graduate_students + self.undergraduate_students
        print('Total number of undergraduate and graduate students', sum)
        
    def is_undergraduate_greater(self):
        if self.undergraduate_students > self.graduate_students :
            print("There are more undergraduate students than graduate students")
        elif self.undergraduate_students <= self.graduate_students :
            print("There are more graduate students than undergraduate students")
    
SPU = University(university_name = "Saint Peters University",
                 location = "Jersey City",
                 undergraduate_students = 3000,
                 graduate_students = 5000)

SPU.print_university_size()
SPU.is_undergraduate_greater()

#Bonus Question
class College(University):
    def print_college(self):
        print("Printing \"College class\" university name:" , self.university_name)
        
C = College("Northeastern University", "Boston", 4000,5000)
C.print_college()