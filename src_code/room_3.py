class Room3:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.group_of_guests = []
        self.list_of_songs = []
    
    def guest_count(self):
        return len(self.group_of_guests)
    
    def song_count(self):
        return len(self.list_of_songs)

    def check_in(self, guest):
        
        self.group_of_guests.append(guest)
    
    def check_out(self, guest):
        self.group_of_guests.remove(guest)

    def add_song(self, new_song):
        self.list_of_songs.append(new_song)