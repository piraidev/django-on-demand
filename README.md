# DJANGO ON-DEMAND

Manage suppliers and consumers in an on-demand marketplace. 
More info about on-demand: https://www.pubnub.com/blog/what-is-the-on-demand-economy/

Yes, fork it.

Please, contribute.

Thanks!

Full documentation on [insert documentation url]

### Install app
This app is still work in progress. To install the work in progress version 
`pip3 install -i https://test.pypi.org/simple/ django-on-demand`

### INSTALLED_APPS requirement
This app is using `django-rest-framework` to provide API endpoints, which means this app will need to be added to the list of installed apps.
The app will automatically install `django-rest-framework` if it's not installed.
`on_demand` also needs to be added to the list of installed apps.

```
INSTALLED_APPS = [
    .,
    .,
    .,
    'on_demand',
    'rest_framework'
]
```