

from abc import ABC, abstractmethod


class Subproblem(ABC):

    def __init__(self, instance, partial_sol, partial_sol_val, *other_args):
        self.instance = instance
        self.partial_sol = partial_sol
        self.partial_sol_val = partial_sol_val
        self.other_args = other_args

    def get_instance(self):
        return self.instance

    def get_partial_sol(self):
        return self.partial_sol

    def get_other_args(self):
        return self.other_args

    def get_partial_sol_val(self):
        return self.partial_sol_val

    def get_all(self):
        a = list()
        a.append(self.instance)
        a.append(self.partial_sol)
        a.append(self.partial_sol_val)
        a.append(self.other_args)
        return a

    @abstractmethod
    def clone_sol(self):
        """
        clones the partial solution so it can be saved without
        being overridden in recursive calls
        :return:
        """
        pass


class BranchAndBound(ABC):

    def __init__(self, minimization=True):
        self.scale = 1
        if minimization:
            self.scale = -1


    def can_prune(self, subproblem : 'Subproblem', best_sol, best_val) -> bool:
        """
        :param subproblem:
        :param best_sol:
        :param best_val:
        :return:
        """
        if self.completeQ(subproblem):
            return True

        if self._can_prune(subproblem, best_sol, best_val) or not self.legalQ(subproblem):
            return True

        if self.scale*self.bound(subproblem) < self.scale*best_val:
            return True

        return False

    @abstractmethod
    def _can_prune(self, subproblem : 'Subproblem', best_sol, best_val) -> bool:
        """
        use any additional measures you wish to take for pruning here
        If you do not wish to implement, just have the method return False
        :param subproblem:
        :param best_sol:
        :param best_val:
        :return:
        """
        pass

    @abstractmethod
    def legalQ(self, subproblem : 'Subproblem')-> bool:
        """
        return true iff partial solution is legal
        for the given subproblem.

        If you are maintaining legality of your solution
        implicitly, you may just return True here.
        :param subproblem:
        :return:
        """
        pass

    @abstractmethod
    def completeQ(self, subproblem : 'Subproblem') -> bool:
        """
        return True iff partial solution for subproblem is a complete solution
        i.e. cannot be extended
        :param subproblem:
        :return:
        """

    @abstractmethod
    def bound(self, subproblem : 'Subproblem', *args, **kwargs)->float:
        """
        return an upper/lower bound on the value of some
        subproblem instance.
        :param subproblem:
        :param args:
        :param kwargs:
        :return:
        """
        pass


    @abstractmethod
    def get_next_choices(self, subproblem : 'Subproblem'):
        """
        generate next choice(s) to be made
        :param subproblem:
        :return:
        """
        pass

    @abstractmethod
    def gen_subproblem_with_choice(self, subproblem : 'Subproblem', choice ) -> Subproblem:
        """
        generates a new subproblem with this choice made

        :param subproblem:
        :param choice:
        :return:
        """
        pass

    @abstractmethod
    def restore_subproblem(self, subproblem : 'Subproblem', choice):
        """
        restore the subproblem back to its original values
        If you are copying lists, etc. you can skip this, but
        implementing carefully will speed up code quite a bit
        :param subproblem:
        :param choice:
        :return:
        """
        pass

    @abstractmethod
    def gen_subproblem_without_choice(self,subproblem : 'Subproblem', choice) -> Subproblem:
        """

        generates a new subproblem without this choice made...
        *If not applicable, then return None*

        :param subproblem:
        :param choice:
        :return:
        """
        pass

    def betterQ(self, subproblem : Subproblem, best_val) -> bool:
        """
        returns true iff the partial solution for the subproblem has
        better value that the best solution so far
        :param subproblem:
        :param best_val:
        :return:
        """
        return self.scale*subproblem.get_partial_sol_val() > self.scale*best_val


    @abstractmethod
    def solve(self, *args, **kwargs):
        """
        (1) create a subproblem for initial instance
        (2) initialize best_sol, best_val to defaults
        (3) call _branch_and_bound on subproblem and defaults
        (4) return the best solution found
        :param args:
        :param kwargs:
        :return:
        """
        pass



    def _branch_and_bound(self, subproblem : 'Subproblem', best_sol, best_val):
        #If we can prune, then we will terminate this branch and return
        #the better of the subproblem's solution and the best so far.
        #bound function is also used implicitly at this step in the
        #can_prune method


        if self.betterQ(subproblem, best_val):
            best_sol, best_val = subproblem.clone_sol(), subproblem.get_partial_sol_val()

        if self.can_prune(subproblem, best_sol, best_val):
            return best_sol, best_val


        # if we made it here, then there is a possibility that a
        # better solution exists in this subtree

        next_choices = self.get_next_choices(subproblem)
        #in the case where we are only making one next choice,
        #we will convert to a list so that for-loop works
        if not isinstance(next_choices, list):
            next_choices = [next_choices]

        for choice in next_choices:
            # i. generate a partial solution P' and subproblem
            # S' with that choice made
            with_choice = self.gen_subproblem_with_choice(subproblem,choice)

            #recursively find the best solution with choice made
            best_sol, best_val = self._branch_and_bound(with_choice,best_sol,best_val)
            self.restore_subproblem(with_choice, choice)

            #recursively find best solution without choice made
            without_choice = self.gen_subproblem_without_choice(subproblem, choice)
            if without_choice is not None:
                best_sol, best_val = self._branch_and_bound(without_choice, best_sol, best_val)
                self.restore_subproblem(without_choice, choice)

        return best_sol, best_val





