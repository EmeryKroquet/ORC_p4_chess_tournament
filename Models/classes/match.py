class Match:
    """Créer un tournoi entre 2 joueurs
    """

    def __init__(self, status, id_player_1, id_player_2, score_player_1=0, score_player_2=0, ):
        self.status = status
        self.id_player_1 = id_player_1
        self.id_player_2 = id_player_2
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def __str__(self):
        return f'Player {self.id_player_1} ({self.score_player_1, pts})'\
            f'--VS--' \
            f'Player {self.id_player_2} ({self.score_player_2, pts})'

    def scoring(self, winner):
        """choisir un gagnant sur la base de l'ID du joueur et
            mettre à jour le statut de la manche

        """

        if self.id_player_1 == winner:
            self.score_player_1 = 1

        elif self.id_player_2 == winner:
            self.score_player_2 = 1

        else:
            self.score_player_1 == 0.5
            self.score_player_2 == 0.5
        self.status = 'Round ended !'

    def serialize(self):
        """ serialize the match """
        serialized_match = {'status': self.status,
                            'id_player_1': self.id_player_1,
                            'id_player_2': self.id_player_2,
                            'score_player_1': self.score_player_1,
                            'score_player_2': self.score_player_2,

                            }
