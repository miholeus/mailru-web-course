sudo rm /etc/nginx/sites-enabled/default
sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/ask.conf   /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart
sudo pip install -r /home/box/web/etc/requirements.txt
