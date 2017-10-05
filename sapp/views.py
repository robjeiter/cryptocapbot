from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from sapp.models import User


def get_price(request):
    peth = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD').json()
    pethp = float(peth.get('USD'))
    pbtc = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD').json()
    pbtcp = float(pbtc.get('USD'))

    result_message = {}

    for user in User.objects.filter(currency='ETH', lower__gte=pethp):
        result_message['chat_id'] = user.userid
        token = '435375582:AAG5gMaGbKfsCkZyWZL2SMsxjDVnFQgFoyc'
        result_message['text'] = "Hey there! We inform you because your threshold has been hit. ETH at its current price of "+str(pethp)+"/USD is now lower than the limit set by you. Since your limit was hit we removed all your thresholds. Feel free to type any messange and to restart the bot to define new thresholds."
        post_message_url = "https://api.telegram.org/bot{0}/sendMessage".format(token)
        response_msg = json.dumps(result_message)
        status = requests.post(post_message_url, headers={
            "Content-Type": "application/json"}, data=response_msg)
   
    User.objects.filter(currency='ETH', lower__gte=pethp).update(upper='1000000', lower='0')

    for user in User.objects.filter(currency='ETH', upper__lte=pethp):
        result_message['chat_id'] = user.userid
        token = '435375582:AAG5gMaGbKfsCkZyWZL2SMsxjDVnFQgFoyc'
        result_message['text'] = "Hey there! We inform you because your threshold has been hit. ETH at its current price of "+str(pethp)+"/USD is now higher than the limit set by you. Since your limit was hit we removed all your thresholds. Feel free to type any messange and to restart the bot to define new thresholds."
        post_message_url = "https://api.telegram.org/bot{0}/sendMessage".format(token)
        response_msg = json.dumps(result_message)
        status = requests.post(post_message_url, headers={
            "Content-Type": "application/json"}, data=response_msg)

    User.objects.filter(currency='ETH', upper__lte=pethp).update(upper='1000000', lower='0')

    for user in User.objects.filter(currency='BTC', lower__gte=pbtcp):
        result_message['chat_id'] = user.userid
        token = '435375582:AAG5gMaGbKfsCkZyWZL2SMsxjDVnFQgFoyc'
        result_message['text'] = "Hey there! We inform you because your threshold has been hit. BTC at its current price of "+str(pbtcp)+"/USD is now lower than the limit set by you. Since your limit was hit we removed all your thresholds. Feel free to type any messange and to restart the bot to define new thresholds."
        post_message_url = "https://api.telegram.org/bot{0}/sendMessage".format(token)
        response_msg = json.dumps(result_message)
        status = requests.post(post_message_url, headers={
            "Content-Type": "application/json"}, data=response_msg)

    User.objects.filter(currency='BTC', lower__gte=pbtcp).update(upper='1000000', lower='0')

    for user in User.objects.filter(currency='BTC', upper__lte=pbtcp):
        result_message['chat_id'] = user.userid
        token = '435375582:AAG5gMaGbKfsCkZyWZL2SMsxjDVnFQgFoyc'
        result_message['text'] = "Hey there! We inform you because your threshold has been hit. BTC at its current price of "+str(pbtcp)+"/USD is now higher than the limit set by you. Since your limit was hit we removed all your thresholds. Feel free to type any messange and to restart the bot to define new thresholds."
        post_message_url = "https://api.telegram.org/bot{0}/sendMessage".format(token)
        response_msg = json.dumps(result_message)
        status = requests.post(post_message_url, headers={
            "Content-Type": "application/json"}, data=response_msg)

    User.objects.filter(currency='BTC', upper__lte=pbtcp).update(upper='1000000', lower='0')

    return HttpResponse("A warm hello to diocshka from Cryptocapbot deployed on AWS")
    

