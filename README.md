![LUSO Bites logo](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712002531/luso_bites_logo_rvmr0h.png)

# Welcome Luso Bites, 

Your culinary haven for exploring and savoring the rich gastronomic tradition of Portugal. In this space, embark on a journey of authentic aromas and flavors where I share delightful recipes capturing the essence of Portuguese cuisine. From classic dishes to contemporary interpretations, LusoBites is a celebration of a passion for Portuguese cooking, inviting you to experience the magic in every bite. Discover Portugal's culinary heritage, one delicious morsel at a time.

Live Blog- [LUSO Bites](https://luso-bites-9e7b470f6cac.herokuapp.com/)

![The website](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712052662/Captura_de_ecra%CC%83_2024-04-02_a%CC%80s_12.07.45_rxneik.png)

## Table of content

- [Welcome Luso Bites,](#welcome-luso-bites)
  - [Table of content](#table-of-content)
  - [User Experience (UX)](#user-experience-ux)
    - [User Stories](#user-stories)
    - [Design](#design)
      - [Blog Colour](#blog-colour)
      - [Images](#images)
      - [Fonts](#fonts)
      - [Wireframes](#wireframes)
  - [Agile Methodology](#agile-methodology)
  - [Testing](#testing)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Linter Validation](#python-linter-validation)
  - [Manual Testing](#manual-testing)
    - [Site Navigation](#site-navigation)
    - [About Page](#about-page)
    - [Recipes Page](#recipes-page)
    - [Recipe Details Page](#recipe-details-page)
    - [Django All Auth Pages](#django-all-auth-pages)
  - [Bugs](#bugs)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed bugs:](#unfixed-bugs)
    - [Custom error pages](#custom-error-pages)
  - [Features](#features)
    - [Header](#header)
    - [Footer](#footer)
    - [Home Page](#home-page)
    - [About Pages](#about-pages)
    - [Recipes Pages](#recipes-pages)
    - [Recipe blog Pages](#recipe-blog-pages)
  - [Deployment - Heroku](#deployment---heroku)
    - [Create the Heroku App](#create-the-heroku-app)
    - [Attach the Postgres database](#attach-the-postgres-database)
    - [Prepare the environment and settings.py file](#prepare-the-environment-and-settingspy-file)
    - [Create files/directories](#create-filesdirectories)
    - [Update Heroku Config Vars](#update-heroku-config-vars)
    - [Deploy](#deploy)
  - [Comments](#comments)
  - [Languages](#languages)
  - [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  - [Credits](#credits)
    - [Code](#code)
    - [Media and Content](#media-and-content)


## User Experience (UX)

A visitor to our blog can be an amateur in the kitchen or even a professional to increase their knowledge of Portuguese cuisine. They are eager to expand and enrich their recipe collection or simply share them with others.

### User Stories

### Design

#### Blog Colour

![Colour Palette](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712003287/color_palett_rrqj2w.png)

Given that the core of my platform is centered on the world of Portuguese cuisine, I opted for an immaculate white background, accompanied by green details (thus representing the vivid color of nature), and reds (thus representing Portugal).

#### Images

The web app has no fixed images. All the images is uploaded.

#### Fonts

The main font used for the body is the elegant Orienta font. The logo, recipes titles and footer feature the Sigmar font.

#### Wireframes

<details>
<summary>Home Page</summary>

![Home Page](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044584/wireframe_home_web_a9ioyb.png)
</details>

<details>
<summary>Home Page Mobile</summary>

![Home Page Mobile](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044567/wireframe_home_mobile_mrrmqs.png)
</details>

<details>
<summary>About</summary>

![About](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044584/wireframes_about_web_kvonpk.png)
</details>

<details>
<summary>About Mobile</summary>

![About Mobile](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044563/wireframe_about_mobile_fvvthm.png)
</details>

<details>
<summary>The Recipes</summary>

![The Recipes](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044585/wireframe_recipes_web_gxszom.png)

</details>

<details>
<summary>The Recipes Mobile</summary>

![The Recipes Mobile](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044575/wireframe_recipe_mobile_ffbaph.png)

</details>


## Agile Methodology

To handle the development process using an agile approach, we use GitHub projects. You can check the project board [here](https://github.com/users/Goncalves95/projects/3) for reference.

Each User Story is called a title and has its own points to reach so that point can be said to be closed. It is assigned to a person responsible for developing it. And with the labels so that we can focus on the most important points first in the project and then move on to the less important ones.

## Testing

### HTML Validation

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/).

<details>
<summary>Home Page</summary>

![Home Page](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712051930/html_validator_home_fmh6dk.png)
</details>

<details>
<summary>About Page</summary>

![About Us](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712051926/html_validator_about_f30gsd.png)
</details>

<details>
<summary>Recipes Page</summary>

![Recipes Page](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712051938/html_validator_recipes_qruo2n.png)
</details>

<summary>Logout</summary>

![Logout](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712051934/html_validator_login_jmyjsx.png)
</details>

<details>
<summary>Sign Up</summary>

![Sign Up](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712051934/html_validator_login_jmyjsx.png)
</details>

<details>
<summary>Login</summary>

![Login](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712051934/html_validator_login_jmyjsx.png)
</details>

<details>
<summary>Recipe Update</summary>
</details>

### CSS Validation

No errors were found when passing the CSS file through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

<details>
<summary>Result</summary>

![CSS validation results](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712003288/css_validator_gjw7kj.png)
</details>

### JavaScript Validation

No errors were found when passing through [Jshint](https://jshint.com/).

<details>
<summary>Result</summary>

![JavaScript validation results](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712003290/javascript_validator_zczikt.png)
</details>

### Python Linter Validation

All Python files was check by [CI Python Linter](https://pep8ci.herokuapp.com/).

<details>
<summary>manage.py</summary>

![Result](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044443/python_manage_validator_joclbq.png)
</details>

<details>
<summary>models.py</summary>

![Result](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044459/python_veric_models_ethlbu.png)
</details>

<details>
<summary>about/models.py</summary>

![Result](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044446/python_models_about_validator_q5hhkp.png)
</details>

<details>
<summary>lusobites/urls.py</summary>

![Result](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044440/python_blog_urls_validator_uytiej.png)
</details>

<details>
<summary>views.py</summary>

![Result](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044466/python_views_validator_xvcz2x.png)
</details>

<details>
<summary>about/views.py</summary>

![Result](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044463/python_views_about_validator_n3unpy.png)
</details>

<details>
<summary>settings.py</summary>

![Result](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044449/python_settings_validator_optfhf.png)

</details>

<details>
<summary>luso/urls.py</summary>

![Results](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044456/python_urls_validator_vfaa5b.png)
</details>

<details>
<summary>about/luso/urls.py</summary>

![Results](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044452/python_urls_about_validator_eydrqd.png)
</details>

## Manual Testing

### Site Navigation
| Element               | Action     | Expected Result                    | Pass/Fail |
|-----------------------|------------|------------------------------------|-----------|
| **NavBar**            |            |                                    |           |
| Site Name (logo area) | Click      | Redirect to home                   |     Pass      |
| Home Link             | Click      | Redirect to home                   |      Pass     |
| About Us Link        | Click      | Open About Us page                |     Pass      |
| Recipes Link          | Click      | Open Gallery Page                 |     Pass      |
| Login Link          | Click      | Open Login Page                 |      Pass     |
| Sign Up Link          | Click      | Open Sign Up Page                 |     Pass      |
| Logout Link          | Click      | Open Sign Up Page                 |     Pass      |

### About Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
| Picture About          | Display  | Showing the picture from data base |      Pass     |
| Info text | Display | Showing information about from data base |     Pass      |
| Fill up the form | Click | Showing message submisson sucess |     Fail      |
| Fill up the form | Click | Send the information to data base |     Pass      |
| Fill up the form | Click | Missing information for fill up apear a message for fill up the fields |     Pass      |

### Recipes Page
| Element     | Action                  | Expected Result                                                                         | Pass/Fail |
|-------------|-------------------------|-----------------------------------------------------------------------------------------|-----------|
| Recipe Card | Display correct content | Display correct image, recipe title, slug and artist from data base                    |     Pass      |
| recipe Card | Click                   | Clicking on recipe title or slug card takes you to the correct recipe's detail page. |     Pass      |
| Recipe Card | Pagination              | Site will paginate 6 recipes cards to page                                       |     Pass      |

### Recipe Details Page
| Element                        | Action              | Expected Result                                                                                                         | Pass/Fail |
|--------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------|-----------|
| Recipe Content               | Display             | Display correct Recipe image, title, author, description (ingredients and method), and comments                                                |     Pass      |
| Like button (Outline)          | Click               | Clicking the outlined heart changes it to a solid heart                                                                 |     Pass      |
| Like button (Solid)            | Click               | Clicking the solid heart changes it back to an outlined heart                                                           |      Pass     |
| Like button                    | Display             | Button only clickable if user in session                                                                                  |    Pass       |
| User Comments                  | Display             | Displays correct name, date, time, and comment body                                                                    |     Pass      |
| User Comments                  | Display             | Comments are ordered oldest to newest                                                                                   |     Pass      |
| User Comments                  | Display             | Comments that wainting to be aproved dont show for the normal user (just for admin and the author user)                                          |     Pass      |
| Update comment button          | Display             | Button only visible if user is the comment author                                                                       |     Pass      |
| Update comment button          | Click               | Change the comment field and buttom to update                                                                                        |    Pass       |
| Update comment submit button   | Click               | Form submit - page updates and comment displays in comments section with correct content                                |     Pass      |
| Update comment submit button   | Click               | Success message appears informing the user that the comment has been updated                                            |     Fail     |
| Update comment submit button   | Click               | Success message fades after 3 seconds                                                                                   |     Fail      |
| Cancel update comment button   | Click               | Redirects the user back to the recipe detail page                                                                   |      Pass     |
| Delete comment button          | Display             | Button only visible if the user is the comment author                                                                   |     Pass      |
| Delete comment button          | Click               | Opens delete comment confirmation page                                                                                  |     Pass      |
| Confirm delete button          | Click               | Comment is removed from the comment section                                                                             |     Pass      |
| Confirm delete button          | Click               | Success message appears informing the user that the comment has been deleted                                            |    Fail     |
| Confirm delete button          | Click               | Success message fades after 3 seconds                                                                                   |    Fail     |
| Confirm delete button          | Click               | Redirects the user back to the recipe detail page                                                                   |     Pass      |
| Cancel delete button           | Click               | Redirects the user back to the recipe detail page                                                                   |      Pass     |
| Add comment Form               | Display             | Form only visible if user is loged in                                                                                    |     Pass      |
| Add comment Form submit button | Leave empty         | On submit: form won't submit                                                                                            |     Pass      |
| Add comment Form submit button | Leave empty         | Error message displays                                                                                                  |     Pass      |
| Add comment Form submit button | Filled in           | Form submit - page updates and comment displays in the comments section with correct content                            |     Pass      |
| Add comment Form submit button | Click               | Success message appears informing the user that the comment has been added                                              |     Fail      |
| Add comment Form submit button | Click               | Success message fades after 3 seconds                                                                                   |     Fail     |

### Django All Auth Pages

| Element       | Action | Expected Result                                                                                                        | Pass/Fail |
|---------------|--------|------------------------------------------------------------------------------------------------------------------------|-----------|
| **Sign Up**        |                     |                                                                |           |
| Log in link        | Click               | Redirect to the login page                                     |     Pass      |
| Username field     | Leave empty         | On submit: form won't submit                                   |      Pass     |
| Username field     | Insert correct format | On submit: form submit                                         |     Pass      |
| Username field     | Insert duplicate username | On submit: form won't submit                              |      Pass     |
| Email field        | Insert incorrect format | On submit: form won't submit                               |      Pass     |
| Email field        | Insert correct format | On submit: form submit                                         |     Pass      |
| Email field        | Leave empty         | On submit: form submit                                         |     Pass      |
| Email field        | Insert duplicate email | On submit: form won't submit                                   |     Pass      |
| Password field     | Insert incorrect format | On submit: form won't submit                                   |    Pass       |
| Password field     | Passwords don't match | On submit: form won't submit                                   |     Pass      |
| Password field     | Insert correct format and passwords match | On submit: form submit                    |     Pass      |
| Sign Up button(form valid) | Click        | Form submit                                                    |      Pass     |
| Sign Up button(form valid) | Click        | Redirect to the home page                                      |     Pass      |
| Sign Up button(form valid) | Click        | Success message confirming login appears                      |     Fail     |
| Sign Up button(form valid) | Click        | Success message fades after 3 seconds                          |     Fail    |
| **Log in**         |                     |                                                                |           |
| Sign up link       | Click               | Redirect to the sign-up page                                   |     Pass      |
| Username field     | Leave empty         | On submit: form won't submit                                   |      Pass     |
| Username field     | Insert wrong username | On submit: form won't submit                                   |     Pass      |
| Password field     | Leave empty         | On submit: form won't submit                                   |     Pass      |
| Password field     | Insert wrong password | On submit: form won't submit                                   |    Pass       |
| Login button(form valid) | Click         | Form submit                                                    |      Pass     |
| Login button(form valid) | Click         | Redirect to the page where user logged in from                                     |     Pass      |
| Login button(form valid) | Click         | Success message confirming login appears                      |     Fail     |
| Login button(form valid) | Click         | Success message fades after 3 seconds                          |      Fail     |
| **Log Out**        |                     |                                                                |           |
| Logout button      | Click               | Redirect to the homepage                                       |     Pass      |
| Logout button      | Click               | Success message confirming log out appears                     |      Fail     |
| Logout button      | Click               | Success message fades after 3 seconds                         |     Fail      |


## Bugs 

### Fixed Bugs
- Transporting the static files to heroku. helping follow the steps on [djangoproject](https://docs.djangoproject.com/en/4.2/howto/static-files/)

### Unfixed bugs:
- Search Field:
- I couldn't get the recipe/ingredient search field to work so I decided to remove it. I followed several tutorials to try to resolve it, to no avail. I did it in the models in the views, html page and urls, it worked, opening the html page with the search text but I couldn't get it to search for the recipe and pull it from the database.
- The messages appeared until I made a new model. After that I couldn't get them to appear to the user. They are being made by the system but do not appear visible.

### Custom error pages

Custom Error Pages have been implemented to offer users more information about the encountered errors and to guide them back to the Blog with navigational buttons (back Home).

400 Bad Request.

403 Forbidden: It appears that you are attempting to access restricted content.

404 Not Found: The page you are searching for does not exist.

500 Internal Server Error.

## Features

### Header

![header logged in](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044502/nav_bar_logedin_web_npoges.png)

![header logged out](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044508/not_logedin_web_lqpkhd.png)

**Logo**
![Logo](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044424/nav_mobile_ok8xtj.png)

**Navigation Bar**
![Navigation Bar](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044502/nav_bar_logedin_web_npoges.png)
![Navigation Bar Mobile](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044422/nav_mobile_-_co%CC%81pia_xkrloc.png)

### Footer
![Footer](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044482/footer_web_bx5dhw.png)

### Home Page
![Home Page](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044412/home_page_web_v4nf1l.png)
![Home Page Mobile](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044415/homr_page_mobile_canb6c.png)

### About Pages
![About Page](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044470/about_web_arilza.png)
![About Page Mobile](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044410/about_page_mobile_jft01j.png)

### Recipes Pages
![Recipes](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044558/recipes_web_sr2tvn.png)
![Recipes Mobile](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044435/recipes_page_mobile_ityiqc.png)

### Recipe blog Pages
![Blog Post](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044522/recipe_web_fsvlhf.png)
![Blog Post Mobile](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044433/recipe_page_mobile_yhgep9.png)

**Sign Up, Log in and Log out**
![sign Up, log in and log out](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044514/sign_up_web_vgvysi.png)
![sign Up, log in and log out Mobile](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044419/log_page_mobile_mpnasj.png)

- The implementation of Django AllAuth facilitated the establishment of essential user functionalities such as Sign Up, Log In, and Log Out.

**Messages**

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

## Comments
<details>
<summary>Waiting to aprovel</summary>

![Comment waiting for aprovel](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044477/comment_area_web_awotl6.png)
</details>

<details>
<summary>Update comment</summary>

![Update Comment](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044480/comment_box_edit_web_i81cnm.png)
</details>

<details>
<summary>Delete message</summary>

![Message to delete comment](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712044498/model_delete_web_oo8j0c.png)
</details>

<details>
<summary>Loged in</summary>

![Comments with loged in](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712053058/comments_nmckpf.png)
</details>

<details>
<summary>Loged out</summary>

![Comments Loged out](https://res.cloudinary.com/drkrtxaiq/image/upload/v1712053110/Captura_de_ecra%CC%83_2024-04-02_a%CC%80s_12.17.58_mhgkso.png)
</details>


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
Inspiration on tho follwing ptojects:
- [I Think Therefore I Blog](https://github.com/Code-Institute-Solutions/blog/blob/main/08_templates/01_base_template/base.html) - Following the bases for make a blog in django and creat a data base.
- [Thorin and Company](https://thorin-and-company-nando95-241442fa6743.herokuapp.com/) - Inspirations to styling and form.
- [Masterpiece](https://masterpiece23-cbdad7ea4f9e.herokuapp.com/) - Inspiration from Joonas Timlin.

### Media and Content
- [GoodFood](https://www.bbcgoodfood.com/) - Used to make the recipes and pictures.
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database schema design.
- [PixaBay](https://pixabay.com/pt/), [Unsplash](https://unsplash.com/pt-br) - Some fotos and pictures for the blog.

[def]: #layout
[def2]: #live-website