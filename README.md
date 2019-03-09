# Game-Shop-Microservices
Rewrite [Game-Shop](https://github.com/JohnDing1995/GameShop) project with microservices architecture
## API
### Authentication
`\auth\login`

Method: `POST`

Request:

```json
    {
        'email': Your Email
        'password': Your password
    }
```
Response:
  ```json
      {
          'status': Result of action,
          'message': Message,
          'auth_token': Your session token
```
`\auth\register`

Method: `POST`

Request:
    
  ```json
      {
        'email':Your Email(unique)
        'password': Your password
        'username': Username you pick
      }
 ```
Response:
  ```json
      {
          'status': Result of action,
          'message': Message,
          'auth_token': Your session token
      }
```
### User
`\users\me`

Get information of current logged user

Mmethod: `GET`

Request:

Header



```
        {Authentication: 'Bearer [Your token]'}
```
Response
```
    {
        'id': Current user's id,
        'email': Current user's email
        'name': Current user name
     }
```