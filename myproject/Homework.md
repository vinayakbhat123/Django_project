## steps to create a django projects
# Step 1: Check Python installation
   - python --version
# Step 2: Create project folder
  - mkdir django_projects
  - cd django_projects
# Step 3: Create Virtual Environment (IMPORTANT)
  - python -m venv myenv
# Step 4: Activate virtual environment
  - myenv\Scripts\activate
# Step 5: Install Django
  - pip install django
  - Verify installation:
     -  django-admin --version
# Step 6: Create Django Project
  - django-admin startproject myproject
# Step 7: Go inside project folder
  - cd myproject
# Step 8: Run Development Server
  - python manage.py runserver

# Step 9 (Optional): Create Django App
  - python manage.py startapp appname 



  # step by step
   - views.py in challenges app created index view
   - created urls.py file in challenges 
      - created urlpatterns[] gave a path()
   - include("challenges.urls") in urlpatterns in path()
   - make months dynamic using <months> in urls challenges
   # - Path Converters
      - added <str:months> in urls challenges and take number to show months
   # Adding more dynamic view logic
      - created a challenges dictionary {} and make it dynamic
   # Redirects
     - check the month in challenges index key 
     - and using HttResponseRedirect('/challenges/+redirect_month)
   # Reverse Functions and URLS
    - use reverse(name_url,args) 
    - used name url in urls.py in challenges folder 
       - It eliminate the hard coding urls 
   # Returning a html
     - use <h1></h1> in HttpResponse
   # practicing URLs,Views and Dynamic View Logic
     - use <ul><li><a></a></li></ul> to display list_months using for loop
   # Summary
     - Revision
   # Adding and Registring Template
    - Create templates folder inside challenges folder
        - create challenges folder inside the templates folder
        - form from django.template.loader import render_to_string  
            - added to monthly_challenges function
        - In settings.py  in
        - dirs[
                  <!-- BASE_DIR / "challenges" / "templates" -->
        ]
     - In settings.py Go to INSTALLED_APPS 
        - put "challenges" 
   # Rendering templates
    - from django.shortcuts import render
       - used in monthly_challenges() to render challenges/challenge.html file
   # template language and variable Interpolation
     - assigning key:value pairs to challenge.html
     - render dynamic month and months_text in challenge.html 
   # Filters
     - {{ variable|title }}  => for capitalize()   => 
    -   {{}} =>  refer to openvariable and close variable
    -  {% %} => refer to block 
     - {# #} => Comment
   # 39> Django visual Studio code extension
     - add Django extension
   # 40> tags and the "for" tags
    - created index.html and used {% for in %}{% endfor %} to render months
    - used  <ul><li><a href={{month}}>{{month|title}}</a></li></ul>
   # 41> URL tag for dynamic urls 
     <!-- - used  <li><a href={% url "month-challenges" month=month %}>{{month|title}}</a></li>  -->
     - referencing URL-Name for better use eliminating hardcoded URLPath
   # 42> The "if" tag for Conditional Content
      - {% if  %}{% endif %} to display {{text}} dynamically
   # 43> Template Inheritance
    - django_projects > myprojects > templates > base.html
      - use {% block Name %} {% endblock %}
      - use {% extends Name} in index.html
      - In settings.py inside DIR [BASE_DIR / "templates" ] 
