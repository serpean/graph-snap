# !python -m pip install snap-stanford
import snap


def test():
    status = False
    try:
        import snap

        version = snap.Version
        i = snap.TInt(5)
        if i == 5:
            status = True
    except:
        pass

    if status:
        print("SUCCESS, your version of Snap.py is %s" % (version))
    else:
        print("*** ERROR, no working Snap.py was found on your computer")


def test_graphviz():
    G = snap.GenGrid(snap.PUNGraph, 5, 3)
    G.DrawGViz(snap.gvlDot, "grid5x3.png", "Grid 5x3")


def test_plot():
    G = snap.GenPrefAttach(100000, 3)
    G.PlotInDegDistr("pref-attach", "PrefAttach(100000, 3) in Degree")


def load_undirected_graph(name, _type=None):
    print(f"--- Load undirected graph {name} ---")
    if _type == "str":
        return snap.LoadEdgeListStr(snap.TUNGraph, name, 0, 1)
    return snap.LoadEdgeList(snap.TUNGraph, name, 0, 1)


def load_directed_graph(name, _type=None):
    print(f"--- Load directed graph {name} ---")
    if _type == "str":
        return snap.LoadEdgeListStr(snap.TNGraph, name, 0, 1)
    return snap.LoadEdgeList(snap.TNGraph, name, 0, 1)


def print_size(graph):
    for p in graph.GetWccSzCnt():
        print("size %d: count %d" % (p.GetVal1(), p.GetVal2()))


def print_dim(G):
    print("Dim %s" % G.GetBfsFullDiam(100, False))


def highest_300(G):
    print("Top 300 highest")
    count = 0
    res = dict()
    for k, v in {p.GetVal1(): p.GetVal2() for p in sorted(G.GetDegCnt(), reverse=True)}.items():# degree, count
        if count >= 300:
            return res
        res.update({k: v})
        count += v
    return res


def remove_300(G, param=None):
    print("Removing nodes...")
    if param is None:
        raise Exception("No param")
    elif sum(list(param.values())) > 300:
        print(f"WARN More then 300 deletions {sum(list(param.values()))}")
    print(f"Num nodes before deletion {G3_d.GetNodes()}")
    for NI in G.Nodes():
        if NI.GetDeg() in param.keys() and param[NI.GetDeg()] > 0:
            G.DelNode(NI.GetId())
    print(f"Num nodes after deletion {G3_d.GetNodes()}")


if __name__ == '__main__':
    G0 = load_undirected_graph("data/0.edges")
    print_size(G0)

    G1 = load_undirected_graph("data/414.edges")
    print_size(G1)

    G3_d = load_directed_graph("data/links.tsv", "str")
    print_dim(G3_d)
    d_highest_300 = highest_300(G3_d)
    for k, v in d_highest_300.items(): print(f"Degree: {k} | Count: {v}")
    remove_300(G3_d, d_highest_300)
    print_dim(G3_d)

    G3_u = load_undirected_graph("data/links.tsv", "str")
    print_dim(G3_u)
    u_highest_300 = highest_300(G3_u)
    for k, v in u_highest_300.items(): print(f"Degree: {k} | Count: {v}")
    remove_300(G3_u, u_highest_300)
    print_dim(G3_d)







