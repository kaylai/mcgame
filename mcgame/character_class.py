class Character(object):
    """Top level character class encompassing player characters
    and NPC's

    Args:
        object (_type_): _description_
    
    Questions #TODO:
    - Do NPC's have items and other traits like a player character does?
    - Can give attributes such as item. Then a character could own
    an item, and the item's attr can change as they progress, add
    soul gems, etc etc.
    - Need getters and setters
    """
    def __init__(self, name, race, birthsign, family_background, religion,
                 career_background, reason_for_adventuring, professional_contact,
                 personal_challenge):
        #TODO what attr do all chars have? Ex:
        # General stats:
        self.name = name
        self.race = race
        self.birthsign = birthsign
        self.family_background = family_background
        self.religion = religion
        self.career_background = career_background
        self.reason_for_adventuring = reason_for_adventuring
        self.professional_contact = professional_contact
        self.personal_challenge = personal_challenge
        
        self.items = None #Also need item class
        pass
    
class PlayerCharacter(Character):
    """Player character class

    Args:
        Character (_type_): _description_
    """
    def __init__(self):
        super().__init__()

class NonPlayerCharacter(Character):
    """NPC

    Args:
        Character (_type_): _description_
    """
    def __init__(self):
        super().__init__()