def get_message_from_request(request):

    received_message = {}
    decoded_request = json.loads(request.body.decode('utf-8'))

    if 'message' in decoded_request:
        received_message = decoded_request['message'] 
        received_message['chat_id'] = received_message['from']['id'] # simply for easier reference

    nutzerid = received_message['chat_id']
    #lastmessagestatus = User.objects.filter(userid=nutzerid)
    #lsmsg = lastmessagestatus.value("lastmessagestatus", flat=True)
    lsm = User.objects.filter(userid=nutzerid).values('lastmessagestatus')
    lsms = str(lsm)
    lsmt = lsms.replace("<QuerySet [{'lastmessagestatus': '","")
    lsmu = lsmt.replace("'}]>","")
    wert = received_message['text']



    #make an if statement and check what was the received message status of the user
    if lsmu == '1a':
        if wert.isdigit():
            nutzer = User.objects.get(userid=nutzerid)
            nutzer.upper = wert
            nutzer.lastmessagestatus = '2a'
            nutzer.save()
        else:
            nutzer = User.objects.get(userid=nutzerid)
            nutzer.lastmessagestatus = '2x'
            nutzer.save()

    if lsmu == '1b':
        if wert.isdigit():
            nutzer = User.objects.get(userid=nutzerid)
            nutzer.upper = wert
            nutzer.lastmessagestatus = '2b'
            nutzer.save()
        else:
            nutzer = User.objects.get(userid=nutzerid)
            nutzer.lastmessagestatus = '2y'
            nutzer.save()


    elif lsmu == '3b':
        if wert.isdigit():
            nutzer = User.objects.get(userid=nutzerid)
            nutzer.lower = wert
            nutzer.lastmessagestatus = '4a'
            nutzer.save()
        else:
            nutzer = User.objects.get(userid=nutzerid)
            nutzer.lastmessagestatus = '4y'
            nutzer.save()

    elif lsmu == '3a':
        if wert.isdigit():
            nutzer = User.objects.get(userid=nutzerid)
            nutzer.lower = wert
            nutzer.lastmessagestatus = '4a'
            nutzer.save()
        else:
            nutzer = User.objects.get(userid=nutzerid)
            nutzer.lastmessagestatus = '4x'
            nutzer.save()


    return received_message

#answer messages
antwortethu = "Thanks, now please enter your lower limit (USD/ETH) for receiving notifications:"
antwortbtcu = "Thanks, now please enter your lower limit (USD/BTC) for receiving notifications:"
antwortx = "Please type a valid number! Please do not put any characters. So far I also can't process digits (sorry for that)."


