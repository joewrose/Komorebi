# Komorebi

The Komorebi website revolves around the idea of a social media for those who want to experience the creativity of others but don't want the other aspects of social media that can turn toxic such as commenting, messaging and invasive recommendation algorithms. Komorebi has the base essentials for a pleasant experience and a bare-bones recommendation alrogithm which will recommend images for you based on what similar users also liked.

## Features

- Dynamic Webpages with likes and dislikes
- Each image has a dedicated webpage with a share button, to encourange sharing on other platforms
- Thumbnail-isation of images on the home page to keep the website responsive
- Creation, editing, and deletion of accounts
- Personalisation of accounts with profile images and descriptions

## Technology Used

Komorebi needs the following packages to work as intended:

- [Django] - Framework used to create the website
- [AJAX] - Used to update the webpages and database with likes, dislikes and follows
- [Django-ImageKit] - Creates thumbnails to keep website responsive
- [Pillow] - Helps handling of images within Django
- [Bootstrap] - Set of CSS classes which makes styling easier
- [Django-Crispy-Forms] - Bootstrap classes for forms


   [Django-ImageKit]: <https://github.com/matthewwithanm/django-imagekit>
   [Pillow]: <https://pypi.org/project/Pillow/2.2.1/>
   [Django-Crispy-Forms]: <https://django-crispy-forms.readthedocs.io/en/latest/>
   [Bootstrap]: <https://getbootstrap.com/>
