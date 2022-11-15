#!/bin/python3

import mechanicalsoup

def Format(s):
    return s.replace("\n", "").replace("\t", "").title()

def Eurospin(n):
   
    print("\n>------EUROSPIN------<\n")

    b = mechanicalsoup.StatefulBrowser()
    # Link to discount page
    b.open("https://www.eurospin.it/promozioni/")
    
    # Parsing html
    data_sconto = Format(b.page.find(class_="row sn_promo_grid_info_filters").find("h2").text)
    items = b.page.find_all(class_="i_title")
    prices = b.page.find_all(class_="i_price")

    print(data_sconto, "\n")

    # Check if the number of items to print is valid
    if (n == 0 or n > len(items)):
        n = len(items)
 

    for i in range(n):
        # Formatting the strings
        price = Format(prices[i].text)[5:9]
        items[i] = Format(items[i].text)
        # Huge fourmula...
        try:
            discount = 100 - (100 * float(price.replace(",", ".")) / float(Format(prices[i].text)[0:5].replace(",", ".")) // 1)
        except:
            continue
        print(items[i] + " ----> " + price + " -" + str(discount) + "%")
    

def Lidl(n):
    
    print("\n>--------LIDL--------<\n")

    b = mechanicalsoup.StatefulBrowser()
    # Link to discounts page
    b.open("https://www.lidl.it/c/offerte-settimanali/c10/w1")
    
    # Parsing html
    data_sconto = Format(b.page.find(class_="lidl-m-ribbon-item__text").text)
    items = b.page.find_all(class_="ret-o-card__headline")
    prices = b.page.find_all(class_="lidl-m-pricebox__price")
    discount = b.page.find_all(class_="lidl-m-pricebox__highlight")
    
    print("Sconti validi tra i giorni: ", data_sconto, "\n")

    # Check if the number of items to print is valid
    if (n == 0 or n > len(items)):
        n = len(items)
    
    for i in range(n):
        items[i] = Format(items[i].text).replace("  ", "")
        prices[i] = Format(prices[i].text)
        discount[i] = Format(discount[i].text)
        if "Approfittane Ora!" in discount[i]:
            discount[i] = ""
        print(items[i] + " ----> " + prices[i] + " " + discount[i])

    print("\n")

def main():
    
    print("Benvenuto nel risparmio!")
    n = int(input("Quanti prodotti vuoi vedere? (0 = all) "))

    Eurospin(n)
    Lidl(n)


if __name__ == "__main__":
    main()
