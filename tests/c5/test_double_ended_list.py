from chapter5 import DoubleEndedList as delist


class TestDoubleEndedList:
    dlist = delist.DoubleEndedList()
    people = ["Amine", "Naima", "Nassim", "Kahina"]
    ages = [30, 28, 27, 31]

    after = None
    for i, person in enumerate(people):
        if after is not None:
            dlist.insertAfter(ages[i - 1], (ages[i], people[i]), key=lambda x: x[0])
        else:
            dlist.insert((ages[i], people[i]))
            after = person

    assert dlist.getFirst().getData() == (30, "Amine")
    assert dlist.getLast().getData() == (31, "Kahina")
    assert (
        str(dlist) == "[(30, 'Amine')->(28, 'Naima')->(27, 'Nassim')->(31, 'Kahina')]"
    )
