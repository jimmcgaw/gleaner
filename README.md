# Gleaner System

The Glean System is meant to be used by Food Banks or other organizations that harvest produce from residential or commercial properties. It's meant to allow users to register, submit details about their crop, and allow system administrators to coordinate dates and times with the owner of the crop in order to schedule harvesting.

It is not intended to be used a system to manage volunteers.

Right now, the project is under active development, so it's unlikely to be ready for production use in the near future. Feel free to get in touch with me with any questions or suggestions.

## Technology

The Gleaner system is built with the Python-based web framework Django. It uses node-based tools like gulp, bower, and npm for dev tooling.

## Getting Started

If you'd like to play along at home, clone this repository. To install Python dependencies, run the classic:

``` $ pip install -r requirements.txt ```

and to install the tooling stuff:

``` $ npm install
 $ bower install ```

 To boot up the development server at http://localhost:8000/, run:

 ``` $ python manage.py runserver ```