def send_messages(message, token):
    
    post_message_url = "https://api.telegram.org/bot{0}/sendMessage".format(token)

    result_message = {}         # the response needs to contain just a chat_id and text field for  telegram to accept it
    #making sure the message is sent to the same person as received from, with same chat id
    result_message['chat_id'] = message['chat_id']

    nutzerid = message['chat_id']
    wert = message['text']
    #lastmessagestatus = User.objects.filter(userid=nutzerid).values('lastmessagestatus')
    lsm = User.objects.filter(userid=nutzerid).values('lastmessagestatus')
    lsms = str(lsm)
    lsmt = lsms.replace("<QuerySet [{'lastmessagestatus': '","")
    lsmu = lsmt.replace("'}]>","")



    peth = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD').json()
    pethp = float(peth.get('USD'))
    pbtc = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD').json()
    pbtcp = float(pbtc.get('USD'))

    
    notifyethlow = User.objects.filter(currency='ETH', lower__gte=pethp)
    #users = notifyethlow.userid
    #for userid in notifyethlow:
        #do something
    """
    try:
        notifyethlow = User.objects.get(currency='ETH', lower__gte=pethp)
        users = notifyethlow.userid
    except:
        users = 'fun'
    """

    if lsmu == '2a':
        result_message['text'] = antwortethu
        nutzer = User.objects.get(userid=nutzerid)
        nutzer.lower = wert
        nutzer.lastmessagestatus = '3a'
        nutzer.save()

    elif lsmu == '2b':
        result_message['text'] = antwortbtcu
        nutzer = User.objects.get(userid=nutzerid)
        nutzer.lower = wert
        nutzer.lastmessagestatus = '3b'
        nutzer.save()

    elif lsmu == '4a':
        cur = User.objects.filter(userid=nutzerid).values('currency')
        up = User.objects.filter(userid=nutzerid).values('upper')
        lo = User.objects.filter(userid=nutzerid).values('lower')
        cur1 = str(cur)
        up1 = str(up)
        lo1 = str(lo)
        cur2 = cur1.replace("<QuerySet [{'currency': '","")
        up2 = up1.replace("<QuerySet [{'upper':","")
        lo2 =lo1.replace("<QuerySet [{'lower':","")
        cur3 = cur2.replace("'}]>","")
        up3 = up2.replace("}]>","")
        lo3 =lo2.replace("}]>","")

        antwortend = "That's it. You are all set. You will receive notifications if 1 " +cur3 +" is higher than" +up3+ " USD or lower than" +lo3+" USD. To change your thresholds type any message and restart the bot."
        result_message['text'] = antwortend
        nutzer = User.objects.get(userid=nutzerid)
        nutzer.lastmessagestatus = '0'
        nutzer.save()

    elif lsmu == '2x':
        result_message['text'] = antwortx
        nutzer = User.objects.get(userid=nutzerid)
        nutzer.lastmessagestatus = '1a'
        nutzer.save()

    elif lsmu == '2y':
        result_message['text'] = antwortx
        nutzer = User.objects.get(userid=nutzerid)
        nutzer.lastmessagestatus = '1b'
        nutzer.save()

    elif lsmu == '4x':
        result_message['text'] = antwortx
        nutzer = User.objects.get(userid=nutzerid)
        nutzer.lastmessagestatus = '3a'
        nutzer.save()

    elif lsmu == '4y':
        result_message['text'] = antwortx
        nutzer = User.objects.get(userid=nutzerid)
        nutzer.lastmessagestatus = '3b'
        nutzer.save()


    else:

        if 'ETH' in message['text']:
            antworteth = "Cool, now please enter your upper limit (USD/ETH) for receiving notifications. The current price of 1 ETH is "+str(pethp)+" USD."
            result_message['text'] = antworteth
            nutzer = User.objects.update_or_create(userid=nutzerid, defaults = {'upper': '1000000', 'lower': '0', 'currency': 'ETH', 'lastmessagestatus': '1a'})

        elif 'BTC' in message['text']:
            antwortbtc = "Cool, now please tell me what's your upper limit (USD/BTC) for receiving notifications. The current price of 1 BTC is "+str(pbtcp)+" USD."
            result_message['text'] = antwortbtc
            nutzer = User.objects.update_or_create(userid=nutzerid, defaults = {'upper': '1000000', 'lower': '0', 'currency': 'BTC', 'lastmessagestatus': '1b'})
        

        elif 'Ferenc' in message['text']:
            result_message['text'] = 'some text'
            #get_price()
        

        else:
            result_message['text'] = "Welcome to Cryptocap Telegram bot! Which currency would you like to track? For Etherum type ETH! For Bicoin type BTC!"

    response_msg = json.dumps(result_message)
    status = requests.post(post_message_url, headers={
        "Content-Type": "application/json"}, data=response_msg)



class tbotview(generic.View):

    # csrf_exempt is necessary because the request comes from the Telegram server.
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)


    # Post function to handle messages in whatever format they come
    def post(self, request, *args, **kwargs):
        TELEGRAM_TOKEN = '435375582:AAG5gMaGbKfsCkZyWZL2SMsxjDVnFQgFoyc'
        message = get_message_from_request(request)
        send_messages(message, TELEGRAM_TOKEN)

        return HttpResponse()