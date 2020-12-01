import requests

r = requests.get('https://www.bing.com')

print(r.status_code)

data = '''
{
	"version": "1.0",
	"session": {
		"new": true,
		"sessionId": "amzn1.echo-api.session.245ea756-d53a-48a4-9522-a6bb8b7e7f3a",
		"application": {
			"applicationId": "amzn1.ask.skill.5487b5b4-0d03-4e89-bc50-16d5587bccef"
		},
		"user": {
			"userId": "amzn1.ask.account.AG6KYTFZUHNQNFDZMH25YVKUQGBRW3A2LGGQUR3BNSCTRVLU7V2PNMX5HXESRYUVOWWJ6QJHD5CT2L77FZL4WC6SYW2MY7AWUHXIAUINYLBYWNOCPMOWIFPOPTRBKESQKKVUNOCBWIN67AEEMJYFBIJUTYH7LVUZODVRSHLGOR6WM5E7FNMWCMOIXHBJSAJXIBRQLDMTDVPK5EI"
		}
	},
	"context": {
		"System": {
			"application": {
				"applicationId": "amzn1.ask.skill.5487b5b4-0d03-4e89-bc50-16d5587bccef"
			},
			"user": {
				"userId": "amzn1.ask.account.AG6KYTFZUHNQNFDZMH25YVKUQGBRW3A2LGGQUR3BNSCTRVLU7V2PNMX5HXESRYUVOWWJ6QJHD5CT2L77FZL4WC6SYW2MY7AWUHXIAUINYLBYWNOCPMOWIFPOPTRBKESQKKVUNOCBWIN67AEEMJYFBIJUTYH7LVUZODVRSHLGOR6WM5E7FNMWCMOIXHBJSAJXIBRQLDMTDVPK5EI"
			},
			"device": {
				"deviceId": "amzn1.ask.device.AGCKPOJINEJHTMRG5KODB57PFZ6DPYWPTRPEQN7Q7XAZI3UHNUCEIT3YZLY5AUFBS5YA6JHEV53I6J6JWWO2ZOBH7DVR34QOMVPFAUKOU5CDCT2SYD6ZXZTVGXUON7DMWN2FB4DVDLXSUIYZ2MUPD7QD5U3IWFBHQITBLL4S6FWF4X67XXOS6",
				"supportedInterfaces": {}
			},
			"apiEndpoint": "https://api.amazonalexa.com",
			"apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjU0ODdiNWI0LTBkMDMtNGU4OS1iYzUwLTE2ZDU1ODdiY2NlZiIsImV4cCI6MTU0NjUzNTgzMCwiaWF0IjoxNTQ2NTMyMjMwLCJuYmYiOjE1NDY1MzIyMzAsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUdDS1BPSklORUpIVE1SRzVLT0RCNTdQRlo2RFBZV1BUUlBFUU43UTdYQVpJM1VITlVDRUlUM1laTFk1QVVGQlM1WUE2SkhFVjUzSTZKNkpXV08yWk9CSDdEVlIzNFFPTVZQRkFVS09VNUNEQ1QyU1lENlpYWlRWR1hVT043RE1XTjJGQjREVkRMWFNVSVlaMk1VUEQ3UUQ1VTNJV0ZCSFFJVEJMTDRTNkZXRjRYNjdYWE9TNiIsInVzZXJJZCI6ImFtem4xLmFzay5hY2NvdW50LkFHNktZVEZaVUhOUU5GRFpNSDI1WVZLVVFHQlJXM0EyTEdHUVVSM0JOU0NUUlZMVTdWMlBOTVg1SFhFU1JZVVZPV1dKNlFKSEQ1Q1QyTDc3RlpMNFdDNlNZVzJNWTdBV1VIWElBVUlOWUxCWVdOT0NQTU9XSUZQT1BUUkJLRVNRS0tWVU5PQ0JXSU42N0FFRU1KWUZCSUpVVFlIN0xWVVpPRFZSU0hMR09SNldNNUU3Rk5NV0NNT0lYSEJKU0FKWElCUlFMRE1URFZQSzVFSSJ9fQ.eYVS32JNAiH1kV4U0kxLz7P6_W3DxjMS9kgVN86gW98_2waru-jZ9iYhQu05j6LeRKUc9p-iK__ZRJyLPIvETBPDxRNCwLccR7-ohQQIkSN2Y7O4YFjz6Vn_cNL9kepuousDspoHzaiUYyk1_ti1lOJuyJvQYXQF6dpYnjha3KvkzGfp6eUT-9NispaBikD1mOE4oMYK85jxLe7C2zqYr39laARUh2RIDgQhG4f-eXwRHWtBDYTQG33gWY_mAUehlfbfXirw5xl3LXBwgrX59nUrOSYnvL6ASFFZEqsdJSYn2N1nKveKlN40m5nVTXb9oTVuZUFAJG4B7KHIGQjFWQ"
		},
		"Viewport": {
			"experiences": [
				{
					"arcMinuteWidth": 246,
					"arcMinuteHeight": 144,
					"canRotate": false,
					"canResize": false
				}
			],
			"shape": "RECTANGLE",
			"pixelWidth": 1024,
			"pixelHeight": 600,
			"dpi": 160,
			"currentPixelWidth": 1024,
			"currentPixelHeight": 600,
			"touch": [
				"SINGLE"
			]
		}
	},
	"request": {
		"type": "IntentRequest",
		"requestId": "amzn1.echo-api.request.0f2a7ff2-f53b-4fb2-abfb-c941aa01f2df",
		"timestamp": "2019-01-03T16:17:10Z",
		"locale": "en-US",
		"intent": {
			"name": "channelup",
			"confirmationStatus": "NONE",
			"slots": {
				"number": {
					"name": "number",
					"value": "5",
					"confirmationStatus": "NONE",
					"source": "USER"
				}
			}
		}
	}
}
'''
headers = {'Content-Type': 'application/json'}
r = requests.post('https://vwsfunction.azurewebsites.net/api/alexapy', data=data, headers=headers, verify=False)
requests.get("https://graph-na02-useast1.api.smartthings.com/api/smartapps/installations/4ba0f9ec-c728-461d-b420-63608a397a07/alexatv/volumeupby-3?access_token=f438c5ca-76e2-4f2b-b5ef-3ad3960a5900")

print(r.text)