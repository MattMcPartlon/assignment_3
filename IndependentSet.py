from BranchAndBoundABC import BranchAndBound, Subproblem
from utils.datastructures.graph.SimpleGraph import SimpleGraph
from typing import Tuple
import DataGenerator as dg

class Max_IS_Subproblem(Subproblem):

    def __init__(self, G, non_nbrs, partial_sol, partial_sol_val, removed):
        super().__init__((G,non_nbrs),partial_sol, partial_sol_val, removed)

    def get_instance(self) -> Tuple[SimpleGraph,list]:
        return self.instance

    def clone_sol(self):
        return list(self.partial_sol)

    def get_other_args(self):
        return self.other_args[0]



class MaxIndSet(BranchAndBound):

    def __init__(self):
        super().__init__(minimization=False)


    def _can_prune(self, subproblem : Max_IS_Subproblem, best_sol, best_val) -> bool:
        return False

    def legalQ(self, subproblem : Max_IS_Subproblem)-> bool:
        return True

    def completeQ(self, subproblem : Max_IS_Subproblem) -> bool:
        G,non_nbrs = subproblem.get_instance()
        return len(non_nbrs)==0


    def bound(self, subproblem : Max_IS_Subproblem, *args, **kwargs)->float:
        G , non_nbrs = subproblem.get_instance()
        non_nbr_degs = [G.get_degree(u,non_nbrs) for u in non_nbrs]
        min_deg = min(non_nbr_degs)
        return subproblem.get_partial_sol_val()+len(non_nbrs)-min_deg


    def get_next_choices(self, subproblem : 'Subproblem'):
        G, non_nbrs = subproblem.get_instance()
        lowest_degree, lowest_v = G.n(), None
        assert len(non_nbrs)!=0
        for u in non_nbrs:
            deg = G.get_degree(u, non_nbrs)
            if deg<lowest_degree:
                lowest_degree, lowest_v = deg, u
        return lowest_v


    def gen_subproblem_with_choice(self, subproblem : Max_IS_Subproblem, choice ) -> Max_IS_Subproblem:
        """
        remove vertices incident to choice from the subgraph under consideration
        """
        instance, partial_sol, partial_sol_val, _ = subproblem.get_all()
        G , non_nbrs = instance
        #non_nbrs are updated to reflect the choice - i.e.
        #removing all vertices adjacent to choice, and storing them in
        #"removed" so that they can be added back efficiently later
        removed = [choice]
        for u in non_nbrs:
            if G.adjacentQ(u,choice):
                removed.append(u)
        for u in removed:
            non_nbrs.remove(u)
        partial_sol.add(choice)
        return Max_IS_Subproblem(G,non_nbrs,partial_sol,len(partial_sol),removed)


    def gen_subproblem_without_choice(self, subproblem : 'Subproblem', choice) -> Subproblem:
        instance, partial_sol, partial_sol_val, _ = subproblem.get_all()
        G, non_nbrs = instance
        non_nbrs.remove(choice)
        removed = [choice]
        return Max_IS_Subproblem(G,non_nbrs,partial_sol,partial_sol_val,removed)

    def restore_subproblem(self, subproblem: 'Subproblem', choice):
        """
        Since I am modifying the instance variable of the original subproblem directly,
        I have to restore them after a recursive call.
        """
        removed = subproblem.get_other_args()
        _, non_nbrs = subproblem.get_instance()

        for u in removed:
            non_nbrs.add(u)

        partial_sol = subproblem.get_partial_sol()
        if choice in partial_sol:
            partial_sol.remove(choice)


    def solve(self, G : SimpleGraph):
        non_nbrs = set()
        for v in G.get_vertices():
            non_nbrs.add(v)
        partial_sol = set()
        partial_sol_val = 0
        removed = []
        best_sol = []
        best_val = 0
        starting_instance = Max_IS_Subproblem(G,non_nbrs,partial_sol,partial_sol_val,removed)
        best_sol, best_val = self._branch_and_bound(starting_instance, best_sol, best_val)
        return best_sol


p = 0.01
graph = dg.gen_vtx_weighted_graph(10, p=p)
alg = MaxIndSet()
sol = alg.solve(graph)
print(len(sol))
