![LUSO Bites logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Welcome Luso Bites, 

Your culinary haven for exploring and savoring the rich gastronomic tradition of Portugal. In this space, embark on a journey of authentic aromas and flavors where I share delightful recipes capturing the essence of Portuguese cuisine. From classic dishes to contemporary interpretations, LusoBites is a celebration of a passion for Portuguese cooking, inviting you to experience the magic in every bite. Discover Portugal's culinary heritage, one delicious morsel at a time.

Live Blog- [LUSO Bites](https://luso-bites-9e7b470f6cac.herokuapp.com/)

![Responsiveness of the website]()

## :ledger: Index

## User Experience (UX)

A visitor to our blog can be an amateur in the kitchen or even a professional to increase their knowledge of Portuguese cuisine. They are eager to expand and enrich their recipe collection or simply share them with others.

### User Stories

### Design

#### Blog Colour

![Colour Palette]()

Given that the core of my platform is centered on the world of Portuguese cuisine, I opted for an immaculate white background, accompanied by green details (thus representing the vivid color of nature), and reds (thus representing Portugal).

#### Images

The web app has no fixed images. All the images is uploaded.

#### Fonts

The main font used for the body is the elegant Orienta font. The logo, painting titles and footer feature the Sigmar font.

#### Wireframes

<details>
<summary>Home Page</summary>

![Home Page]()
</details>

<details>
<summary>Home Page Mobile</summary>

![Home Page Mobile]()
</details>

<details>
<summary>Gallery</summary>

![Gallery]()
</details>

<details>
<summary>Gallery Mobile</summary>

![Gallery]()
</details>

<details>
<summary>The Recipes</summary>

![The Recipes]()

</details>

<details>
<summary>The Recipes Mobile</summary>

![The Recipes Mobile]()

</details>


## Agile Methodology

To handle the development process using an agile approach, we use GitHub projects. You can check the project board [here](https://github.com/users/Goncalves95/projects/3) for reference.

Each User Story is called a title and has its own points to reach so that point can be said to be closed. It is assigned to a person responsible for developing it. And with the labels so that we can focus on the most important points first in the project and then move on to the less important ones.

## Testing

### HTML Validation

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/).

<details>
<summary>Home Page</summary>

![Home Page]()
</details>

<details>
<summary>About Us</summary>

![About Us]()
</details>

<details>
<summary>Recipes Page</summary>

![Recipes Page]()
</details>

<details>
<summary>Recipe Details</summary>

![Recipe Details]()
</details>

<summary>Logout</summary>

![Logout]()
</details>

<details>
<summary>Sign Up</summary>

![Sign Up]()
</details>

<details>
<summary>Login</summary>

![Login]()
</details>

<details>
<summary>Recipe Update</summary>

![Recipe Update]()
</details>

<details>
<summary>Recipe Delete</summary>

![Recipe Delete]()
</details>

<details>
<summary>Comment Update</summary>

![Comment Update]()
</details>

<details>
<summary>Comment Delete</summary>

![Comment Delete]()
</details>

### CSS Validation

No errors were found when passing the CSS file through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

<details>
<summary>Result</summary>

![CSS validation results]()
</details>

### JavaScript Validation

No errors were found when passing through [Jshint](https://jshint.com/).

<details>
<summary>Result</summary>

![JavaScript validation results]()
</details>

### Python Linter Validation

All Python files was check by [CI Python Linter](https://pep8ci.herokuapp.com/).

<details>
<summary>admin.py</summary>

![Result]()
</details>

<details>
<summary>froms.py</summary>

![Result]()
</details>

<details>
<summary>models.py</summary>

![Result]()
</details>

<details>
<summary>lusobites/urls.py</summary>

![Result]()
</details>

<details>
<summary>views.py</summary>

![Result]()
</details>

<details>
<summary>settings.py</summary>

![Result]()

</details>

<details>
<summary>luso/urls.py</summary>

![Results]()
</details>

## Bugs 

### Fixed Bugs

### Unfixed bugs:

### Custom error pages

Custom Error Pages have been implemented to offer users more information about the encountered errors and to guide them back to the Blog with navigational buttons (back Home).

400 Bad Request.

403 Forbidden: It appears that you are attempting to access restricted content.

404 Not Found: The page you are searching for does not exist.

500 Internal Server Error.

## Features

### Header

![header logged out]()

![header logged in]()

**Logo**

**Navigation Bar**

### Footer

### Home Page

### User Account Pages

**Sign Up, Log in and Log out**

![sign Up, log in and log out]()

- The implementation of Django AllAuth facilitated the establishment of essential user functionalities such as Sign Up, Log In, and Log Out.

**Messages**

![messages]()

- To enhance user experience, success messages are incorporated to provide immediate feedback when users successfully log in or log out.

## Deployment - Heroku

The subsequent actions were carried out to facilitate the deployment of this page to Heroku from its corresponding GitHub repository:

### Create the Heroku App

- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labeled "New" in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next, select your region.
- Click on the Create App button.

### Attach the Postgres database

- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file

- In your workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add Cloudinary URL to env.py.
- Add the Cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url, and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR.
- Add Heroku to the ALLOWED_HOSTS list.

### Create files/directories

- Create requirements.txt file.
- Create three directories in the main directory; media, storage, and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi.

### Update Heroku Config Vars

Add the following Config Vars in Heroku:

- SECRET_KEY = yoursecretkey
- CLOUDINARY_URL = yourcloudinaryurl
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1

### Deploy

- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live and operational.

## Languages

- Python
- HTML
- CSS
- Javascript

## Frameworks - Libraries - Programs Used

- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [PostgreSQL](https://www.postgresql.org/) was used as the database for this project.
- [Heroku](https://dashboard.heroku.com/login) - was used as the cloud-based platform to deploy the site on.
- [AmIResponsive?](https://ui.dev/amiresponsive) - Used to verify the responsiveness of my website on different devices.
- [Balsamiq](https://balsamiq.com/) - Used to generate Wireframe images.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and using lighthouse.
- [Font Awesome](https://fontawesome.com/) - Used for icons in the three-reasons section.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [CI Python Linter](https://pep8ci.herokuapp.com/) - used to validate all the Python code
- [Jshint](https://jshint.com/) - used to validate javascript
- [Colormind](http://colormind.io/) - Used to create color palette.
- [Favicon](https://favicon.io/) - Used to create the favicon.
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database schema design
- [Summernote](https://summernote.org/): A WYSIWYG editor to allow users to edit their posts
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to manage Django Forms
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images
- [Bootstrap v5.3.2](https://getbootstrap.com/docs/5.3/getting-started/introduction/): CSS Framework for developing responsiveness and styling

## Credits

### Code

### Media and Content