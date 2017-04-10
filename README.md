# HumanCode Simulation

This is a simple Text Service with the following RESTful API endpoints:

* POST '/chat', params: username, text, timeout
* GET '/chat', params: username

## Instructions
Post requests must have the username and text parameters. The timeout parameter is optional. The post request will respond with the id the made object

```
{
  id:5
}
```

Get requests must be made with the username. It will return all messages for that user.
```
[
  {
    id: 5, text: 'test message’
  },
  {
    id: 6, text: 'test message 2’
  }
]
```

All messages have a default timeout of the current time in seconds. When the timeout is added as a parameter, the message will be available for that duration. Only unexpired messages can be received.

```
POST /chat?username=thisuser&text=sup&timeout=50000
```
