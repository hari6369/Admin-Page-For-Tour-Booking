from django.shortcuts import render, redirect

def Login(request):
    return render(request, 'Login.html')

def Dashboard(request):
    circumference = 408.4
    progress_data = [
        {"label": "Confirmed", "percent": 95},
        {"label": "Pending", "percent": 60},
        {"label": "Cancelled", "percent": 30},
    ]
    for item in progress_data:
        item["offset"] = round(circumference * (1 - item["percent"] / 100), 2)
    return render(request, 'Dashboard.html', {"progress_data": progress_data})

def Add_Edit(request, tour_id=None):
    # Minimal placeholder: if POST, you should save data to DB.
    if request.method == "POST":
        # TODO: validate and save to DB or update existing tour
        # For now redirect to manage page
        return redirect('manage_tour')

    # If editing, you would load tour data by id and pass to template.
    context = {}
    return render(request, 'Add_Edit.html', context)

def delete_tour(request, id):
    # TODO: delete tour with given id from DB
    return redirect('manage_tour')

def View_Booking(request):
    bookings = [
        {
            "id": 1,
            "tour_name": "Grand European Tour",
            "customer_name": "Alice Johnson",
            "booking_date": "2024-06-15",
            "status": "Confirmed"
        },
        {
            "id": 2,
            "tour_name": "Asian Adventure",
            "customer_name": "Bob Smith",
            "booking_date": "2024-07-20",
            "status": "Pending"
        },
        {
            "id": 3,
            "tour_name": "African Safari",
            "customer_name": "Charlie Brown",
            "booking_date": "2024-08-05",
            "status": "Cancelled"
        },
        {
            "id": 4,
            "tour_name": "South American Expedition",
            "customer_name": "Diana Prince",
            "booking_date": "2024-09-10",
            "status": "Confirmed"
        },
        {
            "id": 5,
            "tour_name": "Australian Outback",
            "customer_name": "Ethan Hunt",
            "booking_date": "2024-10-15",
            "status": "Pending"
        }

    ]
    return render(request, 'View_Booking.html', {"bookings": bookings})

def View_Booking_Details(request):
    return render(request, 'View_Booking_Details.html')

def User_Profile(request):

    return render(request, 'User_Profile.html')

def Manage_Tour(request):
    # Replace this with real DB query later
    tours = [
        {"id": 1, "name": "Beach Getaway", "destination": "Hawaii", "price": 299.99},
        {"id": 2, "name": "Mountain Adventure", "destination": "Colorado", "price": 399.99},
        {"id": 3, "name": "City Exploration", "destination": "New York", "price": 199.99},
        {"id": 4, "name": "Cultural Tour", "destination": "Italy", "price": 499.99},
        {"id": 5, "name": "Safari Experience", "destination": "Kenya", "price": 599.99},
    ]
    return render(request, 'Manage_Tour.html', {"tours": tours})

def Logout(request):
    return redirect('login')
