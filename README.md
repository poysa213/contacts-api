# contacts-api
Contacts api with django rest framework
Allow you to save your contacts (phone_number) with their names.

### Features
* JWTAuthentication
* Create contacts
* Read contacts
* Update contacts
* Delete contacts



### API Endpoints
| HTTP Verbs | Endpoints | Action |  
| --- | --- | --- 
| POST | /api/contacts/ | Create a new contact | 
| GET | /api/contacts/ | Get all contacts |  
| GET | /api/contacts/pk | Get a single contact |
| PUT | /api/contacts/pk | Update a contact |
| DELETE | /api/contacts/pk | Delete a contact | 
| POST | /api/auth/register/ | Create an account |
| POST | /api/auth/token/ | Get you token(refresh&acces) |
| POST | /api/auth/token/verify/ | Verify yoour token | 
| POST | /api/auth/token/regresh/ | Refresh yoour token | 

 
 
