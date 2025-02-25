.. py-notify documentation master file.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Py-Message Documentation
=============================================================================================================

Py-Message is a lightweight package enabling sending messages from Python using email, simple-message-service (SMS),
and an application for messaging, Pushover. Pushover is the easiest to get set up. Email, especially if using GMail,
is a close second. Finally, although extremely convenient once set up, SMS requires the most effort to get up and
running. The upside is SMS will work with any mobile device, even a 1992 Nokia brick.

Setup
------

Using the included messaging functions requires first getting set up with the notification and messaging provider, and
saving the connection credentials as environment variables. Although the functions do allow for passing credentials in
as arguments, it is far better to use environment variables to keep credentials out of scripts and code.

Pushover
^^^^^^^^^

If looking for the easiest solution, `Pushover <https://pushover.net>`_ is a very easy solution for instant push
notifications. For $5 per client, Pushover enables sending instant notifications to web clients and mobile devices.
For $10 I get notifications through Safari on my Mac, and on my iPhone through the Pushover application. I especially
like the ability to set up different channels, so I have notifications categorized based on what the notification
pertains to.

Getting set up requires installing the client application on your phone, and configuring an application on the website.
The client application is quite simple, and is available on both `iPhone <https://pushover.net/clients/ios>`_ and
`Android <https://pushover.net/clients/android>`_. It is also possible to receive notifications through a `desktop
web client as well <https://pushover.net/clients/desktop>`_.

With the client set up, next you need to set up an account on the `Pushover website <https://pushover.net>`_ and
`create an application <https://pushover.net/apps/build>`_. Applications, at least for me, are very much like topics I
use for organizing messages.

Azure Simple-Message-Service (SMS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Py-Message API
===================

.. automodule:: py_message
    :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _reStructured Text Cheat Sheet: https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html
.. _NBSphinx: https://nbsphinx.readthedocs.io/en/0.8.8/
.. _Sphinx Autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html