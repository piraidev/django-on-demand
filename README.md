# DJANGO SOCIAL REST API

Welcome to this open project aimed to help building una buena rest api used for social app.

Yes, fork it.

Please, contribute.

Thanks!

### Instal dependencies
`pip3 install -r requirements.txt`

### Install mysqlclient library
**NOTE:** On some installations Django has issues recognized the installed library. This was solved by installing versions of the library previous to `1.3.13`. For example, installing this specific one `pip3 install mysqlclient==1.3.12` resulted in success.

### MySQL
Set an empty password for user `root` or change the password on `DATABASES` section on `settings.py` but don't push the changes!

After doing this, create a database called `socialapp`.

Then, located in the root directory (where `manage.py` is) run `python3 manage.py migrate` - This will create all the tables and relationships from the models in the db.

## Config
Properties that depend on the environment (production vs pre production environment), such as passworks, keys and tokens should be configured in a file named `local_settings.py` under `socialapp` directory.

This file is *gitignored* to ensure this sensitive data is not published on the repository and that values are explicitly set for the environment where the server is running.

### Run the server
By running `python3 manage.py runserver` you'll be able to start the server.

If you are using VScode, to enable the linter do:
* Go to Code -> Preferences -> Settings, and add the following to the user settings json:
    `    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django"
   ]`