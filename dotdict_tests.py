
import json
from dotdict import DotDict


def go():
    tests = {

        "single array":'{"main":["a","b"]}',
        "single entity":'{"person":{"name":"toto","age":"30"}}',
        "multiple unqualified entities":'{"persons":[{"name":"toto", "age":"30"}, {"name":"toutoune", "age":"24"}]}',
        "multiple qualified entities":'{"persons":[{"person":{"name":"toto", "sex":"M"}}, {"person":{"name":"toutoune", "sex":"F"}}]}',
        "single array as top":'["first", "second"]',
        "special character":'{"persons":[{"person":{"name":"t[oto", "sex":"M]"}}, {"person":{"name":"tou.toune", "sex":"#F"}}]}',
    }

    t="single array"

    print(t)
    s=tests[t]

    ff = json.loads(s)
    print(f"{ff=}")

    d2 = DotDict(ff)

    print(f"{d2.getValueFQN('main')=}")
    print(f"{d2.getValueFQN('main[0]')=}")
    print(f"{d2.getValueFQN('main[1]')=}")


    t="single entity"

    print(t)
    s=tests[t]

    ff = json.loads(s)
    print(f"{ff=}")

    d2 = DotDict(ff)

    print(f"{d2.getValueFQN('person')=}")
    print(f"{d2.getValueFQN('person.name')=}")
    print(f"{d2.getValueFQN('person.age')=}")


    t="multiple unqualified entities"
    print(t)
    s=tests[t]
    ff = json.loads(s)
    print(f"{ff=}")

    d2 = DotDict(ff)

    print(f"{d2.getValueFQN('persons')=}")
    print(f"{d2.getValueFQN('persons[#]')=}")
    print(f"{d2.getValueFQN('persons[0]')=}")
    print(f"{d2.getValueFQN('persons[0].name')=}")
    print(f"{d2.getValueFQN('persons[0].age')=}")
    print(f"{d2.getValueFQN('persons[1]')=}")
    print(f"{d2.getValueFQN('persons[1].name')=}")
    print(f"{d2.getValueFQN('persons[1].age')=}")


    t="multiple qualified entities"
    print(t)
    s=tests[t]


    ff = json.loads(s)
    print(f"{ff=}")

    d2 = DotDict(ff)

    print(f"{d2.getValueFQN('persons')=}")
    print(f"{d2.getValueFQN('persons[0]')=}")
    print(f"{d2.getValueFQN('persons[0].person')=}")
    print(f"{d2.getValueFQN('persons[0].person.name')=}")
    print(f"{d2.getValueFQN('persons[0].person.sex')=}")

    print(f"{d2.getValueFQN('persons[1]')=}")
    print(f"{d2.getValueFQN('persons[1].person')=}")
    print(f"{d2.getValueFQN('persons[1].person.name')=}")
    print(f"{d2.getValueFQN('persons[1].person.sex')=}")


    t="single array as top"
    print(t)
    s=tests[t]
    ff = json.loads(s)
    print(f"{ff=}")

    d2 = DotDict(ff)
    print(f"{d2.getValueFQN('first')=}")
    print(f"{d2.getValueFQN('second')=}")

    print(f"{d2.getValueFQN('Top[0]')=}")
    print(f"{d2.getValueFQN('Top[1]')=}")


    t="special character"
    print(t)
    s=tests[t]


    ff = json.loads(s)
    print(f"{ff=}")

    d2 = DotDict(ff)

    print(f"{d2.getValueFQN('persons')=}")
    print(f"{d2.getValueFQN('persons[0]')=}")
    print(f"{d2.getValueFQN('persons[0].person')=}")
    print(f"{d2.getValueFQN('persons[0].person.name')=}")
    print(f"{d2.getValueFQN('persons[0].person.sex')=}")

    print(f"{d2.getValueFQN('persons[1]')=}")
    print(f"{d2.getValueFQN('persons[1].person')=}")
    print(f"{d2.getValueFQN('persons[1].person.name')=}")
    print(f"{d2.getValueFQN('persons[1].person.sex')=}")


if __name__ == "__main__":

    go()

    


