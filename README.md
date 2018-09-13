# Monitoring ncurses
> Minor tool to monitoring services in terminal

![demo](demo.gif)

## How-to

Create a config.yml with the same structure as bellow:
```yml
services:
  - name: Google
    url: https://www.google.com.br
  - name: Twitter
    url: https://twitter.com
  - name: Failed API
    url: https://mustfail.com
```
Now, run it!

```
~$ python3 ./main.py
```

## Roadmap
* color tips
* asynchronous hits to apis
* python 2.7 support
* reduce retry in requests package

## Meta

Alex Rocha - [about.me](http://about.me/alex.rochas) -
