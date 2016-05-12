import arena
import gladiators
import random

class Team():
    def __init__(self, name):
        self.name = name
        self.units = []

        self.phase_done = 0

class Battle():
    def __init__(self):
        self.teams = {}

    def set_arena(self, arena):
        self.arena = arena

    def add_team(self, name):
        if not self.teams.has_key(name):
            self.teams[name] = Team(name)

    def add_team_unit(self, name, unit):
        self.teams[name].units.append(unit)

    def next_team_turn(self):
        tmp = [x for x in self.teams if not self.teams[x].phase_done ]
        if len(tmp) == 0:
            return None

        ret = self.teams[random.choice(tmp)]
        ret.phase_done = 1
        return ret

    def turn(self):

        while True:
            team = self.next_team_turn()
            if team == None:
                break

            print "Team '%s' turn!" % team.name

