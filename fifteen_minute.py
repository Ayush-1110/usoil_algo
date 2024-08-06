import fetch_webhook as fetch_webhook
import delete_data as delete_data
unique_id = '23cd1e76-93ea-46c4-be39-1998f36a7959'
import color as color






def fifteen_minute(y):
    if(len(y)>0):
        for x in range(len(y)):
            if(y[x]['content'] == "usoil_changed_15min"):
                color.fifteen_minute_color = not color.fifteen_minute_color
                delete_id = y[x]['uuid']
                delete_data.delete_data(delete_id,unique_id)
        # return color
