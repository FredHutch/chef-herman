# Herman

`Herman` is an agent that accepts push [webhooks](https://developer.github.com/webhooks/) from a github repository, placing data about the push onto a [Redis](http://redis.io) list for processing by other agents.

This application is based on [Flask](http://flask.pocoo.org/) and used Jack Stouffer's [Flask Foundation](https://jackstouffer.github.io/Flask-Foundation/) using the [bootstrapy project](https://github.com/kirang89/bootstrapy) to build its core.


Below here is the rest of the original readme, saved until it's not necessary.

#Flask Foundation
[![Build Status](https://travis-ci.org/JackStouffer/Flask-Foundation.png)](https://travis-ci.org/JackStouffer/Flask-Foundation)

Documentation is located at [https://jackstouffer.github.io/Flask-Foundation/](https://jackstouffer.github.io/Flask-Foundation/)

Flask Foundation is a solid foundation for flask applications, built with best practices, that you can easily construct your website/webapp off of. Flask Foundation is different from most Flask frameworks as it does not assume anything about your development or production environments. Flask Foundation is platform agnostic in this respect.

Built off of the [bootstrapy project](https://github.com/kirang89/bootstrapy)

Best practices were learned from:
* [Creating Websites With Flask](http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/)
* [Getting Bigger With Flask](http://maximebf.com/blog/2012/11/getting-bigger-with-flask/)
* [Larger Applications With Flask](http://flask.pocoo.org/docs/patterns/packages/).

## License

Flask-Foundation is licensed under the BSD license. For more info see LICENSE.md

# Want to learn more about Flask?

I also wrote a book on Flask! You can order it [here](https://www.packtpub.com/web-development/mastering-flask).
