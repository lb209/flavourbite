from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Student, Profile

# ==================== REGISTER ====================
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "User already exists"})

        # User create karein
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Student create karein (Yahan se extra password field hata di hai)
        Student.objects.create(
            user=user,
            name=username,
            email=email
        )

        return redirect("login")

    return render(request, "register.html")


# ==================== LOGIN ====================
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        if user:
            login(request, user)
            return redirect("read")

    return render(request, "login.html")


# ==================== DASHBOARD (READ) ====================
def read(request):
    students = Student.objects.all()

    data = []
    for s in students:
        profile, _ = Profile.objects.get_or_create(student=s)
        data.append({"student": s, "profile": profile})

    return render(request, "read.html", {"data": data})


# ==================== CREATE & UPDATE ====================
def create_update(request, id=None):
    student = None
    profile = None

    if id:
        student = get_object_or_404(Student, id=id)
        profile, _ = Profile.objects.get_or_create(student=student)

    if request.method == "POST":
        # Agar naya student hai (id nahi mili URL se)
        if not student:
            user = User.objects.create_user(
                username=request.POST.get("name"),
                email=request.POST.get("email"),
                password="1234"
            )
            student = Student.objects.create(
                user=user,
                name=request.POST.get("name"),
                email=request.POST.get("email")
            )
        else:
            # FIX: Agar student pehle se majood hai (Update mode), toh us ka name aur email bhi update ho
            student.name = request.POST.get("name")
            student.email = request.POST.get("email")
            student.save()

        # Profile fetch ya create karein
        profile, _ = Profile.objects.get_or_create(student=student)

        # FIX: Age blank ka error hal karne ke liye safe check
        age_value = request.POST.get("age")
        if age_value and age_value.strip():
            profile.age = int(age_value)
        else:
            profile.age = None  # Agar khali string ho toh crash na kare balki NULL save ho

        profile.city = request.POST.get("city")
        profile.phone = request.POST.get("phone")

        # Files (Images) ko check karein
        if "image" in request.FILES:
            profile.image = request.FILES["image"]

        # Data save karein
        profile.save()

        # Dashboard par redirect karein
        return redirect("read")

    return render(request, "form.html", {"student": student, "profile": profile})


# ==================== VIEW PROFILE ====================
def profile_view(request, id):
    student = get_object_or_404(Student, id=id)
    profile = get_object_or_404(Profile, student=student)

    return render(request, "profile.html", {
        "student": student,
        "profile": profile
    })


# ==================== DELETE ====================
def delete(request, id):
    Student.objects.get(id=id).delete()
    return redirect("read")