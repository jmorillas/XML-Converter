import pandas as pd
from xml.dom import minidom
import xml.etree.ElementTree as ET
# import os

df = pd.read_csv('Pythagoras_Cashin_and_out_Nov_2023.csv', sep=',')
df = df.dropna()
df = df.reset_index()  # make sure indexes pair with number of rows
df.insert(2, "PartnerType", '')	
df.insert(2, "Country", '')	
df.insert(2, "PartnerbType", 59)		
df.insert(2, "CountryValuesrc", 0)
df.insert(2, "CountryValuedst", 0)


df.loc[(df["OriginalAmount"] >= 0), "PartnerbType"] = 50



print(df)				

#root element
root = ET.Element('TRANSACTIONS')
for index, row in df.iterrows():
    # print(row['BookingDate'], row['PythagorasPID'])
    TransactionID = str(row['TransactionID'])
    TransactionType = str(row['TransactionType'])
    BookingDate = str(row['BookingDate'])
    
    PythagorasPID = str(row['PythagorasPID'])
    BookingID = str(row['BookingID'])
    AccountID = str(row['AccountID'])
    ValueDate = str(row['ValueDate'])
    OriginalAmount = str(row['OriginalAmount'])
    Currency = str(row['Currency']) 
    Country = str(row['CountryTag'])
    PartnerID = str(row['PartnerID'])
    Name = str(row['Name'])
    

    PartnerbType = str(row['PartnerbType'])

    #book sub-element
    transaction = ET.SubElement(root, 'TRANSACTION')
    
    transactionid = ET.SubElement(transaction, 'TRANSACTIONID')
    transactionid.text = TransactionID

    transactiontype = ET.SubElement(transaction, 'TRANSACTIONTYPE')
    transactiontype.text = TransactionType


    bookingdate = ET.SubElement(transaction, 'BOOKINGDATE')
    bookingdate.text = BookingDate
    
    partners = ET.SubElement(transaction, 'PARTNERS')

    partner = ET.SubElement(partners, 'PARTNER')
    
    pythagorasPID = ET.SubElement(partner, 'PYTHAGORASPID')
    pythagorasPID.text = PythagorasPID
    
    country = ET.SubElement(partner, 'COUNTRY')
    country.text = ' '

    partnertype = ET.SubElement(partner, 'PARTNERTYPE')
    partnertype.text = '77'
    
    partner_bookings = ET.SubElement(partner, 'BOOKINGS')

    partner_booking = ET.SubElement(partner_bookings, 'BOOKING')

    partner_bookingID = ET.SubElement(partner_booking, 'BOOKINGID')
    partner_bookingID.text = BookingID
    
    partner_accountID = ET.SubElement(partner_booking, 'ACCOUNTID')
    partner_accountID.text = AccountID
    
    partner_originalamount = ET.SubElement(partner_booking, 'ORIGINALAMOUNT')
    partner_originalamount.text = OriginalAmount
    
    partner_currency = ET.SubElement(partner_booking, 'CURRENCY')
    partner_currency.text = Currency
    
    partner_valuedate = ET.SubElement(partner_booking, 'VALUEDATE')
    partner_valuedate.text = ValueDate


    partnerb = ET.SubElement(partners, 'PARTNER')
    
    partnerID = ET.SubElement(partnerb, 'partnerID')
    partnerID.text = PartnerID

    partnerbtype = ET.SubElement(partnerb, 'PARTNERTYPE')
    partnerbtype.text = PartnerbType

    name = ET.SubElement(partnerb, 'NAME')
    name.text = Name

    countryb = ET.SubElement(partnerb, 'COUNTRY')
    countryb.text = Country


# print("DONE")


# print(ET.dump(root))

xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
with open("Cash_in_out_pythagoras_Nov_bcm.xml", "w") as f:
    f.write(xmlstr)

