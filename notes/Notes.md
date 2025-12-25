# What is a View in Django?
  - A view in Django is a Python function or class that receives an HTTP request, processes  it, and returns an HTTP response.

 - A view is a Python function or class that:
 - Receives a request from the browser
 - Processes data (logic)
 - Returns a response (HTML, JSON, text, etc.)
 # 🔁 Django Request–Response Flow (Simple)
   - Browser → URL → View → Response → Browser
 # 🧠 What does request contain?
  - The request object includes:
  - HTTP method (GET, POST)
  - Form data ,JSON data,User info, Headers
 
 # 🧱 Types of Views in Django
   - 1️⃣ Function-Based Views (FBV)
      - def login_view(request):
          if request.method == "POST":
              return HttpResponse("Login Success")

   - 2️⃣ Class-Based Views (CBV)
      - from django.views import View
          class HomeView(View):
             def get(self, request):
                return HttpResponse("Hello")
  # What is reverse() in Django?
     - reverse() is a Django function used to generate a URL from a URL pattern name      instead of writing the URL manually.
     
     - How reverse() works (simple)
        - URL name  →  reverse()  →  actual URL
   # Why is name used in Django URLs?    (IMP)
    -  It allows referencing URLs dynamically using names instead of hard-coded paths   making applications more maintainable, reusable, and safe when URLs change.

