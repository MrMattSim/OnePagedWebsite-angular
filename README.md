One-Paged Website (angular)
===========================

A single-page website using [Flask](http://flask.pocoo.org), SQLite, and AngularJS.

Set up
------

1. Run `app.py` to create the database
2. Edit the created `sqlite.db` file to add projects (note: `date` is plain text to allow for custom time ranges or "Ongoing" projects; it is assumed the most recently added project is what should be listed at the top of the list)
3. Change the links and "Your Name" instances in `static/index.html` as appropriate

By default, there is only a "Project" model, but the project can easily be extended to support other models if desired.