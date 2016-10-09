# Install

You should clone this repository and put it as you own private project in your Git version control system. For now, let's say you fork the project on Github, and that your Github username is ```toto```.
Then the repository should be available on:

```
https://github.com/toto/demo_celery
```

## Install Redis on the public machine

If the machine is running Window, it may then be simpler to use the first option with Docker:

### With Docker

Install Docker: https://docs.docker.com/engine/installation/

Then just run this (do not forget to change the password):

```
sudo docker run -d -p 0.0.0.0:6379:6379 --name redis redis redis-server --requirepass 1234
```

### Natively

On Linux it is quite simple but you need to compile it:

```
sudo apt-get install wget make g++ screen
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
sudo make install
```

Then you can open a screen to launch Redis in a persitant manner. Again, do not forget to change the password:

```
screen
redis-server --requirepass 1234
```

## Install the demo on your machine

Here you clone the repo using SSH because you want to be able to push easily.

```
git clone git@github.com:toto/demo_celery.git
```

Then you just have to install the Python libs:

```
cd demo_celery
sudo pip install -r requirements.txt
```

## Install the demo on the compute machine

Here you clone using HTTPS because you may not have any SSH key setup:

```
git clone https://github.com/toto/demo_celery.git
```

Then you also just have to install the Python libs:

```
cd demo_celery
sudo pip install -r requirements.txt
```

And you can start the worker with ```make worker``` or with:

```
celery multi start node1 -A distributed --loglevel=info --pidfile=distributed.pid
celery multi start node2 -A updater --loglevel=info --pidfile=updater.pid
```

# Try install

On your local computer, running ```python main.py``` should return 1129.
If you commit changes, the worker pulls it when you call ```updater.update()``` and updates itself.

You should put all your code in ```distributed.py```.

Have fun !!

