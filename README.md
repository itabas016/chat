## Simple Chat ##

_*Base on asyncore, socket packages, have a try to write this simple chat tool. Reference a exercise from Python Tutorial*_

### Server ###

#### Configure ####

```python
# download repo to local
git clone git@github.com:itabas016/chat.git ~

#modify config.py
vim ~/chat/config.py

# Server Host address, default is 0.0.0.0
HOST='0.0.0.0'

# Server host port, default is 6666
PORT=6666

# Current server name
NAME='My Chat'

# Current server maximun support connections online,
# default is 50
MAX_CONNECTIONS=50

# run
python ~/chat/server.py
```

#### Features ####

A complete workflow contains:

> login -> check unique nick name -> login successfule

> chatroom -> add/remove/say/look/who _PS. server will push message for each command._

> logout

### Client ###

#### Usage ####

```bash
python ~/chat/client.py

```
