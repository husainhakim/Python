#wap that defines a list of countries that are a member of brics and check whether a country is a member of brics or not
Kingcountry=['BRAZIL','RUSSIA','CHINA','SOUTH AFRICA','BHARAT','INDIA']
askcountry=input("Enter the country to check if it is in BRICS or not:-")
if askcountry.upper() in Kingcountry:
     print(askcountry,'is  a part of the BRICS')
else:
    print(askcountry,'is not a part of the BRICS')