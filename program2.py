def greeting(name: str) -> str:
    return 'Hello ' + name

def greeting1(name1: str):
    return 'Hello ' + name1

@dec()
def greeting2(name):
    return 'Hello ' + name
    
@dec(a,b)
def greeting3(name: int,tame: float,lak)->int:
    return 'Hello ' + name

def foo(client_id: str) -> Union[list,bool]:
	pass

def f() -> Tuple[dict, str]:
    a = {1: 2}
    b = "hello"
    return a, b

Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

def feeder(get_next_item: Callable[[], str]) -> None:
 pass

@there(a="shffhh")
class ghd(Optimizer.optimizer):
	pass
