class Player:
    """ Model réprésentant le joueur d'échec dasn le tournoi """

    def __init__(self, id, firstname, lastname, gender, rating):

        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.rating = int(rating)

    def __str__(self):
        return f'ID # {self.id}-{self.firstname}' \
            f'{self.last_name}-Rating #{self.rating}'

    def get_rating(self):
        return self.rating

    def get_name(self):
        return self.last_name

    def serialize(self):
        """serialiser un joueur"""
        serialized_player = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'rating': self.rating,
        }
        return serialized_player
