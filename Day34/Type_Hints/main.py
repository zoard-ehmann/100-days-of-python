age: int
name: str
height: float
is_human: bool

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if print(police_check()):
    print("You may pass.")
else:
    print("Pay a fine.")