# Oauth2System

OAuth2System - a simple authorization system for multiple sites or projects.

# Quick Start Demo

First, you need to [register an account](https://emeraldermine.onpella.app/registration), and also [confirm your email](https://emeraldermine.onpella.app/account/email_confirm). [Here](https://emeraldermine.onpella.app/apps) you can create your first application. After that, you will receive a CLIENT ID and a CLIENT SECRET. You'll need them later.
This is the authorization link - https://emeraldermine.onpella.app/oauth2/authorize?client_id={YOUR_CLIENT_ID}&scope={permissions} (in the "scope" value, you must insert the values that the system receives.) 
For example, identify - access to username, display name, user id and avatar, and email to email. If you want to add 2 values at once, then specify something like "identify+email". 
After successful authorization, the user will be redirected to the link you specified in the redirect uri field with the ending "?code={random_code}". You can get the value "code" and already using it and client id and client secret you can get the user using the API.

# API USAGE

And so, to get a user, you need to use this link "emeraldermine.onpella.app/api/user?oauth_token={OAUTH_TOKEN}&client_id={YOUR_CLIENT_ID}&client_secret={YOUR_CLIENT_SECRET}".


# Examples

The following example will be shown based on a site created in [Python](https://www.python.org) - [Flask](https://pypi.org/project/Flask/).
