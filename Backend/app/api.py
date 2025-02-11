from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.models import (
    User,
    Role,
    Category,
    SubCategory,
    Venue,
    Event,
    Seat,
    Payment,
    Order,
    Ticket,
    UserEvent,
)
from app.crud import (
    create_user,
    get_user_by_id,
    get_user_by_email,
    get_all_users,
    delete_user,
    create_role,
    get_all_roles,
    get_role_by_id,
    delete_role,
    create_category,
    get_all_categories,
    get_category_by_id,
    delete_category,
    create_subcategory,
    get_all_subcategories,
    get_subcategory_by_id,
    delete_subcategory,
    create_venue,
    get_all_venues,
    get_venue_by_id,
    delete_venue,
    create_event,
    get_event_by_id,
    get_events,
    get_events_by_category_id,
    get_events_by_event_ids,
    delete_event,
    create_seat,
    get_all_seats,
    get_seat_by_id,
    delete_seat,
    create_payment,
    get_payment_by_id,
    delete_payment,
    create_order,
    get_order_by_id,
    delete_order,
    create_ticket,
    get_all_tickets,
    delete_ticket,
    get_ticket_by_id,
    add_user_event,
    get_user_events_by_user_id,
    update_user,
    update_role,
    update_category,
    update_subcategory,
    update_venue,
    update_event,
    update_seat,
    update_payment,
    update_order,
    update_ticket,
    update_user_event,
    get_event_sales_summary,
    get_events,
    get_users_without_tickets,
    get_events_with_low_tickets,
    get_highest_revenue_events,
)

# Initializing APIRouter for handling API routes
router = APIRouter()


# API Controller
# User APIs
# Tags are used to categorize endpoints in API documentation
@router.post("/users/", response_model=User, tags=["Users"])
def api_create_user(user: User, session: Session = Depends(get_session)):
    return create_user(session, user)


@router.post("/login")
def api_login(email: str, password: str, session=Depends(get_session)):
    user = get_user_by_email(session, email)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    if not User.verify_password(password, user.PasswordHash):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    return user


@router.get("/users/{user_id}", response_model=User, tags=["Users"])
def api_get_user(user_id: int, session: Session = Depends(get_session)):
    user = get_user_by_id(session, user_id)
    # Error handling
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users/", response_model=list[User], tags=["Users"])
def api_get_all_users(session: Session = Depends(get_session)):
    return get_all_users(session)


@router.put("/users/{user_id}", response_model=User, tags=["Users"])
def api_update_user(user_id: int, user: User, session: Session = Depends(get_session)):
    return update_user(session, user_id, user)


@router.delete("/users/{user_id}", tags=["Users"])
def api_delete_user(user_id: int, session: Session = Depends(get_session)):
    delete_user(session, user_id)
    return {"message": "User deleted successfully"}


# Role APIs
@router.post("/roles/", response_model=Role, tags=["Roles"])
def api_create_role(role: Role, session: Session = Depends(get_session)):
    return create_role(session, role)


@router.get("/roles/", response_model=list[Role], tags=["Roles"])
def api_get_all_roles(session: Session = Depends(get_session)):
    return get_all_roles(session)


@router.get("/roles/{role_id}", response_model=Role, tags=["Roles"])
def api_get_role(role_id: int, session: Session = Depends(get_session)):
    role = get_role_by_id(session, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="role not found")
    return role


@router.put("/roles/{role_id}", response_model=Role, tags=["Roles"])
def api_update_role(role_id: int, role: Role, session: Session = Depends(get_session)):
    return update_role(session, role_id, role)


@router.delete("/roles/{role_id}", tags=["Roles"])
def api_delete_role(role_id: int, session: Session = Depends(get_session)):
    delete_role(session, role_id)
    return {"message": "role deleted successfully"}


# Category APIs
@router.post("/categories/", response_model=Category, tags=["Categories"])
def api_create_category(category: Category, session: Session = Depends(get_session)):
    return create_category(session, category)


@router.get("/categories/", response_model=list[Category], tags=["Categories"])
def api_get_all_categories(session: Session = Depends(get_session)):
    return get_all_categories(session)


@router.get("/categories/{category_id}", response_model=Category, tags=["Categories"])
def api_get_category(category_id: int, session: Session = Depends(get_session)):
    category = get_category_by_id(session, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="category not found")
    return category


@router.put("/categories/{category_id}", response_model=Category, tags=["Categories"])
def api_update_category(
    category_id: int, category: Category, session: Session = Depends(get_session)
):
    return update_category(session, category_id, category)


@router.delete("/categories/{category_id}", tags=["Categories"])
def api_delete_category(category_id: int, session: Session = Depends(get_session)):
    delete_category(session, category_id)
    return {"message": "category deleted successfully"}


# SubCategory APIs
@router.post("/subcategories/", response_model=SubCategory, tags=["Sub Categories"])
def api_create_subcategory(
    subcategory: SubCategory, session: Session = Depends(get_session)
):
    return create_subcategory(session, subcategory)


