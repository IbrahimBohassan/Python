def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 405:
            return "Not Allowed"
        case _:
            return "Something's wrong with the internet"
        
print(http_error(400))
print(http_error(404))
print(http_error(418))
print(http_error(401))
print(http_error(403))
print(http_error(405))
print(http_error(406))


print("=========================")
print("     Another Example     ")
print("=========================")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

where_is(Point(x=0, y=0))
where_is(Point(x=0, y=1))
where_is(Point(x=1, y=0))
where_is(Point(x=1, y=1))
where_is(Point(x=2, y=2))


