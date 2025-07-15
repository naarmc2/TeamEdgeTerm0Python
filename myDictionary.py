info = {
    "name": "Nathania",
    "age": 17,
    "height": "5'5ft",
    "hobbies": ["painting","reading", "skateboarding"],
    "knows_python": True,
    "family": {"mother": "marcia", "father": "randon", "sister": "andrienne"}
}
print(info["name"])
print(info["age"])
print(info["family"]["mother"])

musician = {
    "name": "Buju Banton",
    "age":52,
    "nationality": 'Jamaican',
    "occupation": "singer",
    "numOfChildren": 17,
    "children": {"daughters": ['Shadai Myrie', 'Jodian Myrie'],
                 "sons": ['Jahazeil Myrie', 'Jahleel Myrie', 'Mark Myrie']},
    "songs": ['Untold Stories','Destiny','and Wanna Be Loved.']
}

name = musician['name']
age = musician["age"]
nationality =  musician["nationality"]
numChildren = musician['numOfChildren']
songs = musician['songs']
print(f"{name} is a {nationality} artist. He has {numChildren} children and here are some of his songs: {', '.join(songs)} ")