


class Room:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.reservations = {}  # Dictionary to store reservations

    def check_availability(self, start_time, end_time):
        # Logic to check room availability for the given time slot
        for slot in self.reservations:
            if not (end_time <= slot[0] or start_time >= slot[1]):
                return False  # Room not available for this time slot
        return True  # Room available for the time slot

    def book_room(self, start_time, end_time, user, purpose):
        if self.check_availability(start_time, end_time):
            self.reservations[(start_time, end_time)] = {'user': user, 'purpose': purpose}
            self.notify_booking(user, start_time, end_time)
            return True  # Booking successful
        else:
            return False  # Room not available for booking

    def notify_booking(self, user, start_time, end_time):
        # Logic to send a notification to the user about the booking
        print(f"Notification sent to {user} for booking room {self.room_number} from {start_time} to {end_time}")


class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email


# Usage example:
if __name__ == "__main__":
  
    room101 = Room("101", 20) 

  
    user1 = User(1, "Alice", "alice@example.com")
    user2 = User(2, "Bob", "bob@example.com")

   
    booking_success = room101.book_room("2023-12-24 10:00", "2023-12-24 12:00", user1, "Team meeting")
    if booking_success:
        print("Room booked successfully!")
    else:
        print("Room not available for booking at this time.")

    
    booking_attempt = room101.book_room("2023-12-24 11:00", "2023-12-24 13:00", user2, "Presentation")
    if booking_attempt:
        print("Room booked successfully!")
    else:
        print("Room not available for booking at this time.")
