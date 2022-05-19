from Models.classes import Player
from Models.classes import Round
from Models.classes import Match


def get_matches(players, adversaires):
    """recursive function to get matches for round 2 and more"""
    if len(players) % 2 == 1:
        return []
    if len(players) == 0:
        return []
    first_player = players[0]
    for player in players[1:]:
        if not player[0] in adversaires[first_player[0]]:
            pair = (first_player, player)
            remaining_players = players[1:]
            remaining_players.remove(player)
            pairs = get_matches(remaining_players, adversaires)
            if pairs is not None:
                return [pair] + pairs


class Tournament:
    """ Modele réprésentant un tournoi"""

    def __init__(
        self, id, name, date, time_control, description,
        total_number_of_rounds=4, continu_round=1,
        players=None, status='initialisation',
        list_of_rounds=None, scores=None, adversaires=None
    ):

        if adversaires is not None:
            adversaires = {}
        if scores is not None:
            scores = {}
        if players is not None:
            players = []
        if list_of_rounds is not None:
            list_of_rounds = []

        self.id = id
        self.name = name
        self.date = date
        self.time_control = time_control
        self.description = description
        self.total_number_of_rounds = total_number_of_rounds
        self.continu_round = continu_round
        self.players = players
        self.status = status
        self.list_of_rounds = list_of_rounds
        self.scores = scores
        self.adversaires = adversaires

    def __str__(self):
        return f'{self.name}'

    def serialize(self):
        """sérialiser le tournoi"""
        seliazed_tournament = {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'time_control': self.time_control,
            'description': self.description,
            'total_number_of_rounds': self.total_number_of_rounds,
            'ongoing_round': self.continu_round,
            'palyers': self.players,
            'status': self.status,
            'list_of_rounds': self.list_of_rounds,
            'scores': self.scores,
            'adversaires': self.adversaires
        }
        return seliazed_tournament
