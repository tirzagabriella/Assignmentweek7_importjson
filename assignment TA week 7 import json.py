import json

# a. create function : OBJECT -> JSON
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# create Point objects
p = Point(1, 2)
# print(p.x)
# print(p.y)


def get_json_str(p):
    obj = {
        '__class__': type(p).__name__,
        'x': p.x,
        'y': p.y
    }
    return json.dumps(obj, indent=2)

# print created JSON objects
z = get_json_str(p)
print(z)

# b. create function : JSON -> OBJECT
def read_json_str(s):
  result = json.loads(str(s))
  return result

result = read_json_str(z)
print(result)