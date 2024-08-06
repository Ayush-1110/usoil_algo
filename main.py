import time

import color
# import fetch_webhook
import delete_data
import asyncio


unique_id = '23cd1e76-93ea-46c4-be39-1998f36a7959'
import fifteen_minute as fifteen_minute
import one_minute as one_minute
import fetch_webhook as fetch_webhook
import place_order as place_order


# color = True
color_2 = False
status = True

# if (color_2 == True):
#     print("Buy", time.ctime())
#     place_order.test_meta_api_synchronization('buy')
#
# else:
#     print("Sell", time.ctime())
#     place_order.test_meta_api_synchronization('sell')
print("Algo Started")

while True:
    y = fetch_webhook.fetch_webhook_data()
    if(len(y)>0):
        one_minute.one_minute(y)
        fifteen_minute.fifteen_minute(y)
    if(color.one_minute_color != status):
        if (color.one_minute_color == color.fifteen_minute_color):
            if(color.one_minute_color == True):
                asyncio.run(place_order.test_meta_api_synchronization('buy'))
            if(color.one_minute_color == False):
                asyncio.run(place_order.test_meta_api_synchronization('sell'))
        if(color.one_minute_color != color_2):
            asyncio.run(place_order.test_meta_api_synchronization('close'))
        status = not status



    time.sleep(30)