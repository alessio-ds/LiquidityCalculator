# -*- coding: utf-8 -*-
"""
Created on Mon May  3 18:43:36 2021

@author: alessiosca
"""

import requests


print("\nLiquidity Calculator (Binance Liquid Swap, PancakeSwap etc)\n")
print("### USE THE DOT FOR DECIMAL NUMBERS  ###")

request=input('Have you got liquidity into BNB/BUSD? y/N: ')

if request=='y' or request=='Y':
    page=requests.get("https://coinmarketcap.com/currencies/binance-coin/")
    pagetext=page.text
    pos=pagetext.find('<div class="priceValue___11gHJ">')
    price=float(pagetext[pos+33:pos+39])
    
    crypto=float(input("Input the initial quantity of BNB: "))
    stable=float(input("Input the initial quantity of BUSD: "))
    cryptofinal=(crypto/price)*stable
    print('\n')
    
    print("You've got exactly :\n",cryptofinal," BNB\n", price, " BUSD")
    input('')
    
    
else:
    crypto=float(input("Input the initial quantity of the FIRST crypto: "))
    stable=float(input("Input the initial quantity of the SECOND crypto: "))
    actualprice=float(input("Input the actual price of the FIRST crypto (in swap with the SECOND): "))
    cryptofinal=(crypto/actualprice)*stable
    print('\n')
    print("You've got exactly':\n",cryptofinal," (1)\n", actualprice, " (2)")
    input('')
