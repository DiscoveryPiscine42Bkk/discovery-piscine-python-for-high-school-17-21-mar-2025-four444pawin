#!/usr/bin/env python3
mult = 0
while mult <=10 :
    print(f"Table de {mult}:", end = "" )
            
    current_num = 0
    while current_num <= 10:
        print(current_num * mult , end = " ")
        current_num += 1
    
    print()
    mult += 1
