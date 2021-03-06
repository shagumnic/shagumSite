from __future__ import absolute_import, unicode_literals
from celery import task, shared_task
from celery.schedules import crontab
from notificationApp.models import VideoGame, VideoGamesList
from django.contrib.auth.models import User
import requests
import json
from webpush import send_user_notification
from datetime import datetime, date

@shared_task()
def update_discount_rate():
	steamIds = ''
    #gamePk = []
	#chosen_discount_rate_dict = {}
	for game in VideoGame.objects.all() :
		if game.isDiscount == True :
		#gamePk.append(game.id)
			if game.steamId not in steamIds :
				steamIds += game.steamId 
				steamIds += ","
	            
	steamIds = steamIds[:len(steamIds)-1]
	if steamIds != '' :
		url = "http://store.steampowered.com/api/appdetails?cc=us&appids=" + steamIds + "&filters=price_overview"
		response = requests.request("GET", url)
		result = response.json()
	else :
		result = {}
	    
	discount_percent_dict = {}
	for key in result.keys() :
		if result[key]["success"] == True :
			discount_percent_dict[key] = result[key]["data"]["price_overview"]["discount_percent"]
		else :
			discount_percent_dict[key] = None

	if len(discount_percent_dict) != 0 :
		for game in VideoGame.objects.all() :
			if game.isDiscount == True and discount_percent_dict[game.steamId] != None and \
			(game.discountrate.discount_percent == None or \
			game.discountrate.discount_percent != discount_percent_dict[game.steamId]):
				game.discountrate.update(discount_percent = discount_percent_dict[game.steamId])
				# discount_description = 
				# game.discountrate_set.all().first().update(discount_percent = 1)
				# discount_description.discount_percent = 1
				# discount_description.save()


@shared_task()
def notify_push_discount() :
	for game in VideoGame.objects.all() :
		if game.isDiscount == True :
			if game.discountrate.discount_percent >= game.discountrate.chosen_discount_percent :
				#do something to notify them about it
				user = game.videogameslist.user
				head = "Dicount Notification"
				body = "The game %s in your %s is on discount for %s %." % (game.name, game.videogameslist.name, str(game.discountrate.discount_percent))
				url = "http://store.steampowered.com/api/appdetails?cc=us&appids=" + game.steamId
				payload = {'head' : head, 'body' : body, 'url' : url}
				send_user_notification(user = user, payload = payload, ttl = 3600)

@shared_task()
def update_released_date() :
	slugs = set()
	for game in VideoGame.objects.all() :
	#if game.isReleased == True :
	#gamePk.append(game.id)
		slugs.add(game.slug)
	for slug in slugs :
		url = "https://api.rawg.io/api/games/" + slug
		response = requests.request("GET", url)
		resultGame = json.loads(response.text)
		released_date = datetime.strptime(resultGame["released"], "%Y-%m-%d").date()
		if released_date != VideoGame.objects.filter(slug = slug).first().released_date :
			VideoGame.objects.filter(slug = slug).update(released_date = released_date)

@shared_task()
def notify_push_released() :
	for game in VideoGame.objects.all() :
		if game.isReleased == True :
			if game.released_date <= datetime.today().date() :
				#do something to notify them about it
				user = game.videogameslist.user
				head = "Released Notification"
				body = "The game %s in your %s is already released on %s." % (game.name, game.videogameslist.name, game.released_date.strftime("%Y-%m-%d"))
				url = "http://store.steampowered.com/api/appdetails?cc=us&appids=" + game.steamId
				payload = {'head' : head, 'body' : body, 'url' : url}
				send_user_notification(user = user, payload = payload, ttl = 3600)