# disposable-emails
Weed out disposable email providers with ease 🚀

## Installation

I will upload this package to PyPi in the near future. As for now:

    pip3 install git+https://github.com/maxmalysh/disposable-emails

There are no dependencies. You don't need Django, Flask or any third-party API.

## How to use

Check an email:

    >>> from disposable_emails import is_disposable_email
    >>> is_disposable_email('john.smith@mailforspam.com')
    True
    >>> is_disposable_email('john.smith@gmail.com')
    False

Check a domain:

    >>> from disposable_emails import is_disposable_domain
    >>> is_disposable_domain('temp-mail.com')
    True
    >>> is_disposable_domain('kremlin.ru')
    False

**Using Django?** There is a form validator which you can use with forms:

    from django import forms
    from disposable_emails.contrib.django import disposable_validator

    class FooForm(forms.Form):
        email = forms.EmailField(
            label="Email",
            max_length=254,
            validators=[disposable_validator]
        )

And with models:

    from django import models
    from disposable_emails.contrib.django import disposable_validator

    class FooModel(models.Model):
        email = models.EmailField(validators=[disposable_validator])


## Credits

This package uses **[disposable](https://github.com/andreis/disposable/)** by @andreis as a source of disposable email services. It is imported as a submodule, so you can expect `disposable_emails` to have as fresh disposable database as possible.

## Contributions

Code contributions are welcome! Just drop a pull request.

