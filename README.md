# cache-buster

This program tries to solve problem of web browsers caching CSS stylesheet, using a method called cache-busting.

## Why CSS caching happens?

Web browsers usually cache CSS, so if the page is reloaded it doesn't need to get it again. Why? To increase web performance. Problem with this is that expiration for CSS can be up to 1 year (depending on your server config). Method for combating caching is called "cache-busting", and there are multiple solutions. One of them is to change your server config to make your CSS expire faster. This is easy solution, but if you have big CSS files, it can hurt your web performance (especially if you have big amount of clients connected at the same time and setting to short expiry time). If you want good web performance, making web browser download CSS only when you change it is a good solution. This program uses the other method.

## How does it work?

It works by changing the link in your html code and CSS filename.

For example:
```
...
<link href="styles/style.css" rel="stylesheet">
...
```
to:
```
...
<link href="styles/style?13-06-21.css" rel="stylesheet">
...
```

##TODO
- add cli
- actually make something working
