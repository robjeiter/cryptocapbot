# Python Code
# myapp/management/commands/mytask.py
"""
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
#from sapp.models import User
print('say hi')
class Command(BaseCommand):
	def get_price(self, **options):
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
	    """