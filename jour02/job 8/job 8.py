def fibres(type,saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")

    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")

    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")

    elif type == "legume" and saison == "hiver":
        print("artichaut, aubergine, navet")

fibres("legume","hiver")
fibres("fruits","ete")
fibres("legume","ete")
fibres("fruits","hiver")