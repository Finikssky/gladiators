import jsonpickle

class WeaponHandType():
	OneHand = "oh"
	TwoHand = "th"
	OneTwoHand = "oth"
	LeftHand = "lh"
	RightHand = "rh"	

class WeaponBaseType():
	Sword = "Sword"
	Axe = "Axe"
	Mace = "Mace"
	Chain = "Chain"
	Spear = "Spear"
	Trident = "Trident"
	Dagger = "Dagger"

class Weapon(object):
    def __init__(self, name, htype, wtype, damage, weight):
        self.name = name 
        self.htype = htype
        self.wtype = wtype
        self.damage = damage
        self.weight = weight