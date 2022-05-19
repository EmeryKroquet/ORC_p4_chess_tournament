from Models.classes.player import Player
from Models.classes.round import Round
from Models.classes.match import Match


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
    """ Modele réprésentant un tournoi """

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


def add_palyer(self):
    """Ajouter les joueurs dans notre liste des joueurs
    """
    self.players.append(Player)
    self.score[player.id] = [0, Player.rating]
    self.adversaires[Player.id] = []


def calculer_prochain_round(self):
    """ Appariement des joueurs pour le prochain tour,
        en fonction du classement pour le premier tour, puis en fonction du score""
    """
    if self.adversaires_round == 1:
        self.player = sorted(self.players, key=player.get_rating, reverse=True)

        first_half = self.players[:4]
        second_half = self.players[4:]
        list_of_matches = []

    for player_1, player_2 in zip(first_halh, second_half):
        match = Match('On going', player_1.id, player_2.id)
        list_of_matches.append(match)
        round_one = Round("round 1 |", 1, list_of_matches)
        self.list_of_rounds.append(round_one)
        self.add_adversaire()
        self.continu_round += 1

    else:
        sorted_players = sorted(self.score.items(),

                                key=lambda item: (item[0][1], item[1][1]),
                                reverse=True)

        list_of_matches = []
        matches = get_matches(sorted_players, self.adversaires)
        for pair in matches:
            match = Match('On going', pair[0][0], pair[0][1])
            list_of_matches.append(match)
            next_round = Round(f'round,{self.adversaire_round} |',
                               self.adversaire_round, list_of_matches)
            self.list_of_round.append(next_round)
            self.add_daversaires()
            self.continu_round += 1


def add_adversaire(self):
    """ Ajouter les adversaires avec le match du dernier tour"""


for match in self.list_of_round[-1].list_of_matches:
    # vérifier si match.id_joueur_2 n'est pas dans les adversaires de match.id_joueur_1
    if not self.adversaires[match.id_player_1].count(match.id_player_2):
        self.adversaires[match.id_player_1].append(match.id_player_2)
        # vérifier si match.id_player_1 n'est pas dans les adversaires de match.id_player_2
        if not self.adversairs[match.id_player_2].count(match.id_player_1):
            self.adversairs[match.id_player_2].append(match.id_player_1)


def end_round(self):
    """finir le round et mettre à jour le score.
    """
    self.list_of_round[-1].round_ended()
    list_round = self.continu_round - 1
    for match in self.list_of_rounds[last_round - 1].list_of_matches:
        self.scores[match.id_player_1][0] += match.score_player_1
        self.scores[match.id_player_2][0] += match.score_player_2
