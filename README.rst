Userinput
=========================================================================================
|pip| |downloads|

Simple python package to handle CLI user input.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install userinput


Available validators
----------------------------------------------
Some commonly used validators are available with the package.

+-------------------+-------------------------------------------------------------------------------------------------------+
| Validator name    | Description                                                                                           |
+===================+=======================================================================================================+
| email             | Check if given input string is a valid email.                                                         |
+-------------------+-------------------------------------------------------------------------------------------------------+
| version_code      | Check if given input string is a valid version code.                                                  |
+-------------------+-------------------------------------------------------------------------------------------------------+
| url               | Check if given input string is a valid URL. Does not check if given URL is online.                    |
+-------------------+-------------------------------------------------------------------------------------------------------+
| human_bool        | Check if given input string is a human Boolean, such as "yes", "y", "true", "si", "no", "n", "false". |
+-------------------+-------------------------------------------------------------------------------------------------------+
| integer           | Check if given input string is a integer numeric value.                                               |
+-------------------+-------------------------------------------------------------------------------------------------------+
| positive_integer  | Check if given input string  is a positive integer numeric value.                                     |
+-------------------+-------------------------------------------------------------------------------------------------------+
| non_empty         | Check if given input string is not empty.                                                             |
+-------------------+-------------------------------------------------------------------------------------------------------+
| hostname          | Check if given input string is a reachable host name.                                                 |
+-------------------+-------------------------------------------------------------------------------------------------------+
| ip                | Check if given input string is a reachable IP address.                                                |
+-------------------+-------------------------------------------------------------------------------------------------------+

Use them as follows:

.. code:: python

    from userinput import userinput

    result = userinput(
        "my_label",
        validator="validator name goes here"
    )

You can also chain validators.
They will be called in the order you provide.

.. code:: python

    from userinput import userinput

    result = userinput(
        "my_label",
        validator=[
            "validator name goes here",
            my_custom_validation_function
        ]
    )


Available sanitizers
-----------------------------------------------
Some commonly used sanitizers are available with the package.

+-------------------+-------------------------------------------------------------------------------------------------------+
| Validator name    | Description                                                                                           |
+===================+=======================================================================================================+
| human_bool        | Cast human Boolean specified above in validators to python Booleans.                                  |
+-------------------+-------------------------------------------------------------------------------------------------------+
| strip             | Remove padding spaces and repeated spaces.                                                            |
+-------------------+-------------------------------------------------------------------------------------------------------+

Use them as follows:

.. code:: python

    from userinput import userinput

    result = userinput(
        "my_label",
        sanitizer="sanitizer name goes here"
    )

You can also chain sanitizers.
They will be called in the order you provide.

.. code:: python

    from userinput import userinput

    result = userinput(
        "my_label",
        sanitizer=[
            "sanitizer name goes here",
            my_custom_sanitification_function
        ]
    )


.. |pip| image:: https://badge.fury.io/py/userinput.svg
    :target: https://badge.fury.io/py/userinput
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/userinput
    :target: https://pepy.tech/badge/userinput
    :alt: Pypi total project downloads 