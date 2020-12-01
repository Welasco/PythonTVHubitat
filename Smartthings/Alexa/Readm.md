In order to create a access we need to follow these steps.

Create you SmartApp, save and publish. If you don't publish it will fail.

Enable OAuth for you app and take a note of your cliend id and secred.

Acccess this link using any browser:
https://graph-na02-useast1.api.smartthings.com/oauth/authorize?response_type=code&redirect_uri=http://localhost&scope=app&client_id=1c0d3c76-d521-49f3-88c9-da9184f3e05f

replace cliend_id with your ID.

It will redirect the browser back to a localhost/?code=xxxxxx

Get the xxxxxx code from your browser.

Using powershell (don't use any browser or it will failt with 500 due cokies).

Invoke-WebRequest "https://graph-na02-useast1.api.smartthings.com/oauth/token?grant_type=authorization_code&scope=app&redirect_uri=http://localhost&client_id=1c0d3c76-d521-49f3-88c9-da9184f3e05f&client_secret=ecf8a1f5-5d8d-4c24-86b2-f0ad3df96b75&code=4gjzB8"

It will create your access token for 50 yeaers.

Here a link with all smartthings api:

https://github.com/tmaiaroto/smartthings-unofficial-docs/blob/master/Documentation.md

Now we need to get the device endpoint using your access token like this:


invoke-webrequest "https://graph-na02-useast1.api.smartthings.com/api/smartapps/endpoints?access_token=431840ed-f528-4abb-8512-4c94be25c731"

it will give you the url you can use to access your device using your access token:

Accessing your device using your endpoint and the access token:

Invoke-WebRequest "https://graph-na02-useast1.api.smartthings.com:443/api/smartapps/installations/67f1498f-fd87-419a-9454-df2f26605cfe/alexatv/on?access_token=6a487af1-b3fa-4560-9dac-5e2e33f4d666"

