import weapons
import skills
import gladiators
import battle

me = gladiators.Gladiator("Sneek")
me.set_primary_attr("agility", 4)
me.set_primary_attr("strength", 2)
me.set_primary_attr("endurance", 2)
me.set_primary_attr("luck", 2)


en = gladiators.Gladiator("Elefant")
en.ai = 1
en.set_primary_attr("agility", 2)
en.set_primary_attr("strength", 3)
en.set_primary_attr("endurance", 4)
en.set_primary_attr("luck", 1)

flamberg = weapons.Weapon("flamberg", weapons.WeaponHandType.TwoHand, weapons.WeaponBaseType.Sword, 15, 7.0)
knife = weapons.Weapon("knife", weapons.WeaponHandType.OneHand, weapons.WeaponBaseType.Dagger, 3, 0.8)

en.battle_inventory.equip_weapon(flamberg, "right")

me.battle_inventory.equip_weapon(knife, "right")
me.battle_inventory.equip_weapon(knife, "left")

battle = battle.Battle()
battle.add_team("blue")
battle.add_team("red")

battle.add_team_unit("blue", me)
battle.add_team_unit("red", en)

battle.turn()
