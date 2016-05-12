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

            for x in team.units:
                self.move_phase(team, x)
                self.targeting_phase(team, x)

    def move_phase(self, team, unit):
        print "Move phase for '%s' from '%s' team!" % (unit.name, team.name)

        if not unit.ai:
            coords = raw_input("input coords:")
            print "Unit %s move to (%s)" % (unit.name, coords)
        else:
            pass

    def targeting_phase(self, team, unit):
        print "Targeting phase for '%s' from '%s' team!" % (unit.name, team.name)

        if not unit.ai:
            team_name = raw_input("input target team:")
            targ_name = raw_input("input target name:")
            print "Unit %s locked %s from '%s' team" % (unit.name, targ_name, team_name)
        else:
            pass