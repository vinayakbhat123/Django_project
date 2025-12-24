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