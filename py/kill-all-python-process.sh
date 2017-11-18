#/bin/sh

ps -ef | grep python | cut -d ' ' -f 4 | xargs kill