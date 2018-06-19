from twython import  Twython
import os

twitter = Twython("", "",
                  "",
                  "")
twitter.verify_credentials()


results = os.popen('speedtest-cli --simple').read().split("\n")[:-1]
ping, down, up = [int(x.split(" ")[1].split(".")[0]) for x in results]
if down < 40:
    twitter.update_status(status = "Hey @Comcast, why am I paying for 150down when I'm only getting" \
                                   " {}down in San Jose?  @xfinity @comcastcares".format(down))







