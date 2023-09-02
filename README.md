# File System Event Listener

A simple file system event listener that checks for creation, deletion and moving of files and/or directories where the `main.py` file is placed.

## Installation

First we need to install the dependencies using
`pip install -r requirements`

## Setting up

Then we must add our Gmail credentials in `email_notifier.py`, modifying `sender_email` and `receiver_email`.
In `password` we need to add an App password provided by Google, we can get this password by:

1. Going to the desired or personal [Google Account](https://myaccount.google.com/).
2. Select Security
3. Under "Signing in to Google", select _2-Step Verification_
4. At the bottom of the page, select _App passwords_
5. In _Select app_ choose _Other_, then type a name we can remember.
6. Press _Generate_
7. An app password will be shown to us, it will not be shown to us again therefore it must be saved in a safe place.
8. With this password, we can replace it in the `password` variable in `email_notifier.py`

Once we have setup the credentials we are now ready to run the application.

## Usage

To run
`python3 main.py`
