# Dynamic CRM!

- This source base on [Django Cookiecuter](https://github.com/pydanny/cookiecutter-django)
- With config to use [Docker](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)
- Template from [Metronic](https://themeforest.net/item/metronic-responsive-admin-dashboard-template/4021469)

## Feature

 - User management
 - Contact management (still working on it)
	 - Profile
	 - Activity
	 - Note
 - Dynamic field for module
 - Dynamic filter for module
 - Dynamic Choice
 - Dynamic dashboard with amchart (Not working yet)
 - Notification
	 - Current using jquery interval to call
	 - Push notice through Browser [Webpush](https://github.com/safwanrahman/django-webpush)


## Description

### User
- Custom User Model
- Datatable with Loop data form View
- API using DRF
	- Read only API

### Choice
- Datatable with Loop data form View
- API using DRF
	- API with custom function to create nested

### App Management
- List Model can edit field (exlude system model)
- Datatable with Loop data form View
- API using JsonResponse

### Filter
- Create filter for App (exclude system app)
- Datatable with Loop data form View
- API using DRF

### Noitce
- Only have api to count unread/ read action/ list
- API using JsonResponse
- Generate key npm install -g web-push && web-push generate-vapid-keys fill into .envs/.django

### Activities
- API using DRF
- Sub form for external form

### Note
- API using DRF
- Sub form for external form


### External Form
- Add external form to module view

