text = """👍👍👍
BANK NIFTY
45000 PE
ABOVE 330
VIEW / EDUCATIONAL PURPOSE
"""


# SLICE PRICE FROM TEXT
price = ""
aboveText = text.find("ABOVE")
for i in range(aboveText+3, aboveText + 12):
    if text[i].isdigit():
        price = price + text[i]



# SLICE POSITION SIDE FROM TEXT
positionSide = ""
findNifty = text.find("NIFTY")
for i in range(findNifty + 10, findNifty + 17):
    if(text[i] == "P"):
        positionSide = "PE"
    if(text[i] == "C"):
        positionSide = "CE"



# SLICE STRIKE PRICE FROM TEXT
strike_price = ""
for i in range(findNifty+ 4, findNifty + 15):
    if text[i].isdigit():
        strike_price = strike_price + text[i]


print(strike_price)


"""
# FIRST ORDER INFORMATION:  {


 'order_name': 'FIRST ORDER', 
 'symbol': 'BANKNIFTY21FEB24C45000', 
 'token': '45811', 
 'buying_price': 301.5, 
 'is_order_executed': False, 
 'order_no': '24021501286644', 
 'target_price': 340.5, 
 'stoploss_price': 260.0, 
 'is_order_cancelled': False, 
 'is_position_squareOff': False, 
 'is_exit_order_placed': False, 
 'exit_order_no': '', 
 'angel_symbol': 'BANKNIFTY21FEB2445000CE'
 
 }

# SECOND ORDER INFORMATION:  {'order_name': 'SECOND ORDER', 'symbol': 'BANKNIFTY21FEB24C45000', 'token': '45811', 'buying_price': 301.5, 'is_order_executed': False, 'order_no': '24021501286645', 'target_price': 340.5, 'stoploss_price': 260.0, 'is_order_cancelled': False, 'is_position_squareOff': False, 'is_exit_order_placed': False, 'exit_order_no': '', 'angel_symbol': ''}








 VIEW/ EDUCATIONAL PURPOSE
300   45000    CE
FIRST ORDER INFORMATION:  {'order_name': 'FIRST ORDER', 'symbol': 'BANKNIFTY21FEB24C45000', 'token': '45811', 
'buying_price': 301.5, 'is_order_executed': False, 'order_no': '24021501286677', 'target_price': 340.5, 'stoploss_price': 260.0, 'is_order_cancelled': False, 
'is_position_squareOff': False, 'is_exit_order_placed': False, 'exit_order_no': '', 'angel_symbol': 'BANKNIFTY21FEB2445000CE'}
THREAD 1 STATE  True
https://api.shoonya.com/NorenWClientTP//SingleOrdHist
BOOK PROFIT, currnet price is:  1445.0    FIRST ORDER
https://api.shoonya.com/NorenWClientTP//ModifyOrder
ORDER MODIFIED TIME:  1
THREAD 1 STATE  True
ORDER MODIFIED TIME:  1




THREAD 1 STATE  True
https://api.shoonya.com/NorenWClientTP//SingleOrdHist
----- AFTER PLACING STOPLOSS ORDER -------- {'order_name': 'FIRST ORDER', 'symbol': 'BANKNIFTY21FEB24C45000', 'token': '45811', 'buying_price': 301.5, 'is_order_executed': True, 'order_no': '24021501286714', 'target_price': 340.5, 'stoploss_price': 260.0, 'is_order_cancelled': False, 'is_position_squareOff': False, 'is_exit_order_placed': True, 'exit_order_no': '24021501286715', 'angel_symbol': 'BANKNIFTY21FEB2445000CE'}
SECOND ORDER INFORMATION:  {'order_name': 'SECOND ORDER', 'symbol': 'BANKNIFTY21FEB24C45000', 'token': '45811', 'buying_price': 301.5, 'is_order_executed': False, 'order_no': '24021501286716', 'target_price': 340.5, 'stoploss_price': 260.0, 'is_order_cancelled': False, 'is_position_squareOff': False, 'is_exit_order_placed': False, 'exit_order_no': '', 'angel_symbol': ''}
BOOK PROFIT, currnet price is:  1445.0    FIRST ORDER
https://api.shoonya.com/NorenWClientTP//ModifyOrder







----- AFTER PLACING STOPLOSS ORDER -------- {'order_name': 'FIRST ORDER', 
'symbol': 'BANKNIFTY21FEB24C45000', 
'token': '45811',
 'buying_price': 301.5, 
 'is_order_executed': True, 
 'order_no': '24021501286723', 
 'target_price': 340.5, 
 'stoploss_price': 260.0, 
 'is_order_cancelled': False, 
 'is_position_squareOff': False, 
 'is_exit_order_placed': True,
 'exit_order_no': '24021501286724', 
 'angel_symbol': 'BANKNIFTY21FEB2445000CE'}
BOOK PROFIT, currnet price is:  1445.0    FIRST ORDER
https://api.shoonya.com/NorenWClientTP//ModifyOrder
ORDER MODIFIED TIME:  1
THREAD 1 STATE  True
ORDER MODIFIED TIME:  1




    # ANGEL SYMBOL HANDLE-----------------------------------------------
    #expiry_date = next_wednesday()
    # day = expiry_date['day']
    # month = expiry_date['month']
    # angel_symbol = "BANKNIFTY" + day + month + "23" + strike + side
    
    # -----------------------------------------------------------------







---------------------------------------------------------------------------------------------------------------------------------------------


hkQ0k2TVRjd09ESTFPVFEwT0N3aWFuUnBJam9pTUROaU5ESmhZell0WWpSak1pMDBZVE5oTFdJelpqa3RNRE5oWkRreU5qUXlZalZpSWl3aWIyMXVaVzFoYm1GblpYSnBaQ0k2TUN3aWRHOXJaVzRpT2lKU1JVWlNSVk5JTFZSUFMwVk9JaXdpZFhObGNsOTBlWEJsSWpvaVkyeHBaVzUwSWl3aWRHOXJaVzVmZEhsd1pTSTZJblJ5WVdSbFgzSmxabkpsYzJoZmRHOXJaVzRpTENKa1pYWnBZMlZmYVdRaU9pSTFOREE1Tm1WbFpTMHpORFkyTFRNd1lUY3RPR1k0WVMxak9XVXhaak01WTJGbU5HUWlMQ0poWTNRaU9udDlmUS5NekpHcWptOVNVRUpuZDVuSHhOUmthY0NQOUdIY0ViaHJTek9sQjVzX1lhNW16UkJtc29BWDc3V0tseV9nUVJaeG9QeGFSc1E1N2tYOF9lcW8zNS1nUSIsImlhdCI6MTcwODI1OTUwOH0.wLpWkQZl5_Aa0DsDEjJMcRPFGH34uJVTprgnvW_Vs1CCu_kA6jov4iXJ7WkSGGzbs1Z6D7pfNjRWzZUvlqI5sQ
🕉📉📈
 
 📉BANK NIFTY📈🕉

 45000 CE

 ABOVE  300

 VIEW/ EDUCATIONAL PURPOSE
300   45000    CE
FIRST ORDER INFORMATION:  {
    'order_name': 'FIRST ORDER', 
    'symbol': 'BANKNIFTY21FEB24C45000', 
    'token': '45811', 
    'buying_price': 301.5, 
    'is_order_executed': False, 
    'order_no': '24021700014088', 
    'target_price': 340.5, 
    'stoploss_price': 260.0, 
    'is_order_cancelled': False, 
    'is_position_squareOff': False, 
    'is_exit_order_placed': False, 
    'exit_order_no': '', 
    'angel_symbol': 'BANKNIFTY21FEB2445000CE'
    }

THREAD 1 IS RUNNING:   True
https://api.shoonya.com/NorenWClientTP//SingleOrdHist
----- AFTER PLACING STOPLOSS ORDER -------- {'order_name': 'FIRST ORDER', 'symbol': 'BANKNIFTY21FEB24C45000', 'token': '45811', 'buying_price': 301.5, 'is_order_executed': True, 'order_no': '24021700014088', 'target_price': 340.5, 'stoploss_price': 260.0, 'is_order_cancelled': False, 'is_position_squareOff': False, 'is_exit_order_placed': True, 'exit_order_no': '24021700014089', 'angel_symbol': 'BANKNIFTY21FEB2445000CE'}      
BOOK PROFIT, currnet price is:  1452.0    FIRST ORDER
https://api.shoonya.com/NorenWClientTP//ModifyOrder
ORDER MODIFIED TIME:  1
THREAD 1 IS RUNNING:   True
ORDER MODIFIED TIME:  1
THREAD 1 IS RUNNING:   True
ORDER MODIFIED TIME:  1
THREAD 1 IS RUNNING:   True
ORDER MODIFIED TIME:  1
THREAD 1 IS RUNNING:   True
ORDER MODIFIED TIME:  1
THREAD 1 IS RUNNING:   True






 VIEW/ EDUCATIONAL PURPOSE
300   45000    CE
FIRST ORDER INFORMATION:  {'order_name': 'FIRST ORDER', 'symbol': 'BANKNIFTY21FEB24C45000', 'token': '45811', 
'buying_price': 301.5, 'is_order_executed': False, 'order_no': '24021700014121', 'target_price': 340.5, 'stoploss_price': 260.0, 
'is_order_cancelled': False, 'is_position_squareOff': False, 'is_exit_order_placed': False, 'exit_order_no': '', 'angel_symbol': 'BANKNIFTY21FEB2445000CE'}
THREAD 1 IS RUNNING:   True


https://api.shoonya.com/NorenWClientTP//SingleOrdHist
----- AFTER PLACING STOPLOSS ORDER -------- {'order_name': 'FIRST ORDER', 'symbol': 'BANKNIFTY21FEB24C45000', 
'token': '45811', 'buying_price': 301.5, 'is_order_executed': True, 'order_no': '24021700014121', 'target_price': 340.5, 
'stoploss_price': 260.0, 'is_order_cancelled': False, 'is_position_squareOff': False, 'is_exit_order_placed': True, 'exit_order_no': 
'24021700014122', 'angel_symbol': 'BANKNIFTY21FEB2445000CE'}      
BOOK PROFIT, currnet price is:  1452.0    FIRST ORDER
https://api.shoonya.com/NorenWClientTP//ModifyOrder
ORDER MODIFIED TIME:  1







https://api.shoonya.com/NorenWClientTP//SingleOrdHist
ORDER HISTORY :::   {'stat': 'Ok', 'norenordno': '24022101512875', 'kidid': '1', 'uid': 'FA152764', 'src_uid': '', 'actid': 'FA152764', 'exch': 'NFO', 'tsym': 'BANKNIFTY21FEB24C46700', 'qty': '15', 'trantype': 'B', 'prctyp': 'SL-LMT', 'ret': 'DAY', 'rejby': 'RED', 'pan': 'DGKPA8809L', 'ordersource': 'API', 'token': '45879', 'pp': '2', 'ls': '15', 'ti': '0.05', 'prc': '331.50', 'trgprc': '330.50', 'dscqty': '0', 's_prdt_ali': 'MIS', 'prd': 'I', 'status': 'REJECTED', 'st_intrn': 'REJECTED', 'rpt': 'Rejected', 'ordenttm': '1708529505', 'norentm': '21:01:45 21-02-2024', 'remarks': 'Option order placed...', 'rejreason': "RED:'MIS' Orders are disallowed after system square off"}
THREAD 1 IS RUNNING:   True
https://api.shoonya.com/NorenWClientTP//SingleOrdHist
ORDER HISTORY :::   {'stat': 'Ok', 
\'norenordno': '24022101512875', 
\'kidid': '1', 
\'uid': 'FA152764', 'src_uid': '', 
\'actid': 'FA152764', 
\'exch': 'NFO', 
\'tsym': 'BANKNIFTY21FEB24C46700', 
'qty': '15', 
'trantype': 'B', 
'prctyp': 'SL-LMT', 
'ret': 'DAY', 
'rejby': 'RED', 
'pan': 'DGKPA8809L', 
'ordersource': 'API', 
'token': '45879', 'pp': '2', 'ls': '15', 'ti': '0.05', 'prc': '331.50', 'trgprc': '330.50', 'dscqty': '0', 's_prdt_ali': 'MIS', 'prd': 'I', 'status': 'REJECTED', 'st_intrn': 'REJECTED', 'rpt': 'Rejected', 'ordenttm': '1708529505', 'norentm': '21:01:45 21-02-2024', 'remarks': 'Option order placed...', 'rejreason': "RED:'MIS' Orders are disallowed after system square off"}


THREAD 1 IS RUNNING:   True
https://api.shoonya.com/NorenWClientTP//SingleOrdHist
ORDER HISTORY :::   {'stat': 'Ok', 'norenordno': '24022101512875', 'kidid': '1', 'uid': 'FA152764', 'src_uid': '', 'actid': 'FA152764', 'exch': 'NFO', 'tsym': 'BANKNIFTY21FEB24C46700', 'qty': '15', 'trantype': 'B', 'prctyp': 'SL-LMT', 'ret': 'DAY', 'rejby': 'RED', 'pan': 'DGKPA8809L', 'ordersource': 'API', 'token': '45879', 'pp': '2', 'ls': '15', 'ti': '0.05', 'prc': '331.50', 'trgprc': '330.50', 'dscqty': '0', 's_prdt_ali': 'MIS', 'prd': 'I', 'status': 'REJECTED', 'st_intrn': 'REJECTED', 'rpt': 'Rejected', 'ordenttm': '1708529505', 'norentm': '21:01:45 21-02-2024', 'remarks': 'Option order placed...', 'rejreason': "RED:'MIS' Orders are disallowed after system square off"}
THREAD 1 IS RUNNING:   True
https://api.shoonya.com/NorenWClientTP//SingleOrdHist
ORDER HISTORY :::   {'stat': 'Ok', 'norenordno': '24022101512875', 'kidid': '1', 'uid': 'FA152764', 'src_uid': '', 'actid': 'FA152764', 'exch': 'NFO', 'tsym': 'BANKNIFTY21FEB24C46700', 'qty': '15', 'trantype': 'B', 'prctyp': 'SL-LMT', 'ret': 'DAY', 'rejby': 'RED', 'pan': 'DGKPA8809L', 'ordersource': 'API', 'token': '45879', 'pp': '2', 'ls': '15', 'ti': '0.05', 'prc': '331.50', 'trgprc': '330.50', 'dscqty': '0', 's_prdt_ali': 'MIS', 'prd': 'I', 'status': 'REJECTED', 'st_intrn': 'REJECTED', 'rpt': 'Rejected', 'ordenttm': '1708529505', 'norentm': '21:01:45 21-02-2024', 'remarks': 'Option order placed...', 'rejreason': "RED:'MIS' Orders are disallowed after system square off"}
THREAD 1 IS RUNNING:   True
https://api.shoonya.com/NorenWClientTP//SingleOrdHist








































from typing import _SpecialForm
from NorenRestApiPy.NorenApi import NorenApi
from threading import Timer
from certify import next_wednesday
# --------------------------
import logging
import pyotp
from telethon import TelegramClient, events
import time
import threading 
from SmartApi import SmartConnect
import asyncio

# --------------------- SMART API CREDENTIALS ---------------------
smart_api_key = 'm1QkdimV'
smartClientID = 'N51889834'
smartPWD = 9862
smartToken = "FKVSHLRW7RDNV6YUYAIK7F5D4I"
smartOTP = pyotp.TOTP(smartToken).now()
correlation_id = "abc123"

smartApi = SmartConnect(smart_api_key)
data = smartApi.generateSession(smartClientID, smartPWD, smartOTP)

refreshToken = data['data']['refreshToken']
print("REFRESH TOKEN IS = " , refreshToken)
feedToken = smartApi.getfeedToken()





class ShoonyaApiPy(NorenApi):
  def __init__(self):
    NorenApi.__init__(self, host='https://api.shoonya.com/NorenWClientTP/', websocket='wss://api.shoonya.com/NorenWSTP/')
    global api
    api = _SpecialForm

 

# LOGIN FINVASIA
api = ShoonyaApiPy()
token = '23IL2KM7VY7D5WUL557W67EG34J75LM3'
otp = pyotp.TOTP(token).now()









# FINVASIA CREDENTIALS
user = 'FA152764'
pwd = '@RadeonV11'
factor2 = otp
vc = 'FA152764_U'
app_key = 'd2ffa5fa99ba35cfce2593eef2714dfa'
imei = 'abc1234'
 
# logging.basicConfig(level=logging.DEBUG)



# FINVASIA API LOGIN
loginResult = api.login(userid=user, password=pwd, twoFA=otp, vendor_code=vc, api_secret=app_key, imei=imei)

 


# ----------- MANAGE CHANNEL --------------
# print("THE LOGIN RESULT IS: ",loginResult)
# MY CHANNEL : 1001959827182
# SHIVAY CHANNEL: 1001640142628


senderUserID = -1001959827182
receiverUserID = -1001959125612
# ----------- MANAGE CHANNEL --------------




# DEFAULT STATE FOR ORDER OBJECT 1
order1_Obj = {
  'order_name': 'FIRST ORDER',
  'symbol': '',
  'token': 0,
  'buying_price' : 0,
  'is_order_executed': False,
  'order_no': '',
  'target_price' : 0,
  'stoploss_price': 0,
  'is_order_cancelled' : False,
  'is_position_squareOff' : False,
  'is_exit_order_placed': False,
  'exit_order_no': '',
  'angel_symbol': '',
}

# DEFAULT STATE FOR ORDER OBJECT 2
order2_Obj = {
  'order_name': 'SECOND ORDER',
  'symbol': '',
  'token': 0,
  'buying_price' : 0,
  'is_order_executed': False,
  'order_no': '',
  'target_price': 0,
  'stoploss_price' : 0,
  'is_order_cancelled' : False,
  'is_position_squareOff' : False,
  'is_exit_order_placed' : False,
  'exit_order_no': '',
  'angel_symbol': '',
}

cancel_target_orderno= ''

# DEFAULT STATE FOR THREAD
thread_1_Active = True
thread_2_Active = True

order_1_history = None
order_2_history = None


def getOrderStauts(orderHistory):
  return orderHistory[0]

api_called = 0
order_history_count = 0

token1 = 0
token2 = 0





# LOOP FOR ORDER 1-------------------------------------------------------------------
def loopForOrder1():
  global thread_1_Active
  while thread_1_Active:
    if token1 != 0 and order1_Obj['order_no'] != '':
      print("THREAD 1 IS RUNNING:  ", thread_1_Active)
      handleSquareOff(order1_Obj['angel_symbol'], order1_Obj['token'], order1_Obj)
    time.sleep(1/2.5)      
# -----------------------------------------------------------------------------------





# LOOP FOR ORDER 2-------------------------------------------------------------------
def loofForOrder2():
  global thread_2_Active
  while thread_2_Active:
    if token2 != 0 and order2_Obj['order_no'] != '':
      print("THREAD 2 IS RUNNING:  ", thread_2_Active)
      handleSquareOff(order2_Obj['angel_symbol'], order2_Obj['token'], order2_Obj)
    time.sleep(1/2.5) 
# -----------------------------------------------------------------------------------







# RUN DIFFERENT THREAD TO GET BOTH LATEST DATA---------------------------------------
threadOrder1 = threading.Thread(target=loopForOrder1)
threadOrder2 = threading.Thread(target=loofForOrder2)

threadOrder1.start()
threadOrder2.start()
# -----------------------------------------------------------------------------------






# #------------------------------------------------------------------------------- IMPLEMENTING TELEGRAM FUNCTIONALITY-------------------------------------------------------
api_id = 29395559
api_hash = 'd3f70d97f92a979dc5578168c14fa117'
client = TelegramClient('session1', api_id, api_hash)


isNeedToPlaceSecondOrder = True


# ON MESSAGE RECEIVE -------------
async def placeOrder(messageText):
    global token1
    global token2
    global isNeedToPlaceSecondOrder

    # EXTRACT MESSAGE CONTENT
    message_content = messageText.upper()
    findNifty = message_content.find("NIFTY")

    # SLICE PRICE FROM TEXT-----------------------------------
    price = ""
    aboveText = message_content.find("ABOVE")
    for i in range(aboveText+3, aboveText + 12):
        if message_content[i].isdigit():
            price = price + message_content[i]

    
    # SLICE STRIKE PRICE FROM TEXT----------------------------
    strike = ""
    for i in range(findNifty+ 4, findNifty + 15):
        if message_content[i].isdigit():
            strike = strike + message_content[i]
    


    # SLICE POSITION SIDE FROM TEXT---------------------------
    side = ""        
    for i in range(findNifty + 10, findNifty + 17):
        if(message_content[i] == "P"):
            side = "PE"
        if(message_content[i] == "C"):
            side = "CE"


    optionName = "BANKNIFTY " + strike + " " + side
    print(price+ "   "+ strike+ "    "+ side)


    # CONVERT STRING PRICE TO FLOAT
    order_price = float(price)
    stoploss_price = order_price - 40

    # MODIFY ORDER PRICE
    order_price = order_price + 1.5
    target_price = order_price + 39


    # EXTRACT SYMBOL AND TOKEN FROM FINVASIA
    searchInstruements = api.searchscrip(exchange="NFO", searchtext=optionName)['values']
    myInstrument = searchInstruements[0]
    finvasiaTradingSymbol = myInstrument['tsym']
    finvasiaTradingToken = myInstrument['token']


    # EXTRACT SYMBOL AND TOKEN FROM ANGEL LTP DATA
    angelLtpData = smartApi.ltpData("NFO", finvasiaTradingSymbol, finvasiaTradingToken)
    angelSearchData = angelLtpData['data']
    angelTradingSymbol = angelSearchData['tradingsymbol']
    angelTradingToken = angelSearchData['symboltoken']
    


    # PLACE ORDER
    if(message_content.find("BANK")):
      order_response = api.place_order(
      buy_or_sell='B', 
      product_type='I', 
      exchange='NFO', 
      tradingsymbol=finvasiaTradingSymbol, 
      quantity=15, 
      discloseqty=0, 
      price_type='SL-LMT', 
      price=order_price, 
      trigger_price=order_price - 1, 
      retention='DAY', 
      remarks='Option order placed...')

      orderNo = order_response['norenordno']


      # IF ORDER 1 IS EMPTY------------
      if token1 == 0:
        token1 = finvasiaTradingToken
        order1_Obj['symbol'] = finvasiaTradingSymbol
        order1_Obj['token'] = finvasiaTradingToken
        order1_Obj['buying_price'] = order_price
        order1_Obj['order_no'] = orderNo
        order1_Obj['target_price'] = target_price
        order1_Obj['stoploss_price'] = stoploss_price
        order1_Obj['angel_symbol'] = angelTradingSymbol

        print("FIRST ORDER INFORMATION: ", order1_Obj)
        

        #  SEND ORDER NOTIFICATION
        msg = f'''BUY ORDER PLACED:
                    AT PRICE: {order_price}
                    TARGET PRICE: {target_price}
                    STOPLOSS PRICE: {stoploss_price}
                    ORDER NO: {orderNo}
                    ANGEL SYMBOL: {angelTradingSymbol}
                    ANGEL TOKEN: {angelTradingToken}
                    FINVASIA SYMBOL: {finvasiaTradingSymbol}
                    FINVASIA TOKEN: {finvasiaTradingToken}'''
        
        await forwardMessage(receiverUserID, msg)
      
      # IF ORDER 1 IS NOT EMPTY THEN FILL ORDER 2
      else:
        token2 = finvasiaTradingToken
        order2_Obj['symbol'] = finvasiaTradingSymbol
        order2_Obj['token'] = finvasiaTradingToken
        order2_Obj['buying_price'] = order_price
        order2_Obj['order_no'] = orderNo
        order2_Obj['target_price'] = target_price
        order2_Obj['stoploss_price'] = stoploss_price
        order1_Obj['angel_symbol'] = angelTradingSymbol

        print("SECOND ORDER INFORMATION: ", order2_Obj)
        

        # SEND ORDER NOTIFICATION 
        msg = f'''BUY ORDER PLACED:
                    AT PRICE: {order_price}
                    TARGET PRICE: {target_price}
                    STOPLOSS PRICE: {stoploss_price}
                    ORDER NO: {orderNo}
                    ANGEL SYMBOL: {angelTradingSymbol}
                    ANGEL TOKEN: {angelTradingToken}
                    FINVASIA SYMBOL: {finvasiaTradingSymbol}
                    FINVASIA TOKEN: {finvasiaTradingToken}'''
        
        await forwardMessage(receiverUserID, msg)
# ----------------------------------------------------------------------------------------------------------------------------------------------------





state = "LOSS"
isTargetModified = False
isStoplossModified = False
isAlternateOrderCancelled = False

# HANDLE SQUARE OFF ORDER------------------------------------------------------------------------------------------------------------------------------
def handleSquareOff(angel_token_symbol, token, orderItem):
  global api_called
  global order_history_count
  global cancel_target_orderno
  global state
  global isStoplossModified, isTargetModified
  global isAlternateOrderCancelled
  global thread_1_Active
  global thread_2_Active

  # IF ORDER NOT EXECUTED THEN CHECK EXECUTION STATUS
  if orderItem['is_order_executed'] == False:
    orderItem_history = api.single_order_history(orderno=orderItem['order_no']) 
    order_history_count = order_history_count + 1
    print("ORDER EXECUTION STATUS :::  ", getOrderStauts(orderItem_history)['tsym'], " STATUS: ", getOrderStauts(orderItem_history)['stat'], " CHECK STATUS COUNT: ", order_history_count)

    # IF ORDER EXECUTED THEN
    if getOrderStauts(orderItem_history)['stat'] == 'Ok' and getOrderStauts(orderItem_history)['status'] == "COMPLETED":
      orderItem['is_order_executed'] = True                                       
      
      # PLACE SQUARE OFF ORDER
      square_off_order_response = api.place_order(
        buy_or_sell='S', 
        product_type='I', 
        exchange='NFO', 
        tradingsymbol=orderItem['symbol'], 
        quantity=15, 
        discloseqty=0, 
        price_type='SL-LMT', 
        price=orderItem['stoploss_price'], 
        trigger_price=orderItem['stoploss_price']+1, 
        retention='DAY', 
        remarks='stoploss order placed...'
      )

      #print(f''' ************* ******** ****** SL PRICE: {orderItem['stoploss_price']}   SL TRIGGER: {orderItem['stoploss_price'] + 1} ''')

      
      if orderItem['is_exit_order_placed'] == False:
        orderItem['exit_order_no'] = square_off_order_response['norenordno']
        orderItem['is_exit_order_placed'] = True
        #print("----- AFTER PLACING STOPLOSS ORDER --------", order1_Obj)
      #------------------------------------------------------------------------------- REF: README.PY > PLACE SQUARE OFF ORDER

      
        # 1.
        if orderItem['order_name'] == 'FIRST ORDER' and orderItem['is_order_executed'] == True and order2_Obj['order_no'] != '':
          cancel_target_orderno = order2_Obj['order_no']
          thread_2_Active = False

        # 2.
        if orderItem['order_name'] == 'SECOND ORDER' and orderItem['is_order_executed'] == True and order1_Obj['order_no'] != '':
          cancel_target_orderno = order1_Obj['order_no']
          thread_1_Active = False

        # 3.
        if cancel_target_orderno != '' and isAlternateOrderCancelled == False:
          cancelled_order = api.cancel_order(orderno=cancel_target_orderno)
          isAlternateOrderCancelled = True
        
        #------------------------------------------------------------------------------- REF: README.PY > CANCEL ALTERNATE ORDER
        

  # IF ORDER EXECUTED THEN HANDLE SQUARE OFF BASED ON CURRENT PRICE
  if orderItem['is_order_executed'] == True:
    current_price_data = smartApi.ltpData("NFO", angel_token_symbol, str(token))                    # -------- FETCH LATEST PRICE
    current_price = current_price_data['data']['ltp']                                               # -------- EXTRACT CURRENT PRICE
    

    if float(current_price) > float(orderItem['buying_price']):                                     # -------- CHECK POSITION STATUS
      state = "PROFIT"
    else:
      state = "LOSS"

    print("ORDER IS IN STATE: ", state)
    if state == "PROFIT" and isTargetModified == False:                                             # -------- IF POSITION IS IN PROFIT
      print("BOOK PROFIT, currnet price is: ",float(current_price), "  ", orderItem['order_name'] )

      modified_response  = api.modify_order(
        exchange='NFO', 
        tradingsymbol=orderItem['symbol'], 
        orderno=orderItem['exit_order_no'],
        newquantity=15, 
        newprice_type='SL-LMT', 
        newprice=orderItem['target_price'], 
        newtrigger_price=orderItem['target_price'] + 1)      # TRIGGER PRICE < LIMIT PRICE

      
      isTargetModified = True           # TARGET MODIFIED = TRUE
      isStoplossModified = False        # STOPLOSS MODIFIED = FALSE
      api_called = api_called +1

      print("ORDER MODIFIED AFTER PLACING STOPLOSS ORDER @officerdotakhter: ", modified_response)
      #--------------------------------------------------------------------- REF: README.PY > MODIFIY TARGET
    


    if state == "LOSS" and isStoplossModified == False:
      print("BOOK LOSS, currnet price is: ",float(current_price), "  ", orderItem['order_name'])

      api.modify_order(
        exchange='NFO', 
        tradingsymbol=orderItem['symbol'], 
        orderno=orderItem['exit_order_no'],
        newquantity=15, 
        newprice_type='SL-LMT', 
        newprice=orderItem['stoploss_price'], 
        newtrigger_price=orderItem['stoploss_price'] + 1)     # TRIGGER PRICE > LIMIT PRICE
      
      isStoplossModified = True                               # STOPLOSS MODIFIED = TRUE
      isTargetModified = False                                # TARGET MODIFIED = FALSE
      api_called = api_called + 1
      #--------------------------------------------------------------------- REF: READMY.PY > MODIFY STOPLOSS

    
    print("ORDER MODIFIED FOR : --- ", api_called, " --- TIME ")




# ------------------------------------------------------------------------------------------------------------------------------------------------------

















# FUNCTION FOR FORWARDING MESSAGE
async def forwardMessage(receiver, message):
    try:
        await client.send_message(receiver, message)
    except Exception as err:
        print("Failed to forward messages: ", err)




# FUNCTION WHEN NEW MESSAGE ARRIVE
@client.on(events.NewMessage(chats=senderUserID))
async def whenSenderSendMessage(event):
    msg_text = event.message.message.upper()
    print(msg_text)
    await placeOrder(msg_text)





# START TELETHON API-----------
async def main():
  await client.run_until_disconnected()

if __name__ == '__main__':
  client.start()
  client.loop.run_until_complete(main())
# #------------------------------------------------------------------------------- IMPLEMENTING TELEGRAM FUNCTIONALITY-------------------------------------------------------

























"""