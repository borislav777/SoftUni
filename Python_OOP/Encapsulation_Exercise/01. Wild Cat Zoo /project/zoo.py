class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker):
        curr_worker = [w for w in self.workers if w.name == worker]
        if curr_worker:
            self.workers.remove(curr_worker[0])
            return f"{worker} fired successfully"
        return f"There is no {worker} in the zoo"

    def pay_workers(self):
        salaries = sum([w.salary for w in self.workers])
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_for_caries = sum([a.money_for_care for a in self.animals])
        if money_for_caries <= self.__budget:
            self.__budget -= money_for_caries
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f'You have {len(self.animals)} animals']
        lions = [repr(l) for l in self.animals if l.__class__.__name__ == 'Lion']
        result.append(f"----- {len(lions)} Lions:")

        result.append('\n'.join(lions))
        tigers = [repr(t) for t in self.animals if t.__class__.__name__ == 'Tiger']
        result.append(f"----- {len(tigers)} Tigers:")
        result.append('\n'.join(tigers))
        cheetahs = [repr(c) for c in self.animals if c.__class__.__name__ == 'Cheetah']
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.append('\n'.join(cheetahs))
        return '\n'.join(result)

    def workers_status(self):
        result = [f'You have {len(self.workers)} workers']
        keepers = [repr(k) for k in self.workers if k.__class__.__name__ == 'Keeper']
        result.append(f"----- {len(keepers)} Keepers:")
        result.append('\n'.join(keepers))
        care_takers = [repr(c) for c in self.workers if c.__class__.__name__ == 'Caretaker']
        result.append(f"----- {len(care_takers)} Caretakers:")
        result.append('\n'.join(care_takers))
        vets = [repr(v) for v in self.workers if v.__class__.__name__ == 'Vet']
        result.append(f"----- {len(vets)} Vets:")
        result.append('\n'.join(vets))
        return '\n'.join(result)