@router.get(
    "/subcategories/{subcategory_id}",
    response_model=SubCategory,
    tags=["Sub Categories"],
)
def api_get_subcategory(subcategory_id: int, session: Session = Depends(get_session)):
    subcategory = get_subcategory_by_id(session, subcategory_id)
    if not subcategory:
        raise HTTPException(status_code=404, detail="subcategory not found")
    return subcategory


@router.get(
    "/subcategories/", response_model=list[SubCategory], tags=["Sub Categories"]
)
def api_get_all_subcategories(session: Session = Depends(get_session)):
    return get_all_subcategories(session)


@router.put(
    "/subcategories/{subcategory_id}",
    response_model=SubCategory,
    tags=["Sub Categories"],
)
def api_update_subcategory(
    subcategory_id: int,
    subcategory: SubCategory,
    session: Session = Depends(get_session),
):
    return update_subcategory(session, subcategory_id, subcategory)


@router.delete("/subcategories/{subcategory_id}", tags=["Sub Categories"])
def api_delete_subcategory(
    subcategory_id: int, session: Session = Depends(get_session)
):
    delete_subcategory(session, subcategory_id)
    return {"message": "subcategory deleted successfully"}


# Venue APIs
@router.post("/venues/", response_model=Venue, tags=["Venues"])
def api_create_venue(venue: Venue, session: Session = Depends(get_session)):
    return create_venue(session, venue)


@router.get("/venues/", response_model=list[Venue], tags=["Venues"])
def api_get_all_venues(session: Session = Depends(get_session)):
    return get_all_venues(session)


@router.get("/venues/{venues_id}", response_model=Venue, tags=["Venues"])
def api_get_venue(venue_id: int, session: Session = Depends(get_session)):
    venue = get_venue_by_id(session, venue_id)
    if not venue:
        raise HTTPException(status_code=404, detail="venue not found")
    return venue


@router.put("/venues/{venue_id}", response_model=Venue, tags=["Venues"])
def api_update_venue(
    venue_id: int, venue: Venue, session: Session = Depends(get_session)
):
    return update_venue(session, venue_id, venue)


@router.delete("/venues/{venue_id}", tags=["Venues"])
def api_delete_venue(venue_id: int, session: Session = Depends(get_session)):
    delete_venue(session, venue_id)
    return {"message": " venue deleted successfully"}


# Event APIs
@router.post("/events/", response_model=Event, tags=["Events"])
def api_create_event(event: Event, session: Session = Depends(get_session)):
    return create_event(session, event)


@router.get("/events", response_model=list[Event], tags=["Events"])
def api_get_events(session: Session = Depends(get_session)):
    events = get_events(session)
    if not events:
        raise HTTPException(status_code=404, detail="No events present")
    return events


