
class character:
    def __init__(self, armour, health_current, health_max, initiative, initiative_mod, weapon, attr_dex):
        self.armour = armour
        self.health_current = health_current
        self.health_max = health_max
        self.initiative = initiative
        self.initiative_mod = initiative_mod
        self.weapon = weapon
        self.attr_dex = attr_dex
        return

    def calculate_initiative(self, initiative_roll):
        self.initiative = initiative_roll + self.attr_dex + self.initiative_mod
        return 

    



#####
# Tests
#####

def character_class_should_report_values_correctly():
    # Arrange
    armour = "leather"
    health_current = 35
    health_max = 50
    initiative = None
    initiative_mod = 2
    weapon = "hvy pistol"
    attr_dex = 1
    
    # Act
    player = character(armour, health_current, health_max, initiative, initiative_mod, weapon, attr_dex)

    # Assert
    assert(player.armour == armour)
    assert(player.health_current == health_current)
    assert(player.health_max == health_max)
    assert(player.initiative == initiative)
    assert(player.weapon == weapon)
    #print("Passed")
    return

def calculate_initiative_should_set_initiative_correctly():
    # Arrange
    armour = "leather"
    health_current = 35
    health_max = 50
    initiative = None
    initiative_mod = 2
    weapon = "hvy pistol"
    attr_dex = 1

    initiative_roll = 15
    expected_initiave_result = 18

    # Act
    player = character(armour, health_current, health_max, initiative, initiative_mod, weapon, attr_dex)
    player.calculate_initiative(initiative_roll)
    
    # Assert
    assert(expected_initiave_result == player.initiative)
    #print("Passed")
    return

if __name__ == "__main__":
    character_class_should_report_values_correctly()
    calculate_initiative_should_set_initiative_correctly()
