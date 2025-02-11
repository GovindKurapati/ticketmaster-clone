from datetime import datetime
from sqlmodel import Session, select, text, func
from typing import List, Optional
from fastapi import HTTPException, status
from datetime import datetime
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


# Common function to check required fields
def validate_required_fields(obj, required_fields: List[str]):
    missing_fields = [
        field for field in required_fields if getattr(obj, field, None) is None
    ]
    if missing_fields:
        # Exception Handling is done here
        # Raise an HTTP 422 error if required fields are missing, detailing which fields are absent
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Missing required fields: {', '.join(missing_fields)}",
        )


# CRUD Operations for User
# CREATE
def create_user(session: Session, user: User) -> User:
    # validations
    validate_required_fields(
        user,
        [
            "Email",
            "FirstName",
            "LastName",
            "DateOfBirth",
            "PasswordHash",
        ],
    )
    existing_user = session.exec(select(User).where(User.Email == user.Email)).first()
    if existing_user:
        raise ValueError("User with this email already exists.")
    if not user.RoleID:
        user.RoleID = 1
    if isinstance(user.DateOfBirth, str):
        user.DateOfBirth = datetime.strptime(user.DateOfBirth, "%Y-%m-%d").date()
    if user.CreatedAt == "":
        user.CreatedAt = None
    if user.UpdatedAt == "":
        user.UpdatedAt = None

    user.PasswordHash = User.hash_password(user.PasswordHash)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


# READ
def get_user_by_id(session: Session, user_id: int) -> Optional[User]:
    user = session.get(User, user_id)
    # Exception Handling
    # To raise an exception if the user is not found in the database
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


def get_user_by_email(session: Session, email: str) -> User:
    statement = select(User).where(User.Email == email)
    return session.exec(statement).first()


def get_all_users(session: Session) -> List[User]:
    return session.exec(select(User)).all()


# UPDATE
def update_user(session: Session, user_id: int, user_data: User) -> User:
    validate_required_fields(user_data, ["UserID"])
    user = session.get(User, user_id)
    # Exception Handling
    # To raise an exception if the user is not found in the database
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)
    session.commit()
    session.refresh(user)
    return user


# DELETE
def delete_user(session: Session, user_id: int) -> None:
    user = get_user_by_id(session, user_id)
    session.delete(user)
    session.commit()


# CRUD Operations for Role
def create_role(session: Session, role: Role) -> Role:
    validate_required_fields(role, ["Name", "RoleID"])
    session.add(role)
    session.commit()
    session.refresh(role)
    return role


def get_all_roles(session: Session) -> List[Role]:
    return session.exec(select(Role)).all()


def get_role_by_id(session: Session, role_id: int) -> Optional[Role]:
    role = session.get(Role, role_id)
    # Exception Handling
    # To raise an exception if the role is not found in the database
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Role not found"
        )
    return role


def update_role(session: Session, role_id: int, role_data: Role) -> Role:
    role = session.get(Role, role_id)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Role not found"
        )
    for key, value in role_data.dict(exclude_unset=True).items():
        setattr(role, key, value)
    session.commit()
    session.refresh(role)
    return role


def delete_role(session: Session, role_id: int) -> None:
    role = get_role_by_id(session, role_id)
    session.delete(role)
    session.commit


# CRUD Operations for Category
def create_category(session: Session, category: Category) -> Category:
    validate_required_fields(category, ["CategoryID", "Name"])
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


def get_all_categories(session: Session) -> List[Category]:
    return session.exec(select(Category)).all()


def get_category_by_id(session: Session, category_id: int) -> Optional[Category]:
    category = session.get(Category, category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="category not found"
        )
    return category


def update_category(
    session: Session, category_id: int, category_data: Category
) -> Category:
    category = session.get(Category, category_id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )
    for key, value in category_data.dict(exclude_unset=True).items():
        setattr(category, key, value)
    session.commit()
    session.refresh(category)
    return category


def delete_category(session: Session, category_id: int) -> None:
    category = get_category_by_id(session, category_id)
    session.delete(category)
    session.commit()


# CRUD Operations for SubCategory
def create_subcategory(session: Session, subcategory: SubCategory) -> SubCategory:
    validate_required_fields(subcategory, ["SubCategoryID", "CategoryID", "Name"])
    session.add(subcategory)
    session.commit()
    session.refresh(subcategory)
    return subcategory


def get_all_subcategories(session: Session) -> List[SubCategory]:
    return session.exec(select(SubCategory)).all()


def get_subcategory_by_id(
    session: Session, subcategory_id: int
) -> Optional[SubCategory]:
    subcategory = session.get(SubCategory, subcategory_id)
    if not subcategory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="subcategory not found"
        )
    return subcategory