@router.get("/events/{event_id}", response_model=Event, tags=["Events"])
def api_get_event(event_id: int, session: Session = Depends(get_session)):
    event = get_event_by_id(session, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.get(
    "/events/byCategory/{category_id}", response_model=list[Event], tags=["Events"]
)
def api_get_events_by_category_id(
    category_id: int, session: Session = Depends(get_session)
):
    events = get_events_by_category_id(session, category_id)
    if not events:
        raise HTTPException(status_code=404, detail="Event not found")
    return events


@router.put("/events/{event_id}", response_model=Event, tags=["Events"])
def api_update_event(
    event_id: int, event: Event, session: Session = Depends(get_session)
):
    return update_event(session, event_id, event)


@router.delete("/events/{event_id}", tags=["Events"])
def api_delete_event(event_id: int, session: Session = Depends(get_session)):
    delete_event(session, event_id)
    return {"message": "Event deleted successfully"}


# Seat APIs
@router.post("/seats/", response_model=Seat, tags=["Seats"])
def api_create_seat(seat: Seat, session: Session = Depends(get_session)):
    return create_seat(session, seat)


@router.get("/seats/", response_model=list[Seat], tags=["Seats"])
def api_get_all_seats(session: Session = Depends(get_session)):
    return get_all_seats(session)


@router.get("/seats/{seat_id}", response_model=Seat, tags=["Seats"])
def api_get_seat(seat_id: int, session: Session = Depends(get_session)):
    seat = get_seat_by_id(session, seat_id)
    if not seat:
        raise HTTPException(status_code=404, detail="seat not found")
    return seat


@router.put("/seats/{seat_id}", response_model=Seat, tags=["Seats"])
def api_update_seat(seat_id: int, seat: Seat, session: Session = Depends(get_session)):
    return update_seat(session, seat_id, seat)


@router.delete("/seats/{seat_id}", tags=["Seats"])
def api_delete_seat(seat_id: int, session: Session = Depends(get_session)):
    delete_seat(session, seat_id)
    return {"message": "seat deleted successfully"}


# Payment APIs
@router.post("/payments/", response_model=Payment, tags=["Payments"])
def api_create_payment(payment: Payment, session: Session = Depends(get_session)):
    return create_payment(session, payment)


@router.get("/payments/{payment_id}", response_model=Payment, tags=["Payments"])
def api_get_payment(payment_id: int, session: Session = Depends(get_session)):
    payment = get_payment_by_id(session, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment


@router.put("/payments/{payment_id}", response_model=Payment, tags=["Payments"])
def api_update_payment(
    payment_id: int, payment: Payment, session: Session = Depends(get_session)
):
    return update_payment(session, payment_id, payment)


@router.delete("/payments/{payment_id}", tags=["Payments"])
def api_delete_payment(payment_id: int, session: Session = Depends(get_session)):
    delete_payment(session, payment_id)
    return {"message": "payment deleted successfully"}


# Order APIs
@router.post("/orders/", response_model=Order, tags=["Orders"])
def api_create_order(order: Order, session: Session = Depends(get_session)):
    return create_order(session, order)


@router.get("/orders/{order_id}", response_model=Order, tags=["Orders"])
def api_get_order(order_id: int, session: Session = Depends(get_session)):
    order = get_order_by_id(session, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.put("/orders/{order_id}", response_model=Order, tags=["Orders"])
def api_update_order(
    order_id: int, order: Order, session: Session = Depends(get_session)
):
    return update_order(session, order_id, order)


@router.delete("/orders/{order_id}", tags=["Orders"])
def api_delete_order(order_id: int, session: Session = Depends(get_session)):
    delete_order(session, order_id)
    return {"message": "order deleted successfully"}


# Ticket APIs
@router.post("/tickets/", response_model=Ticket, tags=["Tickets"])
def api_create_ticket(ticket: Ticket, session: Session = Depends(get_session)):
    return create_ticket(session, ticket)


@router.get("/tickets/", response_model=list[Ticket], tags=["Tickets"])
def api_get_all_tickets(session: Session = Depends(get_session)):
    return get_all_tickets(session)


@router.get("/tickets/{ticket_id}", response_model=Ticket, tags=["Tickets"])
def api_get_ticket(ticket_id: int, session: Session = Depends(get_session)):
    ticket = get_ticket_by_id(session, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="ticket not found")
    return ticket


@router.put("/tickets/{ticket_id}", response_model=Ticket, tags=["Tickets"])
def api_update_ticket(
    ticket_id: int, ticket: Ticket, session: Session = Depends(get_session)
):
    return update_ticket(session, ticket_id, ticket)


@router.delete("/tickets/{ticket_id}", tags=["Tickets"])
def api_delete_ticket(ticket_id: int, session: Session = Depends(get_session)):
    delete_ticket(session, ticket_id)
    return {"message": "Ticket deleted successfully"}


# UserEvent APIs
@router.post("/user_events/", response_model=UserEvent, tags=["UserEvents"])
def api_add_user_event(user_event: UserEvent, session: Session = Depends(get_session)):
    return add_user_event(session, user_event)


@router.get(
    "/user_events/{user_id}", response_model=list[UserEvent], tags=["UserEvents"]
)
def api_get_user_events(user_id: int, session: Session = Depends(get_session)):
    return get_user_events_by_user_id(session, user_id)


@router.put(
    "/user_events/{user_id}/{event_id}", response_model=UserEvent, tags=["UserEvents"]
)
def api_update_user_event(
    user_id: int,
    event_id: int,
    user_event: UserEvent,
    session: Session = Depends(get_session),
):
    return update_user_event(session, user_id, event_id, user_event)


@router.get(
    "/event_list_by_user_id/{user_id}", response_model=list[Event], tags=["UserEvents"]
)
def api_get_event_list_by_user_id(
    user_id: int, session: Session = Depends(get_session)
):
    event_id_list = get_user_events_by_user_id(session, user_id)
    if not event_id_list:
        raise HTTPException(status_code=404, detail="No events found for this user")
    events = get_events_by_event_ids(session, event_id_list)
    if not events:
        raise HTTPException(status_code=404, detail="No events found for this user")
    return events


@router.get("/get_event_sales_summary")
def api_get_event_sales_summary(session: Session = Depends(get_session)):
    summary = get_event_sales_summary(session)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return summary


@router.get("/users_without-tickets")  ##set difference and subquery
def users_without_tickets(session=Depends(get_session)):
    users = get_users_without_tickets(session)
    return {"users": users}


@router.get("/events_low-tickets")  ##set comparision
def events_with_low_tickets(session=Depends(get_session)):
    events = get_events_with_low_tickets(session)
    return {"events": events}


@router.get("/events_highest-revenue")  ## with claus and windowing fn
def highest_revenue_events(session=Depends(get_session)):
    events = get_highest_revenue_events(session)
    return {"events": events}
