import jsonpickle

import weapons

class Gladiator(object):
    def __init__(self, name):

        self.name = name

        # primary_attrs
        self.agility = 0
        self.strength = 0
        self.endurance = 0
        self.luck = 0

        # secondary_attrs
        self.max_health = 0
        self.max_stamina = 0

        # skill and exp points
        self.pa_points = 10

        # things
        self.cur_lweapon = None
        self.cur_rweapon = None

        # system
        self.ai = 0

    def set_primary_attr(self, attr, val):
        if val < 0:
            return False

        try:
            diff = val - self.__dict__[attr]

            if diff > self.pa_points:
                print "Low points!"
                return False
            else:
                self.pa_points -= diff
                self.__dict__[attr] = val
                self.calculate_attrs()
        except:
            return False

    def calculate_attrs(self):
        self.cur_health = self.max_health = self.endurance * 8 + self.strength * 2
        self.cur_stamina = self.max_stamina = self.endurance * 7

    def take_damage(self, val):
        self.cur_health -= val
        if self.cur_health < 0:
            self.cur_health = 0

    def get_tired(self, val):
        self.cur_stamina -= val
        if self.cur_stamina < 0:
            self.cur_stamina  = 0

    def take_rest(self, val):
        self.cur_stamina += val
        if self.cur_stamina > self.max_stamina:
            self.cur_stamina = self.max_stamina

    def take_weapon(self, weapon, hand):

        if weapon.htype == weapons.WeaponHandType.TwoHand:
            self.cur_rweapon = weapon
            self.cur_lweapon = None

        else:
            if hand == "right":   
                if weapon.htype == weapons.WeaponHandType.OneHand or weapon.htype == weapons.WeaponHandType.RightHand or weapon.htype == weapons.WeaponHandType.OneTwoHand:
                    self.cur_rweapon = weapon
                else:
                    print "Can't take this weapon in right hand!"

            if hand == "left":
                if weapon.htype == weapons.WeaponHandType.OneHand or weapon.htype == weapons.WeaponHandType.LeftHand or weapon.htype == weapons.WeaponHandType.OneTwoHand:
                    self.cur_lweapon = weapon
                else:
                    print "Can't take this weapon in left hand!"