def update_subcategory(
    session: Session, subcategory_id: int, subcategory_data: SubCategory
) -> SubCategory:
    subcategory = session.get(SubCategory, subcategory_id)
    if not subcategory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="SubCategory not found"
        )
    for key, value in subcategory_data.dict(exclude_unset=True).items():
        setattr(subcategory, key, value)
    session.commit()
    session.refresh(subcategory)
    return subcategory


def delete_subcategory(session: Session, subcategory_id: int) -> None:
    subcategory = get_subcategory_by_id(session, subcategory_id)
    session.delete(subcategory)
    session.commit()


# CRUD Operations for Venue
def create_venue(session: Session, venue: Venue) -> Venue:
    validate_required_fields(
        venue,
        ["VenueID", "Name", "Location", "Capacity", "PhoneNumber", "Email", "Type"],
    )
    session.add(venue)
    session.commit()
    session.refresh(venue)
    return venue


def get_all_venues(session: Session) -> List[Venue]:
    return session.exec(select(Venue)).all()


def get_venue_by_id(session: Session, venue_id: int) -> Optional[Venue]:
    venue = session.get(Venue, venue_id)
    if not venue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="venue not found"
        )
    return venue


def update_venue(session: Session, venue_id: int, venue_data: Venue) -> Venue:
    venue = session.get(Venue, venue_id)
    if not venue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Venue not found"
        )
    for key, value in venue_data.dict(exclude_unset=True).items():
        setattr(venue, key, value)
    session.commit()
    session.refresh(venue)
    return venue


def delete_venue(session: Session, venue_id: int) -> None:
    venue = get_venue_by_id(session, venue_id)
    session.delete(venue)
    session.commit()


# CRUD Operations for Event
def create_event(session: Session, event: Event) -> Event:
    validate_required_fields(
        event,
        ["EventID", "Name", "Date", "Status", "TotalTickets", "CategoryID", "VenueID"],
    )
    session.add(event)
    session.commit()
    session.refresh(event)
    return event


def get_events(session: Session):
    statement = select(Event)
    event = session.exec(statement)
    return event.all()


def get_event_by_id(session: Session, event_id: int) -> Optional[Event]:
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found"
        )
    return event


def get_events_by_category_id(session: Session, category_id: int) -> List[Event]:
    statement = select(Event).where(Event.CategoryID == category_id)
    events = session.exec(statement).all()
    if not events:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No events found for this category",
        )
    return events


def update_event(session: Session, event_id: int, event_data: Event) -> Event:
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found"
        )
    for key, value in event_data.dict(exclude_unset=True).items():
        setattr(event, key, value)
    session.commit()
    session.refresh(event)
    return event


def delete_event(session: Session, event_id: int) -> None:
    event = get_event_by_id(session, event_id)
    session.delete(event)
    session.commit()


def get_events_by_event_ids(session: Session, event_id_list: List[int]) -> List[Event]:
    statement = select(Event).where(
        Event.EventID.in_(event_id_list)
    )  # set membership query
    events = session.exec(statement).all()
    return events


# CRUD Operations for Seat
def create_seat(session: Session, seat: Seat) -> Seat:
    validate_required_fields(seat, ["SeatID", "SeatNumber", "VenueID"])
    session.add(seat)
    session.commit()
    session.refresh(seat)
    return seat


def get_all_seats(session: Session) -> List[Seat]:
    return session.exec(select(Seat)).all()


def get_seat_by_id(session: Session, seat_id: int) -> Optional[Seat]:
    seat = session.get(seat, seat_id)
    if not seat:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Seat not found"
        )
    return seat


def update_seat(session: Session, seat_id: int, seat_data: Seat) -> Seat:
    seat = session.get(Seat, seat_id)
    if not seat:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Seat not found"
        )
    for key, value in seat_data.dict(exclude_unset=True).items():
        setattr(seat, key, value)
    session.commit()
    session.refresh(seat)
    return seat


def delete_seat(session: Session, seat_id: int) -> None:
    seat = get_seat_by_id(session, seat_id)
    session.delete(seat)
    session.commit()


# CRUD Operations for Payment
def create_payment(session: Session, payment: Payment) -> Payment:
    validate_required_fields(
        payment, ["PaymentID", "PaymentMethod", "Status", "Amount"]
    )
    session.add(payment)
    session.commit()
    session.refresh(payment)
    return payment


def get_payment_by_id(session: Session, payment_id: int) -> Optional[Payment]:
    payment = session.get(Payment, payment_id)
    if not payment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found"
        )
    return payment


def update_payment(session: Session, payment_id: int, payment_data: Payment) -> Payment:
    payment = session.get(Payment, payment_id)
    if not payment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found"
        )
    for key, value in payment_data.dict(exclude_unset=True).items():
        setattr(payment, key, value)
    session.commit()
    session.refresh(payment)
    return payment


def delete_payment(session: Session, payment_id: int) -> None:
    payment = get_payment_by_id(session, payment_id)
    session.delete(payment)
    session.commit()


