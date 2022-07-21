##Creating Your Own Django Apps

You might have noticed that there is no real program code in your project so far. There is a settings file with configuration information, an almost empty URLs file, and a command-line utility that launches a website that doesn’t do much.

This is because to create a functioning Django website, you need to create Django applications. A Django application (or app for short) is where the work gets done. Apps are one of Django’s killer features. Not only do they allow you to add functionality to a Django project without interfering with other parts of the project, but apps are designed to be portable so you can use one app in multiple projects.

So, let’s create our first custom Django app. Our social club website needs an events calendar to show upcoming events for the club, so we’re creating a Django app called events.

Fire up your Python virtual environment, switch into the \myclub_root folder and run the command:

python manage.py startapp events
This is what your command shell output should look like:

(env_myclub) ...> cd myclub_root
(env_myclub) ...\myclub_root> python manage.py startapp events
(env_myclub) ...\myclub_root>
Once you have created your app, you must tell Django to install it into your project. This is easy to do—inside your settings.py file is a list named INSTALLED_APPS. This list contains all the apps installed in your Django project. Django comes with a few apps pre-installed, we just have to add your new events app to the list (change in bold):

1 INSTALLED_APPS = [
2     'events.apps.EventsConfig',
3     'django.contrib.admin',
4     # more apps
5 ]
Inside every app, Django creates a file, apps.py, containing a configuration class named after your app. Here, the class is named EventsConfig. To register our app with Django, we need to point to the EventsConfig class—which is what we are doing in line 2 of our modified INSTALLED_APPS list.

If you were wondering, EventsConfig contains two configuration options by default—the name of the app (“events”), and the default autofield data type.

Line Numbering in Code Examples

Throughout the book, I use line numbering to make it easier for you to follow along with the explanations.

As I often use code snippets from your application files, the line numbering in the example is not the same as the line numbering in the actual source code file.

Now let’s look inside the \myclub_root folder to see what Django has created for us:

\events
    \migrations
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
The migrations folder is where Django stores migrations, or changes to your database. There’s nothing in here you need to worry about right now.
__init__.py tells Python that your events app is a package.
admin.py is where you register your app’s models with the Django admin application.
apps.py is a configuration file common to all Django apps.
models.py is the module containing the models for your app.
tests.py contains test procedures that run when testing your app.
views.py is the module containing the views for your app.
Now we have a complete picture of a Django project, we can also answer the question from earlier in the chapter: “well, if it’s not a view, where does it go?”

When you have code that isn’t a view, you create a new Python module (.py file) inside your app and put related functions and classes inside the file. Note the emphasis on related. If you have a bunch of functions that provide database management utilities, for example, put them all in one file. Functions and classes not related to database management should go in another file. You should also try to be descriptive in naming modules—after all, it’s more sensible to put your database functions in a file called db_utils.py than a file called monkeys.py…

When creating new modules for your Django project, you should also consider scope. While adding custom modules to apps is far more common (and more portable), you can have project-level modules (e.g., Django’s manage.py) and site-level modules. In the latter case, your custom modules should go in the same folder as your settings.py file.

The last couple of points might seem blindingly obvious, but it’s important to understand that, while Django has a default logic to its structure, nothing is cast in stone. Django is flexible and allows you to expand and change your project structure to suit the logic of your web application.

Now we have a thorough understanding of the structure of Django’s projects and apps, the next obvious question, given we are building web applications is “how do we navigate a Django project?”

To answer this question, we need to check out the final piece of the Django big picture puzzle—URL configurations.

URLconfs—Django’s Navigator
There’s one last piece to the Django framework puzzle—the critical communication pathway that matches a request on the client-side with a project resource (the arrows between the view and the template in Figure 3.3). Like all web applications, Django uses Uniform Resource Locators (URLs) to match content with a request.

Django’s urls package provides dozens of functions and classes for working with different URL formats, name resolution, exception handling and other navigational utilities. However, at its most basic, it allows you to map a URL to a function or class within your Django project.

A Django URL configuration (or URLconf for short) matches a unique URL with a project resource. You can think of it being like matching a person’s name with their address. Except in Django, we’re not matching a street address—we’re matching a Python path using Python’s dot notation.

Assuming you’re not familiar with dot notation, it’s a common idiom in object-oriented programming. I like to think of the dot like a point because the dot points to something. With Python, the dot operator points to the next object in the object chain.

In Django classes, the object chain is like this:

package.module.class.method
Or with functions:

package.module.function.attribute
Some real-life examples:

forms.Form points to the Form class in the forms package.
events.apps.EventsConfig points to the EventsConfig class in the apps sub-package of the events package (i.e., the apps.py file in your events app).
django.conf.urls points to the urls package inside the conf package inside Django, which is also a Python package!
This can sometimes get a bit confusing, but if you remember to join the dots (sorry, a bad pun there), you can usually find out what the dot operator is referring to.

With a URLconf, the path points to a function or class inside a module (.py file). Let’s look at our Django project diagram again (Figure 3.5).

Django App Structure 2
Figure 3.5: Finding functions and classes with Django’s URLconfs.

To create a URLconf, we use the path() function. The first part of the function is the URL, so in Figure 3.5 the URL is app1/. The path() function then maps this URL to app1.views.some_view().

Assuming your site address is http://www.mycoolsite.com, in plain English we’re saying:

“When someone navigates to http://www.mycoolsite.com/app1/, run the some_view() function inside app1’s views.py file”.

Note a URL doesn’t have to map to a view—it can map to any module in your Django app. For example, you may have a set of wireless environmental sensors that post data back to the server. You could have a custom module called sensors.py that has a function or class to record the sensor data to your database, all without ever touching a view.

And that’s all there is to it. Of course, URLconfs can do a lot more than map a static URL to a function or class, but if you can understand the basics—that Django’s incredibly fast and powerful navigation system is based on the simple concept of matching a URL with a resource—then you have all you need to tie all your Django apps together into a navigable web project.

A Final Note on Writing Django Apps
A common and inevitable question arises once you get your head around Django’s basic structure:

“Where do I start? Should I start with writing my models, the URL configurations, my views? Or what?”

Well, here’s your final heresy for the chapter: it doesn’t matter.

Some people like to start by building all the models so they can see how the data structure looks; others prefer to build the visual layout first, so they start with templates. Others might like to get the basic communication framework in place, so they start with views and URLconfs. Others will start at whatever point seems logical for the project.

Being pragmatic to the bone, I am usually in the last group. I try not to get fixated on what someone else thinks is the right or the wrong way to do things and try to find the simplest and quickest way to achieve the result I want. I also like to work incrementally starting small getting the flow right and building on it to create the complete application. This approach means I inevitably end up jumping from one element to another as the application grows.

Your brain is wired differently to mine and every other programmer. This is a Good Thing. Just remember, an imperfect start to a project is way better than not starting at all. Do what works for you.
