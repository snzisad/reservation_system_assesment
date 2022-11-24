from django.http.response import JsonResponse
from .models import Rental, Reservation

def home(request):

    # Check if the database is empty or not
    # If empty, insert some dummy data first
    if Rental.objects.count() == 0:
        load_dummy_data()

    """     
     There are three ways to get the previous reservation id.

     1) Just get the previous reservation id without comparing anything
     2) Compare the current check-in date with other check-in dates and get the immediately previous one
     3) Compare the current check-in date with other checkout dates and get the immediately previous one

     Third way seemed more logical to me. So I have implented that one.
    """


    reservations = Reservation.objects.all().order_by("rental_id")
    reservation_info = []
    for single_reservation in reservations:
        prev_reservation = Reservation.objects.filter(rental = single_reservation.rental).filter(checkout__lte = single_reservation.checkin).order_by("-checkout").first()

        reservation_info.append({
            "id" : single_reservation.id,
            "rental" : single_reservation.rental.name,
            "checkin": '{:%Y-%m-%d}'.format(single_reservation.checkin),
            "checkout": '{:%Y-%m-%d}'.format(single_reservation.checkout),   
            "prev_reservation_id": prev_reservation.id if (prev_reservation != None) else "N/A" 
        })

    # quary_set = Reservation.objects.raw("SELECT A.id, A.checkin, A.checkout, "+
    #     "(SELECT B.name FROM home_rental B WHERE B.id = A.rental_id LIMIT 1) as rental_name, "+
    #     "(SELECT C.id FROM home_reservation C "+
    #     "WHERE C.rental_id = A.rental_id AND C.checkout <= A.checkin ORDER BY C.checkout DESC LIMIT 1) as prev_reservation_id "+
    #     "FROM home_reservation A ORDER BY A.rental_id")

    

    # reservation_info = []
    # for quary in quary_set:
    #     reservation_info.append({
    #         "id" : quary.id,
    #         "rental" : quary.rental_name,
    #         "checkin": '{:%Y-%m-%d}'.format(quary.checkin),
    #         "checkout": '{:%Y-%m-%d}'.format(quary.checkout),   
    #         "prev_reservation_id": quary.prev_reservation_id if (quary.prev_reservation_id != None) else "N/A" 
    #     })

    return JsonResponse(reservation_info, safe=False)


def load_dummy_data():
    rental_list = [Rental(name = "Rental-1"), Rental(name = "Rental-2")]
    Rental.objects.bulk_create(rental_list)

    rental_object_list = [Rental.objects.get(name = "Rental-1"), Rental.objects.get(name = "Rental-2")]
    reservation_list = [
        Reservation(rental = rental_object_list[0], checkin = "2022-01-01", checkout = "2022-01-13"),
        Reservation(rental = rental_object_list[0], checkin = "2022-01-20", checkout = "2022-02-10"),
        Reservation(rental = rental_object_list[0], checkin = "2022-02-20", checkout = "2022-03-10"),
        Reservation(rental = rental_object_list[1], checkin = "2022-01-02", checkout = "2022-01-20"),
        Reservation(rental =  rental_object_list[1], checkin = "2022-01-20", checkout = "2022-02-11")
    ]
    Reservation.objects.bulk_create(reservation_list)
