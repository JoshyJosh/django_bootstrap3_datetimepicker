# Django Calendar Widget

I've been working on integrating [Bootstrap3 Datepicker](https://eonasdan.github.io/bootstrap-datetimepicker/) into a few django projects.
For this to work i need to make a working Event object that has its own unique slug, thats slugified from the title. If the title has already been used there should be an iterator.

Example of three model slugs that have the same model titles: **title, title_1, title_2**

## Current to do list
- make a proper test case in the calendar_events app
- make a working slug generator (my current regex solution dosen seem to register the slug (maybe different keyword instead of slug?))
- integrate bootstrap datetimepicker in a test view
- somehow manage work and sleep
