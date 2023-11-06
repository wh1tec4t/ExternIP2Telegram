First full stable version of this Bot.

Functions:
- Tell me via Telegram changes when Extern IP of my Home Router change.

Solutions:
- Use an IRC Chat PING-PONG feature to detect Changes on my Home Extern IP Router and send a Push signal to advise of Change.

Dependencies:
- Minimal dependencies: socks to IRC connection and requests to Telegram connection.

Execution as a daemon on Linux system:
- #nohup python3 ipext.py &