# CRUD Operations for Order
def create_order(session: Session, order: Order) -> Order:
    validate_required_fields(order, ["OrderID", "TotalAmount", "PaymentID"])
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


def get_order_by_id(session: Session, order_id: int) -> Optional[Order]:
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
        )
    return order


def update_order(session: Session, order_id: int, order_data: Order) -> Order:
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
        )
    for key, value in order_data.dict(exclude_unset=True).items():
        setattr(order, key, value)
    session.commit()
    session.refresh(order)
    return order


def delete_order(session: Session, order_id: int) -> None:
    order = get_order_by_id(session, order_id)
    session.delete(order)
    session.commit()


# CRUD Operations for Ticket
def create_ticket(session: Session, ticket: Ticket) -> Ticket:
    validate_required_fields(
        ticket, ["TicketID", "Number", "Amount", "OrderID", "SeatID"]
    )
    session.add(ticket)
    session.commit()
    session.refresh(ticket)
    return ticket


def get_all_tickets(session: Session) -> List[Ticket]:
    return session.exec(select(Ticket)).all()


def get_ticket_by_id(session: Session, ticket_id: int) -> Optional[Ticket]:
    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="ticket not found"
        )
    return ticket


def update_ticket(session: Session, ticket_id: int, ticket_data: Ticket) -> Ticket:
    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Ticket	not found"
        )
    for key, value in ticket_data.dict(exclude_unset=True).items():
        setattr(ticket, key, value)
    session.commit()
    session.refresh(ticket)
    return ticket


def delete_ticket(session: Session, ticket_id: int) -> None:
    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found"
        )
    session.delete(ticket)
    session.commit()


# CRUD Operations for UserEvent (link between Users and Events)
def add_user_event(session: Session, user_event: UserEvent) -> UserEvent:
    validate_required_fields(user_event, [])
    session.add(user_event)
    session.commit()
    session.refresh(user_event)
    return user_event


def get_user_events_by_user_id(session: Session, user_id: int) -> List[UserEvent]:
    statement = select(UserEvent).where(UserEvent.UserID == user_id)
    return session.exec(statement).all()


def update_user_event(
    session: Session, user_id: int, event_id: int, user_event_data: UserEvent
) -> UserEvent:
    user_event = session.get(UserEvent, (user_id, event_id))
    if not user_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="UserEvent not found"
        )

    for key, value in user_event_data.dict(exclude_unset=True).items():
        setattr(user_event, key, value)

    session.commit()
    session.refresh(user_event)
    return user_event


def get_event_sales_summary(session: Session):
    query = """
        SELECT user.FirstName,
               user.LastName,
               event.Name        AS EventName,
               category.Name     AS Category,
               SUM(ticket.Amount) AS TotalSales
        FROM  ticket 
        JOIN `order` ON ticket.OrderID = `order`.OrderID
               JOIN user ON `order`.UserID = user.UserID
               JOIN userevent ON userevent.UserID = user.UserID
               JOIN event ON userevent.EventID = event.EventID
               JOIN category ON event.CategoryID = category.CategoryID
        GROUP  BY ROLLUP(user.FirstName, user.LastName, event.Name, category.Name);
        """
    summary = session.exec(text(query))
    sales_summary = []
    for row in summary.fetchall():
        sales_summary.append({"firstname": row[0],
                "lastname": row[1],
                "event_name": row[2],
                "category": row[3],
                "total_sales": row[4]
                })
    return sales_summary

def get_events_with_low_tickets(session: Session):
    query = select(Event).where(Event.AvailableTickets < (Event.TotalTickets * 0.1))##set comparision
    result = session.exec(query).all()
    if not result:
        raise HTTPException(status_code=404,detail="No such event found")
    return result

def get_highest_revenue_events(session: Session): ## with claus and windowing fn
    with_event_revenue = (
        select(
            Event.EventID,
            Event.Name,
            func.sum(Ticket.Amount).label("total_revenue")
        )
        .join(Event, Ticket.OrderID == Event.EventID)
        .group_by(Event.EventID, Event.Name)
        .cte("event_revenue")
    )
    query = (
        select(with_event_revenue)
        .where(with_event_revenue.c.total_revenue == select(func.max(with_event_revenue.c.total_revenue)))
    )
    result = session.exec(query).all()
    if not result:
        raise HTTPException(status_code=404,detail="something went wrong")
    return result

def get_users_without_tickets(session: Session): ##set difference and subquery
    subquery = (
        select(Order.UserID)
        .join(Ticket, Ticket.OrderID == Order.OrderID)
        .distinct()
    )
    query = select(User).where(User.UserID.not_in(subquery))
    result= session.exec(query).all()
    if not result:
        raise HTTPException(status_code=404,detail="there are no such users")
    return result