# drf_project_base
An backend api built using [Django REST framework](https://www.django-rest-framework.org/).

Available endpoints:
### api/user/register/
Fields:
- email (required)
- password (required)
- first_name
- last_name

Returns a serialized user object as response.

An account verification token is sent to the user's email once user creation has is done succesfully.
Currently this behaviour is simulated, and the sent email is printed on console. 


### api/user/activate/
Fields:
- token (required)

### auth/token/

Fields:
- grant_type (required)
- username (required)
- password (required)
- client_id (required)
- client_secret

Given the correct access credentials, this endpoint (provided by oauth2_provider app) returns a bearer access token. An authorization application needs to be set up first to provide the oauth2 authorization. Check out this [tutorial](https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html) for further details.

### api/user/change-password/

An end point for changing user password.

Bearer token must be supplied here for authentication.

Fields:
- password (required)

### api/user/users/{id}

Returns the details of the user corresponding to the id.

If a valid bearer token is not supplied in the request header, only the user's first_name will be retrieved.

### api/user/users/

Returns a list containing the details of each user.

If a valid bearer token is not supplied in the request header, details will be limited to the users' first_name.
