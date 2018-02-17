import requests
import simplejson

def coincoin(event, context):

    coincoinpriceurl = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(coincoinpriceurl)
    coincoin = simplejson.loads(response.text)

    coincoinusdpriceasstring = coincoin["bpi"]["USD"]["rate"].split('.')[0]
    coincoinusdpriceasstring = coincoinusdpriceasstring.replace(',','.')
    coincoinusdpriceasstring = coincoinusdpriceasstring.replace('.','')
    coincoinpriceinusd = int(float(coincoinusdpriceasstring))

    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': coincoinpriceinusd
            }
        }
    }

    return response

print(coincoin('',''